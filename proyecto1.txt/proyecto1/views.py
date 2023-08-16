from django.template import template, Context, loader
from django.http import HttpResponse
import datetime

def bienvenida (request):
    return HttpResponse("Bienvenidos al curso de Django!!")

def bienvenida_html(request):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 55630</h2>
    <h3>Hoy es {hoy}</h2>
    </html
    """
    return HttpResponse(response)  

def saludar(request, nombre):
    response = f"Hola, bienvenido {nombre} al curso de Django!"
    return HttpResponse(response)      

def calcular_bruto(request, neto):
    neto = int(neto)
    response = f"<html><h1>El bruto de la factura es {neto*1.21}$</h1></html>"    
    return HttpResponse(response)

def bienvenida_template(request):
    nombre = "Micaela"
    apellido= "Arias"

    curso = "Python Django"
    notas = [8,9,7,10,8]
    diccionario = {"nombre": nombre, "apellido": apellido, "curso": curso, "notas": notas}
    
    plantilla = loader.get_template('bienvenido.html')  
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)