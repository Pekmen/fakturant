
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Company, Invoice

def index(request):
    invoices = Invoice.objects.all().order_by('date_created')
    context = {'invoices' : invoices}

    return render(request, 'fakturant/index.html', context)

def show_company(request, company_short_name):
    company = get_object_or_404(Company, company_short_name=company_short_name)
    context = {'company' : company}
    return render(request, 'fakturant/company.html', context)

def show_invoice(request, invoice_id):
    single_invoice = get_object_or_404(Invoice, invoice_id = invoice_id)
    context = {'single_invoice' : single_invoice}
    return render(request, 'fakturant/invoice.html', context)