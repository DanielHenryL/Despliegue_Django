from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
# class HomeView(View):
#     def get(self, request, *args,**kwargs):
#         context = {

#         }
#         return render(request, 'index.html',context)

class AboutView(View):
    def get(self, request, *args,**kwargs):
        context = {

        }
        return render(request, 'about.html',context)

class ContactView(View):
    def get(self, request, *args,**kwargs):
        context = {

        }
        return render(request, 'contact.html',context)
    def post(self, request, *args,**kwargs):
        message_name = request.POST['full_name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['lagunasdaniel001gmail.com']
        )
        messages.success(request, 'Mensaje enviado con exito')
        context = {
            
        }
        return render(request, 'contact.html',context)