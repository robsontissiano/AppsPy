from django import forms

class StringListField(forms.CharField):
    def prepare_value(self, value):
        return ', '.join(value)

    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]


class ProjectForm(forms.ModelForm):

    def clean_homolog_version(self):
        version_homolog = self.cleaned_data.get('homolog_version')
        if version_homolog is None:
            return self.fields['homolog_version'].initial
        else:
            return version_homolog

    def clean_production_version(self):
        version_production = self.cleaned_data.get('production_version')
        if version_production is None:
            return self.fields['production_version'].initial
        else:
            return version_production

    class Meta:
        model = Project        