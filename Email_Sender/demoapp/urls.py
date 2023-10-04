from django.urls import path
from Email_Sender.demoapp.views import send_email

urlpatterns = [
    path("", send_email, name="send_email")
]