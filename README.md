# 🐍 PyFlunt: Python implementation of Domain Notification Pattern

Python implementation of Domain Notification Pattern based in [Flunt](https://github.com/andrebaltieri/flunt) (.NET) developed by @andrebaltieri

[![PyPI Latest Release](https://img.shields.io/pypi/v/flunt.svg)](https://pypi.org/project/flunt/)
[![Downloads](https://pepy.tech/badge/flunt)](https://pepy.tech/project/flunt)
[![Linters](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/linters.yml/badge.svg)](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/linters.yml)
[![Realease](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/realease.yml/badge.svg)](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/realease.yml)
[![Publish](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/publish.yml/badge.svg)](https://github.com/fazedordecodigo/PyFlunt/actions/workflows/publish.yml)

Flunt is a way to implement a notification pattern in your application to centralize errors and changes in certain actions and entities.

Flunt was born out of two needs: implementing the Domain Notification Pattern to replace domain-level exceptions in the application and reducing the amount of IFs (complexity) by using a contract-based approach.

Thus, basically what Flunt does is add a list of Notifications to your class and various methods to interact with it.

## 🐍 Python Version

- [Python 3.10](https://www.python.org/)

## ➡️ How to use

### 🔧 Installation

````bash
pip install flunt
````

### 🔔 Notifiable

````python
from flunt.notifiable import Notifiable
from flunt.notification import Notification

class Name(Notifiable):
    def __init__(self, name):
        super().__init__()
        
        if len(name) > 3:
            self.add_notification(
                Notification(field='name', message='invalid name')
            )

        self._name = name
````

### 📜 Contract
````python
"""Module Value Objects."""
from flunt.notifiable import Notifiable
from flunt.contract import Contract


class Name(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name, last_name):
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.add_notifications(
            Contract()
            .requires(self.first_name, 'first name')
            .requires(self.last_name, 'last name')
            .is_greater_than(
                value=self.first_name,
                comparer=3,
                key="first_name",
                message="Mínimo de 3 caracteres",
            )
            .is_greater_than(
                value=self.last_name,
                comparer=3,
                key="last_name",
                message="Mínimo de 3 caracteres",
            )
            .get_notifications()
        )


nome = Name('Emerson', 'Delatorre')
if not nome.is_valid():
    for notification in nome.get_notifications():
        print(notification)

````

## 📄 License

This project contains the MIT license. See the file [LICENSE](LICENSE).

## Mods
* [Flunt for C# (Original)](https://github.com/andrebaltieri/Flunt)
* [Flunt.Br](https://github.com/lira92/flunt.br)
* [Flunt for Java](https://github.com/carlosbritojun/jflunt)
* [Flunt for JavaScript](https://github.com/jhonesgoncal/flunt)
* [Flunt for PHP](https://github.com/matheusbloise/flunt-php)