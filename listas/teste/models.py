# Create your models here.
from django.db import models
from djangotoolbox.fields import ListField
from .forms import StringListField


from django.db import models
from django import forms

class StringListField(models.Field):
    u'''
    Save a list of strings in a CharField (or TextField) column.

    In the django model object the column is a list of strings.
    '''
    __metaclass__=models.SubfieldBase
    SPLIT_CHAR=u'\v'
    def __init__(self, *args, **kwargs):
        self.internal_type=kwargs.pop('internal_type', 'CharField') # or TextField
        super(StringListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return value.split(self.SPLIT_CHAR)

    def get_internal_type(self):
        return self.internal_type

    def get_db_prep_lookup(self, lookup_type, value):
        # SQL WHERE
        raise NotImplementedError()

    def get_db_prep_save(self, value):
        return self.SPLIT_CHAR.join(value)

    def formfield(self, **kwargs):
        assert not kwargs, kwargs
        return forms.MultipleChoiceField(choices=self.choices)



class CategoryField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    categories = CategoryField()
    ignorelist = models.StringListField(default=0, blank=True, null=True)


class Project(models.Model):

    name = models.CharField(max_length=150, unique=True)
    repository = models.CharField(max_length=150, unique=True)

    #ftp_homolog_host = models.CharField(max_length=150, blank=True)
    #ftp_homolog_user = models.CharField(max_length=50, blank=True)
    #ftp_homolog_pass = models.CharField(max_length=50, blank=True)
    #ftp_homolog_root = models.CharField(max_length=100, blank=True)
    homolog_version = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    #homolog_update = models.IntegerField(default=0)
    homolog_url = models.CharField(max_length=250, blank=True)
    #homologation_update = models.DateTimeField(auto_now_add=True, blank=True)

    ftp_production_host = models.CharField(max_length=150, blank=True) #host ftp
    ftp_production_user = models.CharField(max_length=50, blank=True) # usuario ftp
    ftp_production_pass = models.CharField(max_length=50, blank=True) # senha
    ftp_production_root = models.CharField(max_length=100, blank=True) # raiz de arquivpos
    
    production_version = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    #production_update = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.name    

