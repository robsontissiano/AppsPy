from django.contrib import admin
from models import ItemAgenda
# Register your models here.


class ItemInline(admin.TabularInline):
	model = ItemAgenda


admin.site.register(ItemAgenda)