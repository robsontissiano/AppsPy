from django.db import models
from django.utils.formats import number_format
from . validators import cnpj_validator, code_validator, phone_validator, \
    value_negative_validator


class Client(models.Model):

    code = models.CharField(max_length=255, unique=True, validators=[
        code_validator])
    name = models.CharField(max_length=150, unique=True)
    cnpj = models.CharField(max_length=20, validators=[
        cnpj_validator], unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=21, null=True, blank=True, validators=[
        phone_validator])
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return self.name


class Service(models.Model):

    description = models.CharField(max_length=255, unique=True, null=False, blank=False)

    def __unicode__(self):
        return self.description


class Item(models.Model):

    class Meta:
        unique_together = ('invoice', 'service')

    invoice = models.ForeignKey('Invoice')
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=19, decimal_places=2, validators=[
        value_negative_validator])

    def __unicode__(self):
        return self.value

    @property
    def formated_value(self):
        return u"R$ %s" % number_format(self.value, 2)


class Invoice(models.Model):

    emission_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey('Client')


class Retention(models.Model):

    invoice = models.ForeignKey('Invoice')
    description = models.CharField(max_length=255)
    aliquot = models.SmallIntegerField()
    value = models.DecimalField(max_digits=19, decimal_places=2)
