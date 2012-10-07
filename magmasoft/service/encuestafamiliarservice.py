'''
Created on 03/10/2012

@author: carlos
'''
import logging

class EncuestaFamiliarService(object):
    '''
    classdocs
    '''
    daos = None
    daoUtil = None
    logger = logging.getLogger("services")


    def __init__(self, daos, daoUtil):
        '''
        Constructor
        '''
        self.daos = daos
        self.daoUtil = daoUtil
        pass
    
    
    def guardar(self, datosEncuesta, listaPersonas, colonia):
        '''
        '''
        ID_ENCUESTADOR_OTRO = 1
        
        
        encuestaDAO = self.daos["encuestaDAO"]
        
        encuestador_id = ID_ENCUESTADOR_OTRO
        fecha = ( datosEncuesta["FECHA"] if ("FECHA" in datosEncuesta) else None)
        observacion = ( datosEncuesta["OBSERVACION"] if ("OBSERVACION" in datosEncuesta) else None)
        
        self.logger.debug("insert in Encuesta(%s, %s, %s)" %
                          ( self.daoUtil.getSQLDateFromString(fecha), encuestador_id, observacion ))
        
        encuesta_id = encuestaDAO.insertar(
                            self.daoUtil.getSQLDateFromString(fecha),
                            encuestador_id,
                            observacion)
        
        self.logger.debug( "encuesta_id: %s" % (encuesta_id) )
        
        
        #logger.debug("insert in Familia(%s, %s, %s)" % ( getSQLDateFromString(fecha), ID_ENCUESTADOR_OTRO, observacion ))
        
        pass
    
    