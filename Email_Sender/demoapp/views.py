from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def send_email(request):

    context = {
        "title": "Send an email"
    }

    if request.method == "POST":
        to = request.POST.get("toemail")
        content = request.POST.get("content")
        # from start to finish: "subject", "message", "from email", "recipient list".
        send_mail("Testing", content, settings.EMAIL_HOST_USER, [to])

        return render(request, "email.html", context)
    else:
        return render(request, "email.html", context)