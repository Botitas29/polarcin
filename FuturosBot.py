
from FuturosConsultas import FuturosConsultas as Consultas
from FuturosOrdenes import FuturosOrdenes as Ordenes
from Binance import Binance
import json


class FuturosBot(Binance):
    orden = ""
    ticker = ""

    def __init__(self):
        Binance.__init__(self)

    def ObtenerComando(self, texto: str) -> str:
        compra = ["comprar", "compra", "buy", "long"]
        venta = ["vender", "venda", "sell", "short"]
        if texto.lower() in compra:
            return "Comprar"
        if texto.lower() in venta:
            return "Vender"

    def ObtenerTicker(self, texto: str) -> str:
        ticker = texto.upper()
        if "PERP" in ticker:
            ticker = ticker.replace("PERP", "")
        if "USDT" not in ticker:
            ticker += "USDT"
        return ticker

    def Desglozar(self, mensaje: str):
        x = mensaje.split()
        self.orden = self.ObtenerComando(x[0])
        self.ticker = self.ObtenerTicker(x[1])

    def ObtenerPosicion(self, ticker: str) -> float:
        c = Consultas()
        return c.ObtenerPosicion(ticker)

    def ObtenerCantidad(self, ticker: str) -> float:
        f = open("Cantidades.json", "r")
        cantidades = json.load(f)
        f.close()
        if ticker in cantidades:
            return cantidades[ticker]
        return 0.0

    def Entrar(self, mensaje: str) -> bool:
        o = Ordenes()
        self.Desglozar(mensaje)
        pos = self.ObtenerPosicion(self.ticker)
        cantidad = self.ObtenerCantidad(self.ticker)
        
        
        if self.orden == "Comprar":
            o.ComprarMarket(self.ticker, cantidad)
            self.Log("Comprando" + self.ticker + " Cant:" + str(abs(pos)))
            
        if self.orden == "Vender":
            o.VenderMarket(self.ticker, cantidad)
            self.Log("Vendiendo" + self.ticker + " Cant:" + str(abs(pos)))
       
        
       
        