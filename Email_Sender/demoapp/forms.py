from django import forms
from django.forms import MultiWidget
from django_summernote.widgets import SummernoteWidget

from Email_Sender.demoapp.models import Email


class EmailForm(forms.ModelForm):
    # to_email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Recipient"}), label="")
    class Meta:
        model = Email
        fields = "__all__"

        widgets = {
            'content': SummernoteWidget(),
            "to_email": forms.TextInput(attrs={"placeholder": "Recipient..."}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject..."}),
        }

        labels = {
            "content": '',
            "to_email": '',
            "subject": '',
        }
        # widgets = {
        #     "subject": forms.Textarea(attrs={"placeholder": "Subject"}),
        #     "to_email": forms.Textarea(attrs={"placeholder": "Recipient"}),
        #     "content": [SummernoteWidget(), forms.TextInput(attrs={"placeholder": 'Your message...'})],
        # }
