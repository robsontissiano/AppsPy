# encoding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
import os
import urllib
from invoice.forms import ClientForm, InvoiceItemForm, InvoiceFormSet, \
    ServiceForm
from invoice.models import Client, Invoice, Item, Service

from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.encoding import force_unicode


def pdf(request, invoice_id):

    # htmlfile = 'https://nf.azion.com/invoice/detail/' + str(invoice_id)
    # pdffile = '/usr/local/azion/azion-nf/static/pdf/invoice.pdf'
    # cmd = '/usr/local/azion/azion-nf/phantomjs/bin/phantomjs \
    # /usr/local/azion/azion-nf/phantomjs/examples/rasterize.js \
    # %s %s %s'

    """
    htmlfile = 'http://127.0.0.1:8080/invoice/detail/' + str(invoice_id)
    pdffile = '/home/hobbit/azion-nf/static/pdf/invoice.pdf'
    cmd = '/home/hobbit/azion-nf/phantomjs/bin/phantomjs \
    /home/hobbit/azion-nf/phantomjs/examples/rasterize.js \
    %s %s %s'
    """

    htmlfile = 'http://127.0.0.1:9090/invoice/detail/' + str(invoice_id)
    pdffile = '/home/reweb/Projects/Robson_Projects/azion-nf/static/pdf/invoice.pdf'
    cmd = '/home/reweb/Projects/Robson_Projects/azion-nf/phantomjs/bin/phantomjs \
    /home/reweb/Projects/Robson_Projects/azion-nf/phantomjs/examples/rasterize.js \
    %s %s %s'


    # htmlfile = 'https://nf.azion.com/invoice/detail/' + str(invoice_id)
    # pdffile = '/usr/local/azion/azion-nf/static/pdf/invoice_' + str( 
    #     invoice_id) + '.pdf'
    # cmd = '/usr/local/azion/azion-nf/phantomjs/bin/phantomjs \
    # /usr/local/azion/azion-nf/phantomjs/examples/rasterize.js \
    # %s %s %s'

    # htmlfile = 'http://192.168.50.226:8080/invoice/detail/' + str(invoice_id)
    # pdffile = '/vagrant/static/pdf/invoice_' + str(
    #     invoice_id) + '.pdf'

    # cmd = '/vagrant/phantomjs/bin/phantomjs \
    # /vagrant/phantomjs/examples/rasterize.js \
    # %s %s %s'

    document_size = 'A4'
    os.system(cmd % (htmlfile, pdffile, document_size))

    f = urllib.urlopen(pdffile)
    data = f.read()
    f.close()
    return HttpResponse(data, content_type='application/pdf')


def invoice_detail(request, invoice_id, template_name='invoice_detail.html'):
    invoice = Invoice.objects.get(pk=invoice_id)
    items = Item.objects.filter(invoice=invoice)
    client = invoice.client
    emission_date = invoice.emission_date
    invoice_total_value = 0
    precision = 2

    for item in items:

        invoice_total_value += item.value
        item.value = floatformat(item.value, precision)
        item.value, decimal = force_unicode(item.value).split('.')
        item.value = intcomma(item.value)
        item.value = item.value.replace(',', '.') + ',' + decimal

    invoice_total_value = floatformat(invoice_total_value, precision)
    invoice_total_value, decimal = force_unicode(invoice_total_value)\
        .split('.')
    invoice_total_value = intcomma(invoice_total_value)
    invoice_total_value = invoice_total_value.replace(',', '.') + ',' + decimal

    context = {
        'invoice_total_value': invoice_total_value,
        'invoice': invoice,
        'items': items,
        'client': client,
        'emission_date': emission_date,
    }
    return render(request, template_name, context)


def index(request):
    client = Client.objects.all().order_by('client')
    service = Service.objects.all()
    context = {
        'client': client,
        'services': service,
    }
    return render(request, 'index.html', context)


def client_add(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com successo.')
            return HttpResponseRedirect(reverse('client_list'), request)

    return render(request, 'client_add.html', {'form': form})


def service_add(request):
    form = ServiceForm()
    messages.set_level(request, messages.DEBUG)

    if request.method == 'POST':

        form = ServiceForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Serviço cadastrado com successo.')
            return HttpResponseRedirect(reverse('service_list'), request)

    return render(request, 'service_add.html', {'form': form})


def invoice_add(request, client_id):

    client = Client.objects.get(pk=client_id)
    emission_date = datetime.datetime.now()

    form = InvoiceItemForm()
    invoice = form.save(commit=False)

    if request.method == 'POST':
        formset = InvoiceFormSet(
            request.POST,
            instance=invoice,
            minimum_forms=1,
        )
        print request.POST

        if formset.is_valid():

            invoice.client = client
            invoice.save()
            formset.save()
            messages.success(request, 'Nota Fiscal cadastrada com successo.')
            return HttpResponseRedirect(reverse('index'), request)
    else:
        formset = InvoiceFormSet()

    context = {
        'emission_date': emission_date,
        'client': client,
        'formset': formset,
    }

    return render(request, 'invoice.html', context)


def client_edit(request, client_id, template_name='client_edit.html'):
    client = Client.objects.get(pk=client_id)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado atualizado com successo.')
            return HttpResponseRedirect(reverse('client_list'))

    return render(request, template_name, {'client': client, 'form': form})


def invoice_edit(request, invoice_id, template_name='invoice.html'):
    invoice = Invoice.objects.get(pk=invoice_id)
    items = Item.objects.filter(invoice=invoice)

    invoice_total_value = 0

    for item in items:
        invoice_total_value += item.value

    if request.method == 'POST':
        formset = InvoiceFormSet(request.POST, instance=invoice)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Nota Fiscal cadastrada com successo.')
            return HttpResponseRedirect(reverse('index'))
    else:
        formset = InvoiceFormSet(instance=invoice)
    context = {
        'emission_date': invoice.emission_date,
        'client': invoice.client,
        'formset': formset,
    }

    return render(request, 'invoice.html', context)


def service_edit(request, service_id):
    service = Service.objects.get(pk=service_id)
    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('service_list'))

    return render(request, 'service_edit.html', {'service': service,
                                                 'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def invoice_list(request, client_id):
    invoice = Invoice.objects.filter(client_id=client_id)
    return render(request, 'invoice_list.html', {'invoices': invoice})


def service_list(request,):
    service = Service.objects.all()
    return render(request, 'service_list.html', {'services': service})


def service_delete(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Serviço removido!')
        return HttpResponseRedirect(reverse('service_list'))

    return render(request, 'service_delete.html', {'service': service})


def client_delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Cliente removido!')
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'client_delete.html', {'client': client})
