from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FormularioContactos 
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER
from .forms import FormularioContactos



# Create your views here.

def contact(request):    
    if request.method == 'POST':         #en este caso procesaremos el formulario
        form = FormularioContactos(request.POST)#aquí almacenamos los datos del formulario
        if form.is_valid():#comprobamos que los datos del formulario son válidos
            cd = form.cleaned_data
            email = EmailMessage (
                 'Porbando DJango', # Asunto
                 'De {} <{}>\n\nMensaje:\n\n{}'.format(cd['name'], cd['email'], cd['message']), #Cuerpo
                 EMAIL_HOST_USER,# Origen (Mi servidor de correo)
                 ["juan.carrillo@entelgy.com"],#Destinno(Para quien es el correo)
                 reply_to=[cd['email']],#email de respuesta(a quien hay que contestar)
              )
            #AQUÍ INTRODUCIMOS EL ENVÍO DEL MAIL
            try:
                email.send()
                #si todo va ok, redireccionamos a ?ok
                return redirect(reverse('contact')+'?ok')
            except:
                #si algo falla, redireccionamos a ?fail
                return redirect(reverse('contact')+'?FAIL')
    else:
        form = FormularioContactos()
    return render(request, 'contact/contact.html', {'form': form})

