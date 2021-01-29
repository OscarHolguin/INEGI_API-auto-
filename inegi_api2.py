# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:58:50 2020

@author: Oscar Holguin
"""

#inegi api example
import os
inegi_api=os.environ['INEGI_API'] #choose your INEGI API 

#OOP to get data from INEGI 
class BIES:
    def __init__(self,url):
        self.url=url
    
    def contenido(self):
        import requests
        import json
        import pandas as pd
        if requests.get(self.url).status_code==200:
            data=json.loads(requests.get(self.url).content)
            data=pd.DataFrame(data['Series'])
        else:
            data='Error: {}'.format(requests.get(self.url).content)
        return data
    def get_key(self,indicador):
        key=self.contenido()[self.contenido()['INDICADOR']==str(indicador)]['OBSERVATIONS'].keys()[0]
        return key
    
    def indicador_valor(self,indicador):
        value=float(self.contenido()[self.contenido()['INDICADOR']==str(indicador)]['OBSERVATIONS'][self.get_key(indicador)][0]['OBS_VALUE'])
        return value
    @classmethod
    def get_period(cls):
        return cls(url2).contenido()['OBSERVATIONS'][0][0]['TIME_PERIOD']


#call API example IED (Trimestral Economic Growth ITAEE)
url2='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/491666/es/0700/true/BIE/2.0/'+inegi_api+'?type=json'

      
itae=BIES(url2)
itae_ind=(itae.indicador_valor(491666))

itae_ind=round(itae_ind,2)
print('The economic growth for chihuahua is', itae_ind, 'for the period',itae.get_period())
