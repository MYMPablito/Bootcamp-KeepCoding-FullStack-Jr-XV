class Views:

    def insertCoin(self):
        crypto = input("Ingrese una criptomoneda conocida: ").upper()
        return crypto
    
    def viewListCoins(self,listcoin):
        print(f"La cantidad de criptos son: {len(listcoin.lista_criptos)},\
      y la cantidad de no criptos son: {len(listcoin.lista_no_criptos)}")
        
    def viewRateExchange(self,change):
        print( "{:,.2f}€".format(change.rate).replace(",","@").replace(".",",").replace("@",".") )

    def viewError(self,er):
        print(er)