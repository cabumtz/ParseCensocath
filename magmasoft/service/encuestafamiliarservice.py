'''
Created on 03/10/2012

@author: carlos
'''
import logging
from magmasoft.dao.daoutil import DaoUtil

class EncuestaFamiliarService(object):
    '''
    classdocs
    '''
    daos = None
    logger = logging.getLogger("services")
    

    def __init__(self, daos):
        '''
        Constructor
        '''
        self.daos = daos
        pass
    
    
    def guardar(self, datosEncuesta, listaPersonas, nombreColonia):
        '''
        '''
        ID_ENCUESTADOR_OTRO = 1
        
        
        encuestaDAO = self.daos["encuestaDAO"]
        coloniaDAO = self.daos["coloniaDAO"]
        
        encuestador_id = ID_ENCUESTADOR_OTRO
        
        colonia_id = coloniaDAO.obtenerColoniaId(nombreColonia)
        
        fecha = ( datosEncuesta["FECHA"] if ("FECHA" in datosEncuesta) else None)
        observacion = ( datosEncuesta["OBSERVACION"] if ("OBSERVACION" in datosEncuesta) else None)
        
        self.logger.debug("insert in Encuesta(%s, %s, %s)" %
                          ( DaoUtil.getSQLDateFromString(fecha), encuestador_id, observacion ))
        
        encuesta_id = encuestaDAO.insertar(
                            DaoUtil.getSQLDateFromString(fecha),
                            encuestador_id,
                            observacion)
        
        self.logger.debug( "encuesta_id: %s" % (encuesta_id) )
        
        
        #logger.debug("insert in Familia(%s, %s, %s)" % ( getSQLDateFromString(fecha), ID_ENCUESTADOR_OTRO, observacion ))
        
        pass
    
    