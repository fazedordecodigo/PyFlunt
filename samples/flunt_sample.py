"""Module Value Objects."""

from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Pessoa(Notifiable):
	"""Class Value Object Name."""

	def __init__(self, first_name, last_name, email):
		"""Found 'Constructor'."""
		super().__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

		self.contract = (
			Contract()
			.requires(self.first_name, 'first name', 'Nome é obrigatório')
			.requires(self.last_name, 'last name', 'Sobrenome é obrigatório')
			.requires(self.email, 'e-mail', 'E-mail é obrigatório')
			.is_lower_than(
				value=self.first_name,
				comparer=3,
				key='first_name',
				message='Mínimo de 3 caracteres',
			)
			.is_lower_than(
				value=self.last_name,
				comparer=3,
				key='last_name',
				message='Mínimo de 3 caracteres',
			)
			.is_email(value=self.email, key='email', message='email errado')
		)
		self.add_notifications(self.contract.get_notifications())


def main():
	"""Run the main function."""
	nome = Pessoa('Emerson', 'Delatorre', 'emerson@delatorre.dev')
	if not nome.is_valid:
		for notification in nome.get_notifications():
			print(notification)
	else:
		print('sem notificações')


if __name__ == '__main__':
	main()
