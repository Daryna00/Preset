from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Тема')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)