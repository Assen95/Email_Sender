from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from Email_Sender.demoapp.forms import EmailForm


def send_email(request):
    if request.method == 'GET':
        email_form = EmailForm()
    else:
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            # We used the "cleaned_data" to convert the data to Python types after the form is validated
            subject = email_form.cleaned_data["subject"]
            message = email_form.cleaned_data["content"]
            sender = settings.EMAIL_HOST_USER
            recipient = email_form.cleaned_data["to_email"]

            send_mail(subject, message, sender, [recipient])
            email_form.save()
            return redirect('send_email')

    context = {
        "email_form": email_form
    }

    return render(request, "email.html", context)


#
    # context = {
    #     "title": "Send an email"
    # }
    #
    # if request.method == "POST":
    #     subject = request.POST.get("subject")
    #     to = request.POST.get("toemail")
    #     content = request.POST.get("content")
    #     # from start to finish: "subject", "message", "from email", "recipient list".
    #     send_mail(subject, content, settings.EMAIL_HOST_USER, [to])
    #
    #     return render(request, "email.html", context)
    # else:
    #     return render(request, "email.html", context)