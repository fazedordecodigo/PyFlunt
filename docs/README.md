PORTUGUÊS | [ENGLISH](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/README_EN.md)

# 🐍 PyFlunt: Domain Notification Pattern

Implementação Python inspirada no [Flunt](https://github.com/andrebaltieri/flunt) (.NET)

[![Último Lançamento no PyPI](https://img.shields.io/pypi/v/flunt.svg)](https://pypi.org/project/flunt/)
[![python](https://img.shields.io/pypi/pyversions/flunt.svg)](https://pypi.org/project/flunt/)
[![Downloads](https://static.pepy.tech/badge/flunt/month)](https://pepy.tech/project/flunt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/discord/1211477389830393866?logo=discord&label=Discord&color=5865F2&logoColor=white)](https://discord.gg/HNwFHQWX)


[![Avaliação de Segurança](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Confiabilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Manutenibilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Vulnerabilidades](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)


Flunt te auxilia a implementar Domain Notification Pattern em sua aplicação para centralizar erros e mudanças em determinadas ações e entidades.

Flunt surgiu de duas necessidades: implementar o Domain Notification Pattern para substituir exceções no nível de domínio da aplicação e reduzir a quantidade de IFs (complexidade) usando uma abordagem baseada em contratos.

Assim, basicamente o que o Flunt faz é adicionar uma lista de Notificações à sua classe e vários métodos para interagir com ela.

## ➡️ Como usar

### 🔧 Instalação

````bash
pip install flunt
````

### 🔔 Notifiable

````python
from flunt.notifications.notifiable import Notifiable

class Nome(Notifiable):
    def __init__(self, nome):
        super().__init__()

        if len(nome) < 3:
            self.add_notification(field='nome', message='nome inválido')
        self._nome = nome
````

### 📜 Contract
````python
"""Módulo Objetos de Valor."""
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Nome(Notifiable):
    """Classe Objeto de Valor Nome."""

    def __init__(self, primeiro_nome, ultimo_nome):
        """Encontrar 'Construtor'."""
        super().__init__()
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.add_notifications(
            Contract()
            .requires(self.primeiro_nome, 'primeiro nome')
            .requires(self.ultimo_nome, 'último nome')
            .is_greater_than(
                value=self.primeiro_nome,
                comparer=3,
                field="primeiro_nome",
                message="Mínimo de 3 caracteres",
            )
            .is_greater_than(
                value=self.ultimo_nome,
                comparer=3,
                field="ultimo_nome",
                message="Mínimo de 3 caracteres",
            )
            .get_notifications()
        )


nome = Nome('Emerson', 'Delatorre')
if not nome.is_valid:
    for notification in nome.get_notifications():
        print(notification)

````

## Contribuindo

Consulte nosso DevGuide no link a seguir: [CONTRIBUTING](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CONTRIBUTING.md)

## Registro de Alterações

Consulte nosso registro de alterações no link a seguir: [CHANGELOG](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CHANGELOG.md)

## 📄 Licença

Este projeto contém a licença MIT. Consulte o arquivo [LICENSE](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/LICENSE).

## Mods
* [Flunt para C# (Original)](https://github.com/andrebaltieri/Flunt)
* [Flunt.Br](https://github.com/lira92/flunt.br)
* [Flunt para Java](https://github.com/carlosbritojun/jflunt)
* [Flunt para JavaScript](https://github.com/jhonesgoncal/flunt)
* [Flunt para PHP](https://github.com/matheusbloise/flunt-php)
