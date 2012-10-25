'''
Created on 03/10/2012

@author: carlos
'''
from magmasoft.dao.daoutil import DaoUtil
from magmasoft.dao.encuestadao import EncuestaDAO
from magmasoft.dao.coloniadao import ColoniaDAO
from magmasoft.service.encuestafamiliarservice import EncuestaFamiliarService
from magmasoft.dao.calledao import CalleDAO

class ServiceFactory(object):
    '''
    classdocs
    '''
    config = None
    daoUtil = None
    dbConn = None
    daos = None
    services = None
    

    def __init__(self, config ):
        '''
        Constructor
        '''
        self.config = config
        self.daoUtil = DaoUtil(self.config) 
        self.dbConn = self.daoUtil.getConnection()
        
        encuestaDAO = EncuestaDAO(self.dbConn)
        coloniaDAO = ColoniaDAO(self.dbConn)
        calleDAO = CalleDAO(self.dbConn)
    
        self.daos = {
                "encuestaDAO": encuestaDAO,
                "coloniaDAO": coloniaDAO,
                "calleDAO": calleDAO
                }
        
        encuestaFamiliarService = EncuestaFamiliarService(self.daos)
        
        self.services = { "encuestaFamiliarService": encuestaFamiliarService }
        
        pass
    
    def getServices(self):
        '''
        obtiene un diccionario con los servicios por su nombre
        '''
        return self.services
    
    def closeConnection(self):
        '''
        '''
        self.dbConn.close()
        pass
    
    