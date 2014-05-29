


## myblog/forms.py
from django import forms
 
class PostForm(forms.Form):
    content = forms.CharField(max_length=256)
    created_at = forms.DateTimeField()


## views.py
from myblog.forms import PostForm
 
def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.Post.objects.create(content=content,
                                         created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
 
    return render(request, 'post/post_form_upload.html', {
        'form': form,
    })


# myblog/templates/post_form_upload.html.    

<form action='/post/form_upload.html' method='post'>{% csrf_token %}
{{ form.as_p }}
<input type='submit' value='Submit' />
</form>

## myblog/urls.py
urlpatterns = patterns('',
    ...
    url(r'^post/form_upload.html$',
        'myblog.views.post_form_upload', name='post_form_upload'),
    ...
)