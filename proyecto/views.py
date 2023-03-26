import reportlab
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactoForm, EntidadFrom
from proyecto.models import Contacto
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
