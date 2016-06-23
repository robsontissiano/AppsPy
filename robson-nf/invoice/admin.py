from django.contrib import admin
from . models import Client, Invoice, Item, Retention, Service


class ItemInline(admin.TabularInline):
    model = Item
    extra = 4


class ClientInline(admin.TabularInline):
    model = Client
    exclude = ['email']


class RetentionInline(admin.TabularInline):
    model = Retention
    extra = 4


class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    fields = ['client']
    list_display = ("emission_date", "client")
    inlines = [ItemInline, RetentionInline]

admin.site.register(Client)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Retention)
admin.site.register(Service)
