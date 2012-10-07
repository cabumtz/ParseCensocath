#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 01/10/2012

@author: carlos
'''
import unittest
from magmasoft.config import Config
from magmasoft.factory.servicefactory import ServiceFactory


class Test(unittest.TestCase):
    serviceFactory = None
    coloniaDAO = None

    def setUp(self):
        '''
        '''
        config = Config()
        self.serviceFactory = ServiceFactory(config)
        self.coloniaDAO = self.serviceFactory.daos["coloniaDAO"]
        pass


    def tearDown(self):
        self.serviceFactory.closeConnection()
        pass


    def test_obtenerColoniaId(self):
        colonia_id = self.coloniaDAO.obtenerColoniaId(u"San cuanácaro")
        print colonia_id
        
        colonia_id = self.coloniaDAO.obtenerColoniaId(u"San cuanácaro")
        print colonia_id
        
        colonia_id = self.coloniaDAO.obtenerColoniaId(u"Terepitengo")
        print colonia_id
        pass
    
        colonia_id = self.coloniaDAO.obtenerColoniaId(u"Terepitengo")
        print colonia_id
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()