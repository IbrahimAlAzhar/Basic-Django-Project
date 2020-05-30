from django import forms


class AddForm(forms.Form):
    text1 = forms.IntegerField()
    text2 = forms.IntegerField()
