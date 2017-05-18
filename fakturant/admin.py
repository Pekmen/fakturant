from django.contrib import admin

from .models import Company, Invoice

class InvoiceAdmin(admin.ModelAdmin):
  fieldsets = [
        (None,  {'fields': ['company',
                            'invoice_type',
                            'invoice_id',
                            'description']}),

        ('Date info', {'fields': ['date_created',
                                  'due_date']}),

        ('Cost info', {'fields': ['unit_cost',
                                  'vat_percent',
                                  'vat',
                                  'total']})
    ]
  list_display = ('invoice_id', 'date_created', 'description')

  search_fields = ['invoice_id']


class CompanyAdmin(admin.ModelAdmin):
  search_fields = ['company_name']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Invoice, InvoiceAdmin)
