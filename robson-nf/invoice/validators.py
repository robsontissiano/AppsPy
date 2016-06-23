# encoding: utf-8

from django.core.validators import RegexValidator


cnpj_validator = RegexValidator(
    regex='^[^a-zA-Z]*$',
    message='O CNPJ informado deve ser numérico.',
    code='invalid_cnpj'
)

code_validator = RegexValidator(
    regex='^[a-zA-Z0-9]*$',
    message='O ID do cliente deve ser Alpha-numérico.',
    code='invalid_code'
)


phone_validator = RegexValidator(
    regex='^[^a-zA-Z]*$',
    message='O Telefone deve ser numérico.',
    code='invalid_phone'
)


value_number_validator = RegexValidator(
    regex='^[0-9]*$',
    message='O Valor deve ser numérico.',
    code='invalid_value'
)

value_negative_validator = RegexValidator(
    regex='^\+?0|[1-9][0-9]*$',
    message='O Valor não deve ser negativo.',
    code='invalid_value'
)
