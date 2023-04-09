from romanos_exception import *
from utiles import *

class NumeroRomano:
    valor_romano=""
    valor_entero=0
    representacion_romano=""
    valor=0
    def __init__(self,valor):
        
        if isinstance(valor, str):#aqui ingresa si el valor es string
            self.representacion_romano = valor
            self.valor = self.romano_a_entero(valor)
        elif isinstance(valor,int):#aqui ingresea si el valor es int    
            self.valor = valor
            self.representacion_romano= self.entero_a_romano(self.valor)
        else:
            raise RomanNumberError("El valor debe ser cadena o entero")     
        

    def entero_a_romano(self,numero:int)->str:
        if numero > 3999 or numero < 0:
            raise RomanNumberError("El limite entre 0 y 3999")
        if numero == 0:
            return ""

        numero = "{:0>4d}".format(numero)
        list_numero = list(numero)
        self.valor_romano=""
        longitud= len(list_numero)
        
        for i in range(longitud):
            longitud = longitud-1
            list_numero[i] = list_numero[i]+"0"*longitud
            self.valor_romano +=dic_entero_a_romanos.get( int(list_numero[i]) ,"")

        return self.valor_romano
    

    def romano_a_entero(self,valor:str)->int:
        lista_romano = list(valor)
        self.valor_entero=0
        cont_repes=0
        caracter_anterior=""
        caracter_ante_anterior=""

        for caracter in lista_romano:
            if caracter == caracter_anterior:
            
                if caracter in "DLV": 
                    raise RomanNumberError("Los caractares D, L y V no se pueden repetir")
                cont_repes +=1
            else:
                cont_repes = 0 

            if cont_repes >= 3:
                raise RomanNumberError("No se puede repetir el valor mas de tres veces seguidas")

            if caracter_anterior and dic_romano_a_entero.get(caracter_anterior,0) < dic_romano_a_entero.get(caracter,0):
                
                if caracter_anterior in "DLV": 
                    raise RomanNumberError("Los caractares D, L y V no se pueden restar")
            
                if caracter not in restas[caracter_anterior]:
                    raise RomanNumberError(f"{caracter_anterior} solo se puede restar de {restas[caracter_anterior][0]} y {restas[caracter_anterior][1]}")    
                self.valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2
                    
                if caracter_anterior == caracter_ante_anterior and caracter_anterior in "IXC":
                    raise RomanNumberError("el valor no puede restarse")

            caracter_ante_anterior =caracter_anterior
            caracter_anterior = caracter
            self.valor_entero += dic_romano_a_entero.get(caracter,0)
        
        return self.valor_entero

    
    def __repr__(self):
        return self.representacion_romano
    
    def __add__(self,otro):
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor+otro.valor)
        elif isinstance(otro,int):
            return NumeroRomano(self.valor+otro)

    def __sub__(self,otro): 
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor-otro.valor)
        elif isinstance(otro,int):
            return NumeroRomano(self.valor-otro)