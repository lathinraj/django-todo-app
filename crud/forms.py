from django import forms

class TodoForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    description=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}))