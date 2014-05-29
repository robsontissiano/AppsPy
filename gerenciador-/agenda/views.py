from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from models import ItemAgenda
from forms import FormItemAgenda
from django.http import Http404

def index(request):
	return HttpResponse("Ola mundo!")


def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html",{'lista_itens': lista_itens})

def adiciona(request):
	if request.method == 'POST':
		form = FormItemAgenda(request.POST, request.FILES)
		if form.is_valid():

			dados = form.cleaned_data
			item = ItemAgenda(data=dados['data'],
			#hora = dados['hora'],
			titulo = dados['titulo'],
			descricao = dados['descricao'])
			item.save()

		return render_to_response("salvo.html", {})

	else: 
		form = FormItemAgenda()

		return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

def item(request, nr_item):
	try:
		item = ItemAgenda.objects.get(pk=nr_item)
	except ItemAgenda.DoesNotExist:
		raise Http404()
	return render_to_response('item.html', {'item': item})












from django import newforms as forms
from django.newforms.forms import BoundField
from django.template import Context, loader

class TemplatedForm(forms.form):
	def output_via_template(self):
		bound_fields = [BoundField(self, field, name) for name, field \
						in self.fields.items()]
		c = Context(dict(form = self, bound_fields = bound_fields))
		t = loader.get_template('invoice_register.html')
		return t.render(c)

	def __str__(self):
		return self.output_via_template()


def invoice_register(self):







def __str__(self):
	return self.invoice_register()








































