from django.shortcuts import render, redirect
# Create your views here.
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.template import loader
from django.urls import reverse
from .models import Member, Socios, MisDatos, MisCursos
from datetime import datetime
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@requires_csrf_token
def addsocio(request):
  dato = " " 
  template = loader.get_template('addsocio.html')
  context = {
    'myfecha': dato,
  }
  return HttpResponse(template.render(context, request))
  
def members(request):
    # ver1 return HttpResponse("Hello world!")
    mymembers = Member.objects.all().values()
    fecha_actual = datetime.now()
    fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        'myfecha': fecha_actual_str,
    }
    # ver1 return HttpResponse(template.render())
    return HttpResponse(template.render(context, request))
    
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@csrf_exempt  
def main(request):
  fecha_actual = datetime.now()
  fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
  aviso = request.GET.get('aviso', 'false')
  textomensaje = request.GET.get('textomensaje', ' ')
  template = loader.get_template('main.html')
  context = {
    'myfecha': fecha_actual_str,
    'esvisible': aviso,
    'textoMensaje': textomensaje,
  }
  return HttpResponse(template.render(context, request))

@csrf_exempt 
def testing(request):
  template = loader.get_template('pruebacorreos.html')
  return HttpResponse(template.render())
  
def enviar(request):
    subject = 'Alta de socio CAMARASAL'
    message = 'Gracias por registrar tu empresa en CFEVirtual. Si ves este correo es satisfactoriamente'
    #from_email = 'coordinacion.virtual@camarasal.com'
    from_email = 'virtual.camarasal@gmail.com'
    to_email = request.POST['email']
    try:
        #html_content = render_to_string('plantillaCorreo.html', {'subject': subject, 'myusuario': myusuario, 'mypass': mypass})
        #text_content = strip_tags(html_content)
        #msg = EmailMultiAlternatives(subject, text_content, from_email, [to_emaill])
        #msg.attach_alternative(html_content, "text/html")
        #msg.send()
        send_mail(subject, message, from_email, [to_email])
    except BadHeaderError:
        return HttpResponse("Invalido!!!!!, no se encontro la cabecera")
    #return HttpResponseRedirect(reverse('success'))
    #return redirect('success', mycorreo=w)
    url = reverse('success') + f'?mycorreo={to_email}'
    return HttpResponseRedirect(url)

def addrecord(request):
    z = request.POST['cfe-empresa']
    u = request.POST['cfe-codigo']
    buscar_empresa = MisDatos.objects.filter(empresa=z,codigo=u).values()  #existe el codigo de la empresa socia
    buscar_empresa_1 = MisDatos.objects.get(empresa=z, codigo=u)
    if buscar_empresa.exists():
        if buscar_empresa.values()[0]["registrado"]=="no":  #¿pregunta si ya se registro alguien con esta empresa?
            myusuario = buscar_empresa.values()[0]["usuario"]
            mypass = buscar_empresa.values()[0]["password"]
            to_emaill = request.POST['cfe-mail']
            
            buscar_empresa_1.nombre = request.POST['cfe-nombre']
            buscar_empresa_1.cargo = request.POST['cfe-cargo']
            buscar_empresa_1.email = request.POST['cfe-mail']
            buscar_empresa_1.telefono = request.POST['cfe-tel']
            fecha_actual = datetime.now()
            fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
            buscar_empresa_1.fecha = fecha_actual_str
            buscar_empresa_1.registrado = "si"
            buscar_empresa_1.save()
            
            subject = 'Alta de socio CAMARASAL'
            #message = 'Gracias por registrar tu empresa en CFEVirtual. Se ha creado el usuario de socio de la Camara de comercio e industria de El Salvador satisfactoriamente. Los datos de ingreso son:'
            from_email = 'virtual.camarasal@gmail.com'
            try:
                html_content = render_to_string('plantillaCorreo.html', {'subject': subject, 'myusuario': myusuario, 'mypass': mypass})
                text_content = strip_tags(html_content)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to_emaill])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                #send_mail(subject, message, from_email, [to_emaill])
            except BadHeaderError:
                return HttpResponse("Invalido, no se encontro la cabecera")
            #return HttpResponseRedirect(reverse('success'))
            #return redirect('success', mycorreo=w)
            url = reverse('success') + f'?mycorreo={to_emaill}'
            return HttpResponseRedirect(url)
        else:
            aviso = "true"
            textomensaje = "La empresa ya está registrada, por favor contacte a RRHH o representante de su empresa, para solicitar la inscripción al curso de su preferencia. Tambien puede gestionar la inscripción a nuestro correo: coordinacion.virtual@camarasal.com"
            return redirect(reverse('main') + f'?aviso={aviso}&textomensaje={textomensaje}')        
    else:
        aviso = "true"
        textomensaje = "El numero de código o nombre de la empresa, no coincide con los socios afiliados. El código no existe, favor verifique haber ingresado los datos correctos"
        return redirect(reverse('main') + f'?aviso={aviso}&textomensaje={textomensaje}')
    
def success(request):
    mycorreo = request.GET.get('mycorreo', '')
    context = {'mycorreo': mycorreo}
    template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    #return render(request, 'myfirst.html', context)
    return HttpResponse(template.render(context, request))

def allsocios(request):
    mydatos = MisDatos.objects.all().values()
    template = loader.get_template('all_socios.html')
    context = {
        'mysocios': mydatos,
    }
    return HttpResponse(template.render(context, request))
    
def editar(request, id):
  mysocio = Socios.objects.get(id=id)
  template = loader.get_template('editar.html')
  context = {
    'mysocios': mysocio,
  }
  return HttpResponse(template.render(context, request))
     
def guardarsocio(request):
    p_filial = request.POST['cfe-filial']
    p_codigo = request.POST['cfe-codigo']
    p_razon_social= request.POST['cfe-razon-social']
    p_persona_natural = request.POST['cfe-persona-natural']
    p_usuario = request.POST['cfe-usuario']
    p_password = request.POST['cfe-password']
    
    #cargo, codigo, email, fecha, filial, nombre, empresa, registrado, socio, telefono,trabaja, usuario, password
    
    mydatos = MisDatos(
        filial = p_filial,
        codigo = p_codigo,
        empresa = p_razon_social,
        nombre = p_persona_natural,
        usuario = p_usuario,
        password = p_password,
        socio = "si",
        trabaja = "si",
        registrado = "no"
    )
    mydatos.save()
    return HttpResponseRedirect(reverse('exito'))

def exito(request):
    template = loader.get_template('sociosuccess.html')
    return HttpResponse(template.render())
    
 # ------------------------------------------------AQUI EMPIEZA EL BLOQUE DE REGISTROS------------------------------
def afiliar(request):
    fecha_actual = datetime.now()
    fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
    template = loader.get_template('registro/afiliar.html')
    context = {
        'myfecha': fecha_actual_str,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt      
def identificacion(request):
    aviso = request.GET.get('aviso', 'false')
    textomensaje = request.GET.get('textomensaje', ' ')
    id_curso = request.GET.get('id', ' ')
    encontrar_curso = MisCursos.objects.filter(numeral_curso=id_curso).values()
    if encontrar_curso.exists():
        name_curso = encontrar_curso[0]['nombre_curso']
        url_curso = encontrar_curso[0]['url_curso']
        url_producto = encontrar_curso[0]['url_producto']
    else:
       name_curso, url_curso, url_producto = '','',''
    template = loader.get_template('registro/identificacion.html')
    context = {
        'esvisible': aviso,
        'textoMensaje': textomensaje,
        'id_curso': id_curso,
        'name_curso': name_curso,
        'url_curso': url_curso,
        'url_producto': url_producto
    }
    return HttpResponse(template.render(context, request))

def acceso(request):
    cfe_correo = request.POST['cfe-mail']
    cfe_codigo = request.POST['cfe-codigo']
    cfe_producto = request.POST['cfe-producto']
    encontrar_empresa = MisDatos.objects.filter(email=cfe_correo,codigo=cfe_codigo).values()
    if encontrar_empresa.exists():
        return HttpResponseRedirect(cfe_producto)
    else:
        aviso = "true"
        textomensaje = "El correo no esta registrado o no se ingreso el codigo de socio correctamente"
        cfe_id = request.POST['cfe-id']
        return redirect(reverse('identificacion') + f'?aviso={aviso}&textomensaje={textomensaje}&id={cfe_id}')        
    
def inscripcion(request):
    fecha_actual = datetime.now()
    fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
    template = loader.get_template('registro/inscripcion.html')
    context = {
        'myfecha': fecha_actual_str,
    }
    return HttpResponse(template.render(context, request))
    
@csrf_exempt  
def socio(request):
    aviso = request.GET.get('aviso', 'false')
    textomensaje = request.GET.get('textomensaje', ' ')
    template = loader.get_template('registro/socio.html')
    context = {
        'esvisible': aviso,
        'textoMensaje': textomensaje,
        }
    return HttpResponse(template.render(context, request))  

def guardar(request):
    cfe_empresa = request.POST['cfe-empresa']
    cfe_codigo = request.POST['cfe-codigo']
    encontrar_empresa = MisDatos.objects.filter(empresa=cfe_empresa,codigo=cfe_codigo).values()  #existe el codigo de la empresa socia
    if encontrar_empresa.exists():
        datos_empresa = MisDatos.objects.get(empresa=cfe_empresa, codigo=cfe_codigo)
        if datos_empresa.registrado=="no":  #¿pregunta si ya se registro alguien con esta empresa?
            myusuario = datos_empresa.usuario
            mypass = datos_empresa.password
            to_emaill = request.POST['cfe-mail']
            
            datos_empresa.nombre = request.POST['cfe-nombre']
            datos_empresa.cargo = request.POST['cfe-cargo']
            datos_empresa.email = request.POST['cfe-mail']
            datos_empresa.telefono = request.POST['cfe-tel']
            fecha_actual = datetime.now()
            fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
            datos_empresa.fecha = fecha_actual_str
            datos_empresa.registrado = "si"
            datos_empresa.save()
            
            subject = 'Alta de socio CAMARASAL'
            #message = 'Gracias por registrar tu empresa en CFEVirtual. Se ha creado el usuario de socio de la Camara de comercio e industria de El Salvador satisfactoriamente. Los datos de ingreso son:'
            from_email = 'virtual.camarasal@gmail.com'
            try:
                html_content = render_to_string('plantillaCorreo.html', {'subject': subject, 'myusuario': myusuario, 'mypass': mypass})
                text_content = strip_tags(html_content)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to_emaill])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                #send_mail(subject, message, from_email, [to_emaill])
            except BadHeaderError:
                return HttpResponse("Invalido!!!!!, no se encontro la cabecera")
            #return HttpResponseRedirect(reverse('success'))
            #return redirect('success', mycorreo=w)
            url = reverse('success') + f'?mycorreo={to_emaill}'
            return HttpResponseRedirect(url)
        else:
            aviso = "true"
            textomensaje = "La empresa ya está registrada, por favor contacte a RRHH o representante de su empresa, para solicitar la inscripción al curso de su preferencia. Tambien puede gestionar la inscripción a nuestro correo: coordinacion.virtual@camarasal.com"
            return redirect(reverse('socio') + f'?aviso={aviso}&textomensaje={textomensaje}')        
    else:
        aviso = "true"
        textomensaje = "El numero de código o nombre de la empresa, no coincide con los socios afiliados. El código no existe, favor verifique haber ingresado los datos correctos"
        return redirect(reverse('socio') + f'?aviso={aviso}&textomensaje={textomensaje}')
  
def usuario(request):
    fecha_actual = datetime.now()
    fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
    template = loader.get_template('registro/usuario.html')
    context = {
        'myfecha': fecha_actual_str,
    }
    return HttpResponse(template.render(context, request))
