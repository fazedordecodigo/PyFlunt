ENGLISH | [PORTUGUÊS](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/README.md)

# 🐍 PyFlunt: Domain Notification Pattern

Python implementation of Domain Notification Pattern inspired by [Flunt](https://github.com/andrebaltieri/flunt) (.NET)

[![Latest Release on PyPI](https://img.shields.io/pypi/v/flunt.svg)](https://pypi.org/project/flunt/)
[![Python Versions](https://img.shields.io/pypi/pyversions/flunt.svg)](https://pypi.org/project/flunt/)
[![Downloads](https://static.pepy.tech/badge/flunt/month)](https://pepy.tech/project/flunt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/discord/1211477389830393866?logo=discord&label=Discord&color=5865F2&logoColor=white)](https://discord.gg/HNwFHQWX)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-yellow.svg)](https://matrix.to/#/#pyflunt:gitter.im)


[![Avaliação de Segurança](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Confiabilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Avaliação de Manutenibilidade](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Vulnerabilidades](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fazedordecodigo_PyFlunt&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fazedordecodigo_PyFlunt)

Flunt is a way to implement a notification pattern in your application to centralize errors and changes in certain actions and entities.

Flunt was born out of two needs: implementing the Domain Notification Pattern to replace domain-level exceptions in the application and reducing the amount of IFs (complexity) by using a contract-based approach.

Thus, basically what Flunt does is add a list of Notifications to your class and various methods to interact with it.

## ✨ Highlights

- Python 3.11+ compatible with **no runtime dependencies**.
- Fluent, chainable validations built on the Domain Notification Pattern.
- Specialized contracts for numbers, datetime, URLs, and Brazilian documents (CPF/CNPJ).
- Centralized notifications via `Notifiable`, reducing scattered `if` checks and domain exceptions.
- Full documentation in `docs/` and on the site (link below).

### New validation contracts

Beyond the base contract, the library now includes specialized contracts for common scenarios:

- `NumericValidationContract` for numeric values (ranges, limits, sign)
- `DateTimeValidationContract` for datetime values (intervals, minimum/maximum)
- `UrlValidationContract` for URLs
- `BrazilianDocumentValidationContract` for Brazilian documents (CPF/CNPJ)

Check the docs in `docs/validations/` for detailed examples.

## ➡️ How to use

### 🔑 Requirements

- Python 3.11 or newer
- No runtime dependencies (optional dev tooling: `uv`, `ruff`, `mypy`, `pytest`)

### 🔧 Installation

````bash
pip install flunt
````

### 🔔 Notifiable

````python
from flunt.notifications.notifiable import Notifiable

class Name(Notifiable):
    def __init__(self, name):
        super().__init__()

        if len(name) < 3:
            self.add_notification(
                field='name', message='Name must have at least 3 characters'
            )
        self._name = name
````

### 📜 Contract
````python
"""Module Value Objects."""
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Name(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name, last_name):
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.add_notifications(
            Contract()
            .requires(self.first_name, 'first name', 'First name is required')
            .requires(self.last_name, 'last name', 'Last name is required')
            .is_greater_than(
                value=self.first_name,
                comparer=3,
                field="first_name",
                message="Minimum of 3 characters",
            )
            .is_greater_than(
                value=self.last_name,
                comparer=3,
                field="last_name",
                message="Minimum of 3 characters",
            )
            .get_notifications()
        )


nome = Name('Emerson', 'Delatorre')
if not nome.is_valid:
    for notification in nome.get_notifications():
        print(notification)

````
## Contributing

Please refer to our DevGuide at the following link: [CONTRIBUTING](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CONTRIBUTING_EN.md)

## 📚 Documentation

- Site (MkDocs): https://fazedordecodigo.github.io/PyFlunt/
- Local files: `docs/`

## Changelog

Please refer to our changelog at the following link: [CHANGELOG](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CHANGELOG_EN.md)

## 📄 License

This project contains the MIT license. See the file [LICENSE](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/LICENSE.md).

## Mods
* [Flunt for C# (Original)](https://github.com/andrebaltieri/Flunt)
* [Flunt.Br](https://github.com/lira92/flunt.br)
* [Flunt for Java](https://github.com/carlosbritojun/jflunt)
* [Flunt for JavaScript](https://github.com/jhonesgoncal/flunt)
* [Flunt for PHP](https://github.com/matheusbloise/flunt-php)
