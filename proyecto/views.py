from .forms import ContactoForm, EntidadFrom, AuditorSupervisorForm, NotificacionForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse,FileResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from herramientas.decorators import entidad_requerida
from io import BytesIO
from proyecto.models import Contacto, AuditorSupervisor, Entidad
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4,landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import *
from reportlab.platypus import Paragraph
import reportlab


#Ingresa nuevos contactos
@login_required
def ContactoPro(request):
    contacto_form = ContactoForm()

    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)

        if contacto_form.is_valid():
            contacto_form.save()
            #Tengo que avisar que tdo fue bien
            return redirect(reverse('contacto')+'?ok')
        else:
            #Tengo que generar un error
             return redirect(reverse('contacto')+'?error')

    return render(request, 'proyecto/contacto.html',{'form':contacto_form})

# Despliega el listado de los contactos
@login_required
def lista_Contacto(request):
    contactos = Contacto.objects.all()
    context = {
        'contactos':contactos
    }
    return render(request, 'proyecto/lista_contactos.html', context)

#busca un contacto y lo despliega
@login_required
def detalle_contacto(request):
    contacto_id = request.GET.get('id')
    contacto = Contacto.objects.get(id=contacto_id)
    context = {
        'contacto': contacto
    }
    return render(request, 'proyecto/detalle_contacto.html', context)

#Imprime en pdf la lista de contactos
@login_required
def imprimir_contactos(request):
    contactos = Contacto.objects.all()
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactos.pdf"'

    buffer = BytesIO()
    # Crea el objeto PDF en formato horizontal (landscape)
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    elements = []

    fecha = datetime.now()
    hoy = fecha.strftime('%d/%m/%y')

    # Header
    elements.append(Paragraph('Audita', getSampleStyleSheet()['Heading1']))
    elements.append(Paragraph('Reporte', getSampleStyleSheet()['Normal']))
    elements.append(Paragraph(hoy, getSampleStyleSheet()['Normal']))
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))

    # Datos de la tabla
    data = []
    data.append(["Nombre", "Movil", "Telefono", "Email", "Cargo", "Empresa"])

    for contacto in contactos:
        this_contact = [contacto.nombre, contacto.movil, contacto.telefono, contacto.email, contacto.cargo, contacto.empresa]
        data.append(this_contact)

    # Configuración de estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Crear la tabla y aplicar el estilo
    tabla = Table(data)
    tabla.setStyle(style)

    # Agregar la tabla al documento
    elements.append(tabla)

    # Construir el PDF
    pdf.build(elements)

    pdfs = buffer.getvalue()
    buffer.close()
    response.write(pdfs)

    return response

# TODAS LAS FUNCIONES RELACIONADAS CON ENTIDAD
#ingresa datos de la entidad a Auditar
def entidad(request):
    entidad_form = EntidadFrom()

    if request.method == 'POST':
        entidad_form = EntidadFrom(data=request.POST)
        if entidad_form.is_valid():
            entidad_form.save()
            #Tengo que avisar que todo salio bien
            return redirect(reverse('entidad')+'?ok')
        else:
            #se genera un error
            return redirect(reverse('entidad')+'?error')
    return render(request, 'proyecto/entidad.html',{'form':entidad_form})

# Muestra la lista de entidades creadas
def entidad_list(request):
    entidades = Entidad.objects.all()
    return render(request, 'proyecto/entidad_list.html',{'entidades': entidades})

def entidad_detail(request, pk):
    entidad = get_object_or_404(Entidad,pk=pk)
    return render(request, 'proyecto/entidad_detail.html', {'entidad': entidad})

def entidad_new(request):
    if request.method == "POST":
        form = EntidadFrom(request.POST)
        if form.is_valid():
            entidad = form.save()
            return redirect('entidad_detail', pk=entidad.pk)
    else:
        form = EntidadFrom()
    return render(request, 'proyecto/entidad_edit.html', {'form': form})

# edita la entidad seleccionada
def entidad_edit(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk)
    if request.method == "POST":
        form = EntidadFrom(request.POST, instance=entidad)
        if form.is_valid():
            entidad = form.save()
            return redirect('entidad_list')
    else:
        form = EntidadFrom(instance=entidad)
    return render(request, 'proyecto/entidad_edit.html', {'form': form})

def entidad_delete(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk)
    entidad.delete()
    return redirect('entidad_list')

# genera el reporte en pdf de la entidad seleccionada
@login_required
def entidad_pdf(request, pk):
    # Obtiene la entidad por su pk
    entidad = get_object_or_404(Entidad,pk=pk)

    # Crea un objeto HttpResponse y define el tipo de contenido a pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="entidad_{entidad.nombre}.pdf"'

    # Crea un objeto BytesIO para guardar el PDF
    buffer = BytesIO()

    # Crea un objeto Canvas y dibuja en él
    p = canvas.Canvas(response, pagesize=A4)

    fecha = datetime.now()
    hoy = fecha.strftime('%d/%m/%y')

    # Header
    p.setLineWidth(.3)
    p.setFont('Helvetica', 22)
    p.drawString(30,750,'Audita')

    p.setFont('Helvetica',12)
    p.drawString(30,735,'Reporte')

    p.setFont('Helvetica-Bold',12)
    p.drawString(480,750, hoy)
    p.line(460,747,560,747)

    p.setFont('Helvetica',12)

    # Aquí puedes dibujar lo que quieras en el PDF. Este es solo un ejemplo.
    
    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 700, "Nombre: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 700, f"{entidad.nombre}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 685, "Direccion: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 685, f"{entidad.direccion}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 670, "Ciudad: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 670, f"{entidad.ciudad}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 655, "Pais: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 655, f"{entidad.pais}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 640, "Nit: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 640, f"{entidad.nit}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 625, "Seguro Social: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 625, f"{entidad.seguroSocial}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 610, "Representante: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 610, f"{entidad.representante}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 595, "Contacto: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 595, f"{entidad.contacto}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 580, "Email: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 580, f"{entidad.email}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 565, "Telefono: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 565, f"{entidad.telefono}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 550, "WhatSapp: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 550, f"{entidad.whatsapp}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 535, "Sitio Web: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 535, f"{entidad.sitio}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 520, "Actividad Economica: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 520, f"{entidad.actividadE}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 505, "Actividad de Servicio: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 505, f"{entidad.actividadS}")

    p.setFont('Helvetica-Bold',12)
    p.drawString(30, 490, "Norma Contable: ")
    p.setFont('Helvetica',12)
    p.drawString(175, 490, f"{entidad.norma}")
  
    # Cierra el objeto PDF
    p.showPage()
    p.save()

    return response

@login_required
@entidad_requerida
def AuditorSupervisorPro(request):
    cargaColaborador(request)
    entidad_seleccionada_id = request.session.get('entidad_seleccionada_id')
    auditorSupervisor_form = AuditorSupervisorForm(entidad_seleccionada_id=entidad_seleccionada_id)

    if request.method == 'POST':
        auditorSupervisor_form = AuditorSupervisorForm(data=request.POST, entidad_seleccionada_id=entidad_seleccionada_id)
        if auditorSupervisor_form.is_valid():
            auditorSupervisor_form.save()
            return redirect(reverse('auditorSupervisor')+'?ok')
        else:
            return redirect(reverse('auditorSupervisor')+'?error')
    return render(request, 'proyecto/auditorSupervisor.html',{'form':auditorSupervisor_form})

@login_required
@entidad_requerida
def cargaColaborador(request):
    colaboradores = AuditorSupervisor.objects.all()
    return render(request,'proyecto/colaborador.html',{'colaboradores':colaboradores})

@login_required
@entidad_requerida
def editarColaborador(request,nombre):
    colaborador = AuditorSupervisor.objects.get(nombre=nombre)
    return render(request, 'proyecto/editarColaborador.html',{'colaborador':colaborador})

@login_required
@entidad_requerida
def editaColaborador(request):
    entidad = request.POST['entidad']
    nombre = request.POST['nombre']
    cargo = request.POST['cargo']
    colegiado = request.POST['colegiado']
    tipo_auditoria = request.POST['tipo_auditoria']
    periodo = request.POST['periodo']
    nombramiento = request.POST['nombramiento']
    fecha_nombramiento = request.POST['fecha_nombramiento']
    tareas = request.POST['tareas']
    tipo = request.POST['tipo']

    colaborador = AuditorSupervisor.objects.get(nombre=nombre)
    # colaborador.entidad = entidad
    # colaborador.nombre = nombre
    colaborador.cargo = cargo
    colaborador.colegiado = colegiado
    colaborador.tipo_auditoria = tipo_auditoria
    colaborador.periodo = periodo
    colaborador.nombramiento = nombramiento
    colaborador.fecha_nombramiento = fecha_nombramiento
    colaborador.tareas = tareas
    colaborador.tipo = tipo

    colaborador.save()
    return redirect(reverse('cargaColaborador'))

@login_required
@entidad_requerida
def eliminarColaborador(request,nombre):
    colaborador = AuditorSupervisor.objects.get(nombre=nombre)
    colaborador.delete()
    return redirect(reverse('cargaColaborador'))

#imprime en pdf el listado de colaboradores de todas las entidades
@login_required
@entidad_requerida
def imprimirColaborador(request):
    colaboradores = AuditorSupervisor.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="colaboradores.pdf"'

    buffer = BytesIO()

    # Crea el objeto PDF y se establece el tamano de la pagina
    A4_horizontal = landscape(A4)
    pdf = canvas.Canvas(response, pagesize=A4_horizontal)

    fecha = datetime.now()
    hoy = fecha.strftime('%d/%m/%y')

    #Header
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica',22)
    pdf.drawString(30,500,'Audita')

    pdf.setFont('Helvetica',12)
    pdf.drawString(30,485,'Reporte')

    pdf.setFont('Helvetica-Bold',12)
    pdf.drawString(750,500, hoy)
    pdf.line(740,497,810,497)

    #Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.fontName = 'Helvetica-Bold'
    styleBH.alignment = reportlab.lib.enums.TA_CENTER
    styleBH.fontSize = 8

    entidad = Paragraph('''Entidad''',styleBH)
    nombre = Paragraph('''Nombre''',styleBH)
    cargo = Paragraph('''Cargo''',styleBH)
    colegiado = Paragraph('''Colegiado''',styleBH)
    tipo_auditoria = Paragraph('''Tipo de Auditoria''',styleBH)
    periodo = Paragraph('''Periodo''',styleBH)
    nombramiento = Paragraph('''Nombramiento''',styleBH)
    fecha_nombramiento = Paragraph('''Fecha de Nombramiento''',styleBH)
    tareas = Paragraph('''Tareas''',styleBH)
    tipo = Paragraph('''Tipo''',styleBH)

    data = []
    data.append([entidad,nombre,cargo,colegiado,tipo_auditoria,periodo,nombramiento,fecha_nombramiento,tareas,tipo])
    
    # #Table Body
    styles = getSampleStyleSheet()
    styleN = styles["Normal"]
    styleN.alignment = reportlab.lib.enums.TA_LEFT
    styleN.fontSize = 7

    high = 405
    for colaborador in colaboradores:
        this_collaborator = [Paragraph(str(colaborador.entidad),styleN),Paragraph(str(colaborador.nombre),styleN),
                             Paragraph(str(colaborador.cargo),styleN),Paragraph(str(colaborador.colegiado),styleN),
                             Paragraph(str(colaborador.tipo_auditoria),styleN),Paragraph(str(colaborador.periodo),styleN),
                             Paragraph(str(colaborador.nombramiento),styleN),Paragraph(str(colaborador.fecha_nombramiento),styleN),
                             Paragraph(str(colaborador.tareas),styleN),Paragraph(str(colaborador.tipo),styleN)]
        data.append(this_collaborator)
        high -=18
    
    #table size
    width,height = A4_horizontal
    table = Table(data, colWidths=[2.5 * cm,3.5 * cm,2.5 * cm,2.5 * cm,2.5 * cm,2.5 * cm,2.5 * cm,2.5 * cm,3.0 * cm,2.0 * cm,])
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX',(0,0), (-1,-1), 0.25, colors.black)
    ]))

    #pdf size
    table.wrapOn(pdf, width,height)
    table.drawOn(pdf, 30, high)
    pdf.showPage()

    # Guarda el archivo PDF y cierra el objeto PDF
    pdf.save()
    pdfs = buffer.getvalue()
    buffer.close()
    response.write(pdfs)

    return response

# maneja las notificaciones del sistema por medio de correo electronico
@login_required
@entidad_requerida
def Notificacion(request):
    notificacion_form = NotificacionForm(user=request.user)

    if request.method == 'POST':
        notificacion_form = NotificacionForm(data=request.POST, user=request.user)
        if notificacion_form.is_valid():
            # Se obtiene la direccion de correo y el nombre del usuario notificado
            email_destino = notificacion_form.instance.nombre_notificado.email
            nombre_destino = notificacion_form.instance.nombre_notificado.first_name

            # Estructura del cuerpo del mensaje
            mensaje = (
                f"Estimado {nombre_destino}.\n\n"
                f"Fecha: {notificacion_form.instance.fecha_notificacion}\n"
                f"Entidad:{notificacion_form.instance.entidad.nombre}\n\n"
                f"{notificacion_form.instance.nota}\n\n"
                f"Atentamente,\n\n{notificacion_form.instance.nombre_notifica} "
            )

            # enviar correo electrionico
            send_mail('Notificación de Audita',
                      mensaje,
                      'noreply@audita.com',
                      [email_destino],
                      fail_silently=False,
                      )
            # Guarda notificacion en base de datos
            notificacion_form.save()
            return redirect(reverse('notificacion')+'?ok')
        else:
            return redirect(reverse('notificacion')+'?error')
    return render(request, 'proyecto/notificacion.html',{'form':notificacion_form})