from django import forms
from django_summernote.widgets import SummernoteWidget

from Email_Sender.demoapp.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        widgets = {"content": SummernoteWidget()}
