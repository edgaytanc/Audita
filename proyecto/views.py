import reportlab
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactoForm, EntidadFrom, AuditorSupervisorForm, NotificacionForm
from proyecto.models import Contacto, AuditorSupervisor
from datetime import datetime

#Ingresa nuevos contactos
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
def lista_Contacto(request):
    contactos = Contacto.objects.all()
    context = {
        'contactos':contactos
    }
    return render(request, 'proyecto/lista_contactos.html', context)

#busca un contacto y lo despliega
def detalle_contacto(request):
    contacto_id = request.GET.get('id')
    contacto = Contacto.objects.get(id=contacto_id)
    context = {
        'contacto': contacto
    }
    return render(request, 'proyecto/detalle_contacto.html', context)

#Imprime en pdf la lista de contactos
def imprimir_contactos(request):
    contactos = Contacto.objects.all()
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contactos.pdf"'

    buffer = BytesIO()
    # Crea el objeto PDF y establece el tamaño de la página
    pdf = canvas.Canvas(response, pagesize=A4)

    fecha = datetime.now()
    hoy = fecha.strftime('%d/%m/%y')

    #Header
    pdf.setLineWidth(.3)
    pdf.setFont('Helvetica',22)
    pdf.drawString(30,750,'Audita')

    pdf.setFont('Helvetica',12)
    pdf.drawString(30,735,'Reporte')

    pdf.setFont('Helvetica-Bold',12)
    pdf.drawString(480,750, hoy)
    pdf.line(460,747,560,747)

    # table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = reportlab.lib.enums.TA_CENTER
    styleBH.fontSize = 10

    nombre = Paragraph('''Nombre''',styleBH)
    movil = Paragraph('''Movil''',styleBH)
    telefono = Paragraph('''Telefono''',styleBH)
    email = Paragraph('''Email''',styleBH)
    cargo = Paragraph('''Cargo''',styleBH)
    empresa = Paragraph('''Empresa''',styleBH)

    data = []

    data.append([nombre,movil,telefono,email,cargo,empresa])

    #Table body
    styleN = styles["BodyText"]
    styleN.alignment = reportlab.lib.enums.TA_CENTER
    styleN.fontSize = 7

    high = 650
    for contacto in contactos:
        this_contact = [contacto.nombre, contacto.movil, contacto.telefono, contacto.email, contacto.cargo, contacto.empresa]
        data.append(this_contact)
        high -= 18

    # table size
    width, height = A4
    table = Table(data, colWidths=[4.0 * cm, 2.5 * cm, 2.5 * cm, 4.0 * cm, 2.5 * cm, 2.5 * cm, ])
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX',(0,0), (-1,-1), 0.25, colors.black)]))
    
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

#ingresa datos de la entidad a Auditar
def Entidad(request):
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

def AuditorSupervisorPro(request):
    cargaColaborador(request)
    auditorSupervisor_form = AuditorSupervisorForm()

    if request.method == 'POST':
        auditorSupervisor_form = AuditorSupervisorForm(data=request.POST)
        if auditorSupervisor_form.is_valid():
            auditorSupervisor_form.save()
            return redirect(reverse('auditorSupervisor')+'?ok')
        else:
            return redirect(reverse('auditorSupervisor')+'?error')
    return render(request, 'proyecto/auditorSupervisor.html',{'form':auditorSupervisor_form})

def cargaColaborador(request):
    colaboradores = AuditorSupervisor.objects.all()
    return render(request,'proyecto/colaborador.html',{'colaboradores':colaboradores})

def editarColaborador(request,nombre):
    colaborador = AuditorSupervisor.objects.get(nombre=nombre)
    return render(request, 'proyecto/editarColaborador.html',{'colaborador':colaborador})

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

def eliminarColaborador(request,nombre):
    colaborador = AuditorSupervisor.objects.get(nombre=nombre)
    colaborador.delete()
    return redirect(reverse('cargaColaborador'))



#imprime en pdf el listado de colaboradores de todas las entidades
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


def Notificacion(request):
    notificacion_form = NotificacionForm()

    if request.method == 'POST':
        notificacion_form = NotificacionForm(data=request.POST)
        if notificacion_form.is_valid():
            notificacion_form.save()
            return redirect(reverse('notificacion')+'?ok')
        else:
            return redirect(reverse('notificacion')+'?error')
    return render(request, 'proyecto/notificacion.html',{'form':notificacion_form})