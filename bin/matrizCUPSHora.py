"""
    Energylyzer, Suite for automatic analysis of energy comsuption 
    Copyright (C) 2015  Jorge J. Gomez-Sanz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import sys
from os import listdir
from os.path import isfile, join
from lxml import etree
from StringIO import StringIO
from pprint import pprint
import string
import codecs
from unidecode import unidecode

def obtenerConsumosPorHoraGlobalizados(dbcur, fechaIni, fechaFin):
    resultado=[]
    query="select cups, sum(consumo) as consumototal, strftime('%%H',fecha) as hora from consumos,contratos where date(fecha)>=date('%s') and date(fecha)<date('%s') and (tarifa='6.1' or tarifa='3.1A') and contratos.idinterno=consumos.contrato group by cups, hora ORDER by cups,hora" % (fechaIni,fechaFin)
    ultCups=""
    horas=[]
    for row in c.execute(query):
        cups=row[0]
        consumototal=row[1]
        hora=row[2]
	if (ultCups!=cups):
	  if (ultCups!=""):
	  	resultado.append((cups,horas))
	  horas=[(hora,consumototal)]
	  ultCups=cups
        else:
	  horas.append((hora,consumototal));
    return resultado

print "Energylyzer, Copyright (C) 2015  Jorge J. Gomez-Sanz, This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by  the Free Software Foundation, either version 3 of the License, or  (at your option) any later version."

if (len(sys.argv)<4):
	print("El formato es 'matrizCUPSHora.py nombreDeBaseDatos fechaIni fechaFin ficheroSalida', donde nombreDeBaseDatos representa el path a un fichero sqlite con la base de datos a analizar; fechaIni y fechaFin denota las fechas entre las cuales interesa volcar los consumos. Estas fechas deben estar en el formato yyyy-mm-dd, por ejemplo 2015-01-01; ficheroSalida es el nombre donde se vuelcan los datos")

fechaIni=sys.argv[2]
fechaFin=sys.argv[3]
salida=sys.argv[4]
conn = sqlite3.connect(sys.argv[1])

c = conn.cursor()
#Cambiar las fechas por las que se necesiten
resultado=obtenerConsumosPorHoraGlobalizados(c,fechaIni,fechaFin)
#Este fichero es para asegurar que se escriben los consumos asociados a las horas que se debe
#en el orden apropiado
#f=open(salida+"Prueba.csv","w")
# f.write("cups,00,,01,,02,,03,,04,,05,,06,,07,,08,,09,,10,,11,,12,,13,,14,,15,,16,,17,,18,,19,,20,,21,,22,,23\n")
#for (cups,horas) in resultado:
#	fila=cups
#	for (hora,consumo) in horas:
#		fila=fila+","+hora+","+str(consumo)
#	f.write(fila+"\n")
#f.close()
#Este fichero contiene los datos sin columnas de comprobacion
f=open(salida,"w")
f.write("cups,00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23\n")
for (cups,horas) in resultado:
	fila=cups
	for (hora,consumo) in horas:
		fila=fila+","+str(consumo)
	f.write(fila+"\n")
f.close()

conn.close()
