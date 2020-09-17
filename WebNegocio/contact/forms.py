from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Tu nombre:', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juanito'}), min_length=3, max_length=100)
    email = forms.EmailField(label='Tu e-mail:', required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'correo@ejemplo.com'}))
    content = forms.CharField(label='Mensaje:', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe aquí tu mensaje'}), min_length=10, max_length=1000)