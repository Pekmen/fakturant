from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Company(models.Model):
    company_name = models.CharField('company name', max_length=50)
    company_short_name = models.CharField('short name', max_length=10)
    VAT_number = models.CharField('vat number', max_length=9)
    address = models.CharField('address', max_length=50)
    account = models.CharField('current account', max_length=20)

    def __str__(self):
        return self.company_name


class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    invoice_type = models.CharField('type', max_length=2)
    invoice_id = models.CharField('invoice id', max_length=32)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')
    description = models.CharField('description', max_length=50)
    unit_cost = models.DecimalField('unit cost', max_digits=20, decimal_places=2)
    vat_percent = models.IntegerField('VAT%')
    vat = models.DecimalField("VAT", max_digits=20, decimal_places=2)
    total = models.DecimalField('total', max_digits=20, decimal_places=2)

    def __str__(self):
        return self.invoice_id