#!/usr/bin/python
# -*- coding: UTF-8 -*-

from magmasoft.config import Config
from magmasoft.factory.servicefactory import ServiceFactory
from optparse import OptionParser
import codecs
import csv
import json
import logging


logger = logging.getLogger("main")

#####################################################
#
#####################################################
def renglonVacio( cells ) :
	"""   """
	if( cells == None ) :
		return False
	for cel in cells :
		if( cel != '' ):
			return False
		
	return True


def writeUtf8(fo, msg):
	fo.write(msg.encode('utf-8'))
	logger.debug( msg.encode('utf-8') )

def obj2String( obj ):
	return json.dumps(obj)

def readUtf8():
	None
	

def print_unicode_dict(di):
	
	strVal = ""
	
	for key in di :
		value = di[key]
		
		strVal = str(value)
			
		logger.debug( "%s => %s" % ( key, strVal ) )
	
		

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
	csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
	for row in csv_reader:
		yield [unicode(cell, 'utf-8') for cell in row]

			
#####################################################
#
#####################################################
def mainProcess(colonia, serviceFactory) :
	""" Cadena comentario """
	salir = False
	renVacio = False
	renNulo = False
	services = serviceFactory.getServices()
	
	logfile = codecs.open("logfile.txt", "w")
	
	csvfile = open( "input/testParseCenso3OO.csv", "r")
	
	rowreader = unicode_csv_reader(csvfile)

	while (not salir) :
		
		writeUtf8( logfile, "-----------------------------------------\n")
		
		while ( True ) :
			cells = rowreader.next();
			if( not renglonVacio(cells) ) :
				break
		
		# se espera leer encabezado
		
		#primer renglon de datos
		listaDatos = []
		salir2 = False
		while( not salir2 ) :
			cells = rowreader.next();
			
			if (cells == None) :
				salir2=True
				renNulo = True
				break
			
			if ( renglonVacio(cells) ) :
				renVacio = True
				writeUtf8( logfile," -  -  -  -  -  -  -  -  -  -  -  -\n")
				break
			else :
				datos = {}
				datos["PARENTESCO"] = cells[0]
				datos["NOMBRE"] = cells[1]
				datos["EDAD"] = cells[2]
				datos["SEXO"] = cells[3]
				datos["RELIGION"] = cells[4]
				datos["LUGAR DE ORIGEN"] = cells[5]
				
				writeUtf8( logfile, obj2String( datos ) )
				writeUtf8( logfile, "\n" )
				listaDatos.append(datos)
				
		# logfile.write listaDatos

		if ( not renVacio ) :
			
			break
		
		# leer propiedades
		renVacio = False
		salir3 = False
		datosEncuesta = {}
		while ( not salir3 ) :
			try:
				cells = rowreader.next();
			
				if ( renglonVacio(cells) ) :
					renVacio = True
					break
				else :
					datosEncuesta[cells[0]] = cells[1]
			except Exception, e :
				#logfile.write "ERROR Exception: "
				#logfile.write e
				salir = True
				salir2 = True
				salir3 = True
				break

		writeUtf8( logfile, obj2String( datosEncuesta ) )
		writeUtf8( logfile, str( "\n" ) )
	
		# escribir a base de datos
		services["encuestaFamiliarService"].guardar(datosEncuesta, listaDatos, colonia)
		#return

	logfile.close()
	pass		


#####################################################
#
#####################################################
def mainFunc():
	parser = OptionParser()
	parser.add_option("-c", "--colonia", dest="colonia", help="nombre de la colonia" )

	(options, args) = parser.parse_args()
	
	logger.debug( "colonia: %s" %  options.colonia )
	
	# abrir la conexión de la base de datos
	config = Config()
	serviceFactory = ServiceFactory(config)
	
	mainProcess(options.colonia, serviceFactory)
	pass



#####################################################
#
#####################################################
mainFunc()
