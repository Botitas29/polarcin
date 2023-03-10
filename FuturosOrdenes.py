import requests
from Binance import Binance

class FuturosOrdenes(Binance):
    def __init__(self):
        Binance.__init__(self)
    
    def ComprarMarket(self, simbolo:str, cantidad:float) ->dict:
        endPoint = self.url + "/fapi/v1/order"
        parametros = "timestamp=" + str(self.ObtenerFechaServer())
        parametros += "&symbol=" +simbolo.upper()
        parametros += "&side=BUY"
        parametros += "&type=MARKET"
        parametros += "&quantity=" + str(cantidad)
        
        parametros = self.Firmar(parametros)
        
        h = self.Encabezados(self.apikey)
        
        r = requests.post(endPoint, params=parametros, headers=h)
        return r.json()
    
    def CerrarCompraMarket(self, simbolo:str, cantidad:float) ->dict:
        endPoint = self.url + "/fapi/v1/order"
        parametros = "timestamp=" + str(self.ObtenerFechaServer())
        parametros += "&symbol=" +simbolo.upper()
        parametros += "&side=SELL"
        parametros += "&type=MARKET"
        parametros += "&quantity=" + str(cantidad)
        parametros += "&reduceOnly=True"
        
        parametros = self.Firmar(parametros)
        
        h = self.Encabezados(self.apikey)
        
        r = requests.post(endPoint, params=parametros, headers=h)
        return r.json()
    
    def VenderMarket(self, simbolo:str, cantidad:float) ->dict:
        endPoint = self.url + "/fapi/v1/order"
        parametros = "timestamp=" + str(self.ObtenerFechaServer())
        parametros += "&symbol=" +simbolo.upper()
        parametros += "&side=SELL"
        parametros += "&type=MARKET"
        parametros += "&quantity=" + str(cantidad)
        
        parametros = self.Firmar(parametros)
        
        h = self.Encabezados(self.apikey)
        
        r = requests.post(endPoint, params=parametros, headers=h)
        return r.json()
    
    def CerrarVentaMarket(self, simbolo:str, cantidad:float) ->dict:
        endPoint = self.url + "/fapi/v1/order"
        parametros = "timestamp=" + str(self.ObtenerFechaServer())
        parametros += "&symbol=" +simbolo.upper()
        parametros += "&side=Buy"
        parametros += "&type=MARKET"
        parametros += "&quantity=" + str(cantidad)
        parametros += "&reduceOnly=True"
        
        parametros = self.Firmar(parametros)
        
        h = self.Encabezados(self.apikey)
        
        r = requests.post(endPoint, params=parametros, headers=h)
        return r.json()
    
    