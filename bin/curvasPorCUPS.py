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
from os import listdir
import os
import os.path
from os.path import isfile, join
from lxml import etree
from StringIO import StringIO
from pprint import pprint
import string
import codecs
from unidecode import unidecode
import sys
import errno


def obtenerConsumosPorHoraGlobalizados(dbcur, fechaIni, fechaFin):
    resultado=[]
    query="select cups, fecha, consumo, contratos.direccion from consumos,contratos where date(fecha)>=date('%s') and date(fecha)<date('%s') and (tarifa='6.1' or tarifa='3.1A') and contratos.idinterno=consumos.contrato ORDER by cups,fecha" % (fechaIni,fechaFin)
    ultCups=""
    horas=[]
    f=None 
    #obtained from http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    try:
        os.mkdir("salida")
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir("salida"):
            pass
        else: raise
    
    for row in c.execute(query):
        cups=row[0]
        consumototal=row[1]
        hora=row[2]
	direccion=row[3]
	if (ultCups!=cups):
	  if (f!=None):
	    f.close()
	  f=open("salida/"+cups+".csv","w")
	  f.write("\""+direccion+"\"\n")
	  f.write("fecha, consumo\n")
	  ultCups=cups
        else:
	  f.write(str(row[1])+","+str(row[2])+"\n")
    if (f!=None):
	    f.close()


print "Energylyzer, Copyright (C) 2015  Jorge J. Gomez-Sanz, This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by  the Free Software Foundation, either version 3 of the License, or  (at your option) any later version."

if (len(sys.argv)<3):

	print("El formato es 'curvasPorCUPS.py nombreDeBaseDatos fechaIni fechaFin', donde nombreDeBaseDatos representa el path a un fichero sqlite con la base de datos a analizar; fechaIni y fechaFin denota las fechas entre las cuales interesa volcar los consumos. Estas fechas deben estar en el formato yyyy-mm-dd, por ejemplo 2015-01-01")

fechaIni=sys.argv[2]
fechaFin=sys.argv[3]

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

resultado=obtenerConsumosPorHoraGlobalizados(c,fechaIni,fechaFin)

conn.close()
