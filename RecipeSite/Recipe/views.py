from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from Recipe.models import Recipe, RecipeIngredient
from Recipe.forms import UserSubmittedRecipeForm, IngredientFormSet

def index(request):
    if request.POST:

        form = UserSubmittedRecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            ingredient_formset = IngredientFormSet(request.POST, instance=recipe)

            if ingredient_formset.is_valid():
                recipe.save()
                ingredient_formset.save()    

                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserSubmittedRecipeForm()
        ingredient_formset = IngredientFormSet(instance=Recipe())
        
    return render_to_response("submit.html", {
        "form": form,
        "ingredient_formset": ingredient_formset,
    }, context_instance=RequestContext(request))
