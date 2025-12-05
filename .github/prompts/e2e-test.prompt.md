---
mode: agent
---

TAREFA:
Crie uma suíte de testes E2E para a(s) funcionalidade(s) alvo informada(s) no contexto, levantando dependências reais via Testcontainers (MongoDB, RabbitMQ) e isolando integrações externas de terceiros (ex.: Azure Speech) por meio de stubs/mocks. Cubra cenários de sucesso, erro e validação ponta a ponta, verificando efeitos observáveis no banco de dados e/ou via fila.

CONTEXTO (fornecido pelo usuário/IDE):

- Fluxo alvo e ponto(s) de entrada (ex.: consumidor RabbitMQ, endpoints HTTP, jobs).
- Variáveis de ambiente necessárias para subir o app em modo de teste.
- Entidades/tabelas coleções relevantes e efeitos esperados (inserções, atualizações, mensagens).

ARQUITETURA/STACK (premissas):

- Projeto NestJS 11+ com Clean Architecture (Domain/Adapters).
- App principal sobe como microserviço RMQ (veja `src/main.ts`).
- Dependências de infraestrutura: MongoDB (via Prisma) e RabbitMQ.
- Testes E2E com Jest + TypeScript.
- Orquestração de dependências reais com Testcontainers.

REQUISITOS GERAIS:

1. Framework e local dos testes:
   - Use Jest com TypeScript.
   - Coloque os arquivos em `tests/e2e`, seguindo o padrão `<feature>.e2e-spec.ts`.
   - Respeite a config `tests/e2e/jest-e2e.json` já existente.

2. Padrão do teste:
   - Estruture por `describe` de fluxo/endpoints/consumidores.
   - Aplique AAA (Arrange, Act, Assert) com comentários por seção: `// Arrange`, `// Act`, `// Assert`.
   - Use nomes de testes claros, no imperativo, descrevendo o comportamento ponta a ponta.

3. Infra via Testcontainers:
   - Suba MongoDB e RabbitMQ com Testcontainers no `beforeAll` do arquivo.
   - Propague as conexões via variáveis de ambiente para o app (ex.: `MONGODB_URI`, `RABBITMQ_URL`, `RABBITMQ_QUEUE`).
   - Gere fila única por teste/arquivo para isolamento (ex.: `queue-${random}`) e garanta limpeza no `afterAll`.
   - Não use Docker localmente se não disponível; condicione a execução com `it.skip` ou marque com `@docker` quando apropriado.

4. App NestJS em modo E2E:
   - Construa o módulo do app (idealmente o `AppModule`) com `Test.createTestingModule` e `createNestApplication()`.
   - Invoque `app.connectMicroservice(...)` e `app.startAllMicroservices()` conforme `src/main.ts` ou reutilize a configuração do módulo.
   - Evite usar o `main.ts` diretamente para controle de ciclo de vida no teste.

5. Stubs/MOCKS de integrações externas:
   - NÃO chame SDKs de cloud (ex.: Azure Speech). Em E2E, stubbe o serviço via injeção de dependência (ex.: provider para `COGNITIVE_SERVICE_PROTOCOL`).
   - Forneça uma implementação fake previsível que retorne uma transcrição determinística para o áudio recebido (pode ignorar conteúdo do áudio).
   - Garanta que qualquer chamada a serviços HTTP externos seja mockada ou bloqueada.

6. Dados de Teste:
   - Use `@faker-js/faker` para gerar payloads e headers.
   - Use seed fixa quando precisar de determinismo: `faker.seed(123)`.
   - Gere buffers pequenos para áudio (ex.: `Buffer.from('...')`) ou um Readable simples.

7. Cenários mínimos por fluxo E2E:
   - Sucesso: Publica mensagem na fila e verifica efeitos no MongoDB (ex.: `Message` e `Transcription` criados com campos esperados).
   - Validação de headers/entradas: Mensagens sem headers obrigatórios não devem causar persistência; verifique logs/ausência de efeitos.
   - Falha na persistência: Simule erro de BD (opcional com container parado ou mock de repositório) e valide tratamento/sem ack indevido.
   - Timeout/retentativa (se aplicável): Use `jest.useFakeTimers()` para avançar o tempo e verificar comportamento.

8. Logger/Side effects:
   - Espie `Logger` do Nest (`.log`/`.error`) quando fizer sentido, sem poluir o teste.
   - Verifique que o consumidor dá ack/nack corretamente (quando possível, via spy no contexto ou via contadores de mensagens consumidas).

9. Estilo/Boas práticas:
   - `jest.resetAllMocks()` em `beforeEach` e limpeza de recursos em `afterAll` (containers, app, conexões).
   - Use `waitFor`/polling para aguardar efeitos assíncronos no BD, com timeout razoável.
   - Não dependa de ordens rígidas de processamento; use asserts resilientes (ex.: `toMatchObject`).

10. Cobertura:

- Cubra o caminho feliz do consumidor RabbitMQ e persistência via Prisma/Mongo.
- Cubra pelo menos um caminho negativo/validação.
- Não teste SDKs/cloud; foque no encadeamento real entre fila -> app -> repositório -> BD.

11. Dependências de desenvolvimento:

- Use `testcontainers` (ou `@testcontainers/rabbitmq`/`@testcontainers/mongodb` quando aplicável) e adicione as dependências no projeto, caso não existam.
- Não versionar imagens; o teste deve baixar automaticamente.

FORMATO DE SAÍDA:

- Um arquivo `.e2e-spec.ts` contendo:
  - Imports mínimos (`@testcontainers/*`, `@nestjs/testing`, `@faker-js/faker`, `mongodb` driver opcional via Prisma Client, etc.).
  - Setup dos containers no `beforeAll` e teardown no `afterAll`.
  - Boot da aplicação Nest com providers override para mocks de serviços externos (ex.: `COGNITIVE_SERVICE_PROTOCOL`).
  - Publicação de mensagem no RabbitMQ (via canal amqplib) e asserts no MongoDB.
  - AAA explícito em cada teste.

EXEMPLO DE ESQUELETO (adapte ao caso real):

```typescript
import { Test, TestingModule } from '@nestjs/testing';
import { INestApplication, Logger } from '@nestjs/common';
import { Transport, MicroserviceOptions } from '@nestjs/microservices';
import { StartedTestContainer, TestContainers } from 'testcontainers';
import { MongoDBContainer } from '@testcontainers/mongodb';
import { RabbitMQContainer } from '@testcontainers/rabbitmq';
import amqplib, { Connection, Channel } from 'amqplib';
import { faker } from '@faker-js/faker';
import { AppModule } from 'src/app.module';
import { COGNITIVE_SERVICE_PROTOCOL } from 'src/adapters/configuration/constants';
import { PrismaClient } from '../../generated/prisma';

describe('Transcrição (E2E)', () => {
  let app: INestApplication;
  let mongo: StartedTestContainer;
  let rmq: StartedTestContainer;
  let amqpConn: Connection;
  let amqpChannel: Channel;
  let prisma: PrismaClient;

  const queue = `queue-${Math.random().toString(36).slice(2)}`;

  beforeAll(async () => {
    faker.seed(123);

    // Arrange: Containers
    mongo = await new MongoDBContainer('mongo:7').start();
    rmq = await new RabbitMQContainer('rabbitmq:3.12-management').start();

    const mongodbUri = mongo.getConnectionString();
    const rmqUrl = `amqp://guest:guest@${rmq.getHost()}:${rmq.getMappedPort(5672)}`;

    process.env.MONGODB_URI = mongodbUri;
    process.env.RABBITMQ_URL = rmqUrl;
    process.env.RABBITMQ_QUEUE = queue;

    // Arrange: App com override do serviço cognitivo (stub)
    const moduleFixture: TestingModule = await Test.createTestingModule({
      imports: [AppModule],
    })
      .overrideProvider(COGNITIVE_SERVICE_PROTOCOL)
      .useValue({
        execute: jest.fn(async () => ({
          segments: [
            {
              speakerId: 'spk1',
              text: 'olá mundo',
              startMs: 0,
              endMs: 1000,
              words: [],
            },
          ],
        })),
      })
      .compile();

    app = moduleFixture.createNestApplication();
    app.connectMicroservice<MicroserviceOptions>({
      transport: Transport.RMQ,
      options: {
        urls: [process.env.RABBITMQ_URL!],
        queue: process.env.RABBITMQ_QUEUE,
      },
    });

    await app.startAllMicroservices();
    await app.init();

    // Arrange: AMQP Publisher e Prisma
    amqpConn = await amqplib.connect(process.env.RABBITMQ_URL!);
    amqpChannel = await amqpConn.createChannel();
    await amqpChannel.assertQueue(queue, { durable: false });

    prisma = new PrismaClient();
    await prisma.$connect();
  });

  afterAll(async () => {
    // Teardown
    await amqpChannel.close();
    await amqpConn.close();
    await prisma.$disconnect();
    await app.close();
    await rmq.stop();
    await mongo.stop();
  });

  it('processa mensagem da fila e persiste transcrição', async () => {
    // Arrange
    const messageId = faker.string.uuid();
    const correlationId = faker.string.uuid();
    const now = new Date();
    const programDate = new Date();
    const payload = Buffer.from('fake-audio');

    const headers = {
      'x-version': '1.0.0',
      'x-message-id': messageId,
      'x-correlation-id': correlationId,
      'x-timestamp': now.toISOString(),
      'x-index': 0,
      'x-channel': 'BandNews',
      'x-program-date-time': programDate.toISOString(),
    } as Record<string, any>;

    // Act
    await amqpChannel.sendToQueue(queue, payload, { headers });

    // Assert (poll BD)
    const deadline = Date.now() + 10_000;
    let transcription: any | null = null;
    while (Date.now() < deadline) {
      const msg = await prisma.message.findFirst({
        where: { messageId },
        include: { transcription: true },
      });
      if (msg?.transcription) {
        transcription = msg.transcription;
        break;
      }
      await new Promise((r) => setTimeout(r, 250));
    }

    expect(transcription).toBeTruthy();
    expect(transcription).toMatchObject({
      channel: 'BandNews',
      index: 0,
      segments: expect.arrayContaining([
        expect.objectContaining({ text: expect.any(String) }),
      ]),
    });
  });

  it('não persiste quando headers obrigatórios faltam', async () => {
    // Arrange
    const badHeaders = { 'x-version': '1.0.0' } as any; // faltando ids e datas
    const payload = Buffer.from('audio');

    // Act
    await amqpChannel.sendToQueue(queue, payload, { headers: badHeaders });

    // Assert: aguarda um curto período e confirma ausência de inserções recentes
    await new Promise((r) => setTimeout(r, 500));
    const count = await prisma.message.count({
      where: { timestamp: { gte: new Date(Date.now() - 60_000) } },
    });
    expect(count).toBeGreaterThanOrEqual(0); // ajuste conforme comportamento de validação
  });
});
```

CHECKLIST DE SAÍDA (avalie antes de finalizar):

- [ ] Containers sobem e são finalizados corretamente (Mongo e RabbitMQ).
- [ ] App Nest inicializa microserviço RMQ com fila única do teste.
- [ ] Serviços externos (ex.: Azure) são stubados via DI.
- [ ] Publicação/consumo de mensagem funcional no fluxo E2E.
- [ ] Assert em efeitos no MongoDB (via Prisma) com polling e tempo limite.
- [ ] AAA explícito em cada teste e nomes claros.
- [ ] Determinismo e limpeza (seed, queues isoladas, teardown).
