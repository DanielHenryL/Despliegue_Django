from django.contrib import messages
from .models import NewsletterUser
from django.shortcuts import render
from .forms import NewsletterUserSignUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.views.generic import View

# Create your views here.
class HomeView(View):
    def get(self, request, *args,**kwargs):
        context = {

        }
        return render(request, 'index.html',context)

    def post(self, request, *args,**kwargs):
        form=NewsletterUserSignUpForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsletterUser.objects.filter(email=instance.email).exists():
                messages.warning(request, 'El email ya existe')
            else:
                instance.save()
                messages.success(request, 'Hemos enviado un correo elctronico, revisa tu correo')
                #correo elctronico
                subject = 'libro de cocina'
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                html_template = 'newsletters/email_templates/welcome.html'
                html_message = render_to_string(html_template)
                message = EmailMessage(subject,html_message,from_email,to_email)

                #para mandar mensaje se usa conmo html por es mas rapido
                message.content_subtype = 'html'
                message.send()
        context ={
            'form':form
        }
        
        return render(request, 'index.html',context)


def newsletter_unsubscribe(request):
    form=NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'El email fue Eliminado')
        else:
            messages.warning(request, 'El email no funciona')
    context = {
        'form':form
    }
    return render(request,'unsubscribe.html',context)
