# Guia de Mensagens de Commit e Pull Requests

## Visão Geral

Este guia combina as melhores práticas do [Chris Beams](http://chris.beams.io/posts/git-commit/) com a especificação [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) e integração com Azure Boards para o projeto de transcrição.

## TaskId Azure Boards

Inclua o ID: `31218`
- Sempre inclua o ID do Work Item no formato `#xxxxx` (ex: `#12345`) na mensagem de commit.
- Coloque o ID no rodapé da mensagem, em uma linha separada.
- Para commits curtos, pode ser adicionado ao final do assunto.


## Estrutura da Mensagem de Commit

```xml
<commit-message>
	<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert</type>
	<scope>(transcription|consumer|repository|service|config|pipeline)</scope>
	<description>Resumo imperativo e conciso da mudança</description>
	<body>(opcional: explicação mais detalhada do que e por quê)</body>
	<footer>(opcional: BREAKING CHANGE: detalhes, ou #xxxxx)</footer>
</commit-message>
```

### Tipos de Commit

* **feat**: ✨ Uma nova funcionalidade
* **fix**: 🐛 Uma correção de bug
* **docs**: 📝 Apenas alterações na documentação
* **style**: 💄 Alterações que não afetam o significado do código (espaços em branco, formatação, ponto e vírgula ausente, etc)
* **refactor**: ♻️ Uma alteração de código que não corrige um bug nem adiciona uma funcionalidade
* **test**: ✅ Adicionando ou atualizando testes
* **chore**: 🔧 Alterações no processo de build ou em ferramentas e bibliotecas auxiliares
* **perf**: ⚡️ Uma alteração de código que melhora o desempenho
* **ci**: 👷 Alterações nos arquivos e scripts de configuração de CI (Integração Contínua)
* **build**: 🏗️ Alterações que afetam o sistema de build ou dependências externas
* **revert**: ⏪ Reverte um commit anterior
* **wip**: 🚧 Trabalho em andamento
* **security**: 🔒 Alterações relacionadas à segurança
* **i18n**: 🌐 Internacionalização e localização
* **a11y**: ♿ Melhorias de acessibilidade
* **ux**: 🎨 Melhorias na experiência do usuário
* **ui**: 🖌️ Alterações na interface do usuário
* **config**: 🔧 Alterações em arquivos de configuração
* **deps**: 📦 Atualizações de dependências
* **infra**: 🌐 Alterações de infraestrutura
* **init**: 🎉 Commit inicial
* **analytics**: 📈 Códigos de analytics ou rastreamento
* **seo**: 🔍 Melhorias de SEO
* **legal**: ⚖️ Alterações de licença ou legais
* **typo**: ✏️ Correções de erros de digitação
* **comment**: 💬 Adicionando ou atualizando comentários no código
* **example**: 💡 Adicionando ou atualizando exemplos
* **mock**: 🤖 Adicionando ou atualizando mocks
* **hotfix**: 🚑 Correção crítica e urgente
* **merge**: 🔀 Mesclando branches
* **cleanup**: 🧹 Limpeza de código
* **deprecate**: 🗑️ Marcando código ou funcionalidades como obsoletos
* **move**: 🚚 Movendo ou renomeando arquivos
* **rename**: ✏️ Renomeando arquivos ou variáveis
* **split**: ✂️ Dividindo arquivos ou funções
* **combine**: 🧬 Combinando arquivos ou funções
* **add**: ➕ Adicionando arquivos ou funcionalidades
* **remove**: ➖ Removendo arquivos ou funcionalidades
* **update**: ⬆️ Atualizando arquivos ou funcionalidades
* **downgrade**: ⬇️ Fazendo downgrade de arquivos ou funcionalidades
* **patch**: 🩹 Aplicando patches
* **optimize**: 🛠️ Otimizando código

### Escopos Sugeridos

Para este projeto de transcrição, use escopos relevantes:

- **transcription**: Lógica de transcrição e processamento
- **consumer**: Consumidor RabbitMQ
- **repository**: Camada de dados e Prisma
- **service**: Serviços de domínio ou Azure
- **config**: Configurações e constantes
- **pipeline**: CI/CD e Azure DevOps
- **docker**: Configurações de containerização

## Regras do Chris Beams

1. **Separe assunto do corpo com uma linha em branco**
2. **Limite o assunto a ~72 caracteres**
3. **Capitalize o assunto**
4. **Não termine o assunto com ponto**
5. **Use o modo imperativo no assunto**
6. **Quebre o corpo em ~72 caracteres**
7. **Use o corpo para explicar o que e por quê, não como**

## Integração Azure Boards

- **Work Item ID**: Sempre inclua `#xxxxx` (ou ID específico do Work Item)
- **Posicionamento**: Preferencialmente no rodapé após o corpo, em linha separada
- **Commits curtos**: Pode incluir `#xxxxx` ao final do assunto se não houver corpo

## Exemplos Práticos

```xml
<examples>
	<example>feat(transcription): adiciona suporte à diarização do Azure Speech #xxxxx</example>
	<example>fix(consumer): corrige timeout na fila RabbitMQ #xxxxx</example>
	<example>docs: atualiza instruções de deployment no README #xxxxx</example>
	<example>refactor(repository): melhora performance das consultas MongoDB #xxxxx</example>
	<example>chore(deps): atualiza dependências do NestJS #xxxxx</example>
	<example>ci: ajusta pipeline de build no Azure DevOps #xxxxx</example>
</examples>
```

### Exemplo com Corpo

```text
feat(service): adiciona retry automático para falhas do Azure Speech

Implementa mecanismo de retry exponencial para lidar com timeouts
e falhas temporárias do serviço Azure Speech-to-Text. Melhora a
resiliência do sistema em ambientes de alta carga.

#xxxxx
```

### Exemplo Breaking Change

```text
feat!: altera estrutura de resposta da API de transcrição

BREAKING CHANGE: O campo 'segments' agora é um array de objetos
com propriedades 'speaker' e 'text' em vez de strings simples.
Clientes precisam atualizar o parsing da resposta.

#xxxxx
```

## Validação

```xml
<validation>
	<type>Deve ser um dos tipos permitidos. Veja https://www.conventionalcommits.org/pt-br/v1.0.0/#especificacao</type>
	<scope>Opcional, mas recomendado para clareza no contexto do projeto</scope>
	<description>Obrigatório. Use o modo imperativo (ex: "adiciona", não "adicionado")</description>
	<body>Opcional. Use para contexto adicional sobre o que e por quê</body>
	<footer>Use para mudanças breaking ou referências do Azure Boards (#xxxxx)</footer>
</validation>
```

## Armadilhas Comuns

❌ **Evite:**

- `fix: bug corrigido` (muito vago)
- `feat: nova feature` (redundante)
- `Update README.md` (não segue convenção)
- `Fixed issue with authentication` (não está em português)

✅ **Prefira:**

- `fix(auth): corrige validação de token JWT #xxxxx`
- `feat(transcription): adiciona suporte a múltiplos idiomas #xxxxx`
- `docs: atualiza README com instruções de instalação #xxxxx`
- `fix(consumer): corrige problema de autenticação #xxxxx`

## Pull Requests

Para PRs, aplique o mesmo padrão:

**Título:** Siga a convenção de commits  
**Descrição:** Deve responder:

- O que mudou?
- Por quê?
- Mudanças breaking?
- Impacto em infraestrutura (RabbitMQ/MongoDB/Azure)?

**Exemplo de título de PR:**

```
feat(transcription): adiciona diarização e detecção de idioma #xxxxx
```

## Comando Final

```xml
<final-step>
	<cmd>git commit -m "type(scope): description #xxxxx"</cmd>
	<note>Substitua pela sua mensagem construída. Inclua corpo e rodapé se necessário usando -m múltiplos.</note>
	<example>git commit -m "feat(service): adiciona retry automático" -m "Implementa retry exponencial para Azure Speech" -m "#xxxxx"</example>
</final-step>
```
