#!/usr/bin/env python
#-*- coding: UTF-8 -*-

class API:

    def __init__(self):
        self.logger = logging.getLogger("ConnectAPI")
        self.headers = None
        self.body = None
        self.url = None
    
    def __generate_headers(self):
        self.headers = {
            'authorization': 'bearer {self.__token}'.format(self.__token),
            'accept': 'application/json',
            'content-type': 'application/json',
        }
        
    def set_api_token(self, token=None, tokenfile=None)
        if token: # token passed dirctly as a string
            token = token.strip()
        elif tokenfile: # a path to a tokenfile ist passed
            token = open(tokenfile,'r').read().strip()
        else: # Try to load token from default file location
            token = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'token'),'r').read().strip()
        if len(token) != 560:
            raise Exception("Invalid Token length")
        self.__token = token
        self.__generate_headers()
        
    def operation(self, start, keyword, address=None, position=None, facts=None, ric=None, properties=None):
        self.url = "https://connectapi.feuersoftware.com/interfaces/public/operation"
        self.body = {
                'start': start,
                'keyword': keyword
                }
        if address:
            self.body['address'] = address
        if position:
            self.body['position'] =  {'latitude':position[0], 'longitude': position[1]}
        if facts:
            self.body['facts'] = facts
        if ric:
            self.body['ric'] = ric
        if properties:
            self.body['properties'] = properties
        self.__send()
    
    def status(self, radio, status, position=None):
        self.url = "https://connectapi.feuersoftware.com/interfaces/public/vehicle/{}/status".format(radio)
        self.body = {
                'status': status
                }
        if position:
            self.body['position'] = {'latitude':position[0], 'longitude': position[1]}
        self.__send()
        
    def __send(self):
        r = requests.post(self.url, data=json.dumps(self.body), headers=self.headers)
        if r.status_code != 200:
            self.logger.warning("Fehler beim senden des Alarms {r.status_code}, \"{}\"".format(r.text))
        else:
            self.logger.info("API call erfolgreich gesendet")
            
   
