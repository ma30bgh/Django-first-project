from django import forms


# By default, all form values are required
#By default, it makes the name of the field a label, which we can change

class TodoCreateForm(forms.Form):
    title = forms.CharField(label='onvan')
    body = forms.CharField(required=False)
    create = forms.DateTimeField()
