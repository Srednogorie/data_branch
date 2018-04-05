from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'myFormFieldsClass', 'type': 'email',
               'data-parsley-error-message': 'Please enter valid email.'}))
    subject = forms.CharField(required=True, min_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'class': 'myFormFieldsClass',
               'data-parsley-error-message': 'Too short. 10 characters or more please.'}))
    message = forms.CharField(required=True, min_length=10, widget=forms.Textarea(
        attrs={'placeholder': 'Your message...', 'class': 'myFormFieldsClass',
               'data-parsley-error-message': 'Too short. 50 characters or more please.', 'rows':10}))
