# CONSUMIR SERVICIO DESDE PYTHON
# DANIEL ANDRADE
from zeep import Client

cliente = Client('http://localhost:8080/SOAPoperaciones/ConversionSW?WSDL')

print(cliente.service.hello("Daniel"))
print(cliente.service.Suma(123,567))
print(cliente.service.resta(100,90))
print(cliente.service.multiplicacion(30,40))
print(cliente.service.division(120,60))
print(cliente.service.Aceleracion(120,30,40))
print(cliente.service.velocidad(600,80))
print(cliente.service.Densidad(340,67))
