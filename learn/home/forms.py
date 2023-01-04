from django import forms
from .models import Todo

# By default, all form values are required
#By default, it makes the name of the field a label, which we can change

class TodoCreateForm(forms.Form):
    title = forms.CharField(label='onvan')
    body = forms.CharField(required=False)
    create = forms.DateTimeField()

# in ravesh be shorat mostaghim model ro be form tabdil mikone
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'create')
        # agar hame fild haro khasi mitoni begi fields='__all__'

