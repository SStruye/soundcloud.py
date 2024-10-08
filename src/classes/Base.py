import requests
import re
from urllib.parse import urlparse, parse_qs

class Base:
    def __init__(self, clientId : str, oauthToken : str):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def getClientId(self):
        return self._params["client_id"]
    
    def setClientId(self, clientId : str):
        self._constParams["client_id"] = clientId
        self._params["client_id"] = clientId

    def getOauthToken(self):
        return self._headers["Authorization"]
    
    def setOauthToken(self, oauthToken : str):
        self._constHeaders["Authorization"] = oauthToken
        self._headers["Authorization"] = oauthToken
        self._headers.update(self._constHeaders)

    # def fetchClientId():
    # def fetchOauthToken():

    def getHeaders(self):
        return self._headers
    
    def setHeaders(self, headers : dict):
        self._headers = headers
        self._headers.update(self._constHeaders)

    def addHeaders(self, headers : dict):
        self._headers.update(headers)   

    def resetHeaders(self):
        self._headers = self._constHeaders

    def getParams(self):
        return self._params
    
    def setParams(self, params : dict):
        self._params = params
        self._params.update(self._constParams)
    
    def addParams(self, params : dict):
        self._params.update(params)

    def resetParams(self):
        self._params = self._constParams

    def getRequest(self, endpoint : str):
        endpoint = re.sub(r'^/?(.*?)/?$', r'/\1', endpoint)
        response = requests.get(url = self._apiURL + endpoint, params = self._params, headers= self._headers)
        if("application/json" in response.headers["Content-Type"]): return response.json()
        return response.text
    
    def resolve(self, resolvable: str | int):
        if(resolvable[0] == "/"): resolvable = resolvable[1:]
        if(resolvable[-1] == "/"): resolvable = resolvable[:-1]
        if(not "soundcloud" in resolvable): resolvable = f'https://soundcloud.com/{resolvable}'
        self.setParams({"url" : resolvable})
        resolved = self.getRequest(endpoint = "/resolve")
        return resolved
    
    def _getCollection(self, endpoint : str):
        self.setParams({"linked_partitioning" : 1, "limit" : 20})
        response = self.getRequest(endpoint)
        collection = response.get("collection")
        next_href = response.get("next_href")
        while(next_href):
            self.setParams(parse_qs(urlparse(next_href).query))
            response = self.getRequest(endpoint)
            next_href = response.get("next_href")
            collection += response.get("collection")
        return collection
    
    _params = {}
    _headers = {}
    _apiURL = "https://api-v2.soundcloud.com"
    _constParams = {}
    _constHeaders = {
        "Origin": "https://soundcloud.com",
        "Referer": "https://soundcloud.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
        "x-datadome-clientid": "3299Bm7k0xNz616xuOP97IrSS5lq_twWW97JnTlmbE60y5fd9p61TsW6Xc7fbO5YeGuDgSXHIn0KI5HC0VZeIVkW1dSf9a3SoBXEZ1TzGxT4TCMOBv8aYGCVbehIFZC5"
    }