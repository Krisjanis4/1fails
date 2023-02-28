class mebeles:
    krasa: str
    matreals: int
class galds(mebeles):
    kajuskaits: str
    def lietot(self):
        return "Ok"
class skapis(mebeles):
    durvjuskaits: str

class apalaisgalds(galds):
    def lietot(self):
        return "Apailaisgalds OK"
class baltaisgalds(galds):
    def lietot(self):
        return "Baltaisgalds Ok"

Apailaisgalds = apalaisgalds()
print(Apailaisgalds.lietot())



'''
class Transportlidzeklis:
    krasa: str
    ritenuSkaits: int
class Automasina(Transportlidzeklis):
    dzinejaTips: str
    def braukt(self):
        return "OK"
class Ritenis(Transportlidzeklis):
    dzinejaTips: str
class Zigulis(Automasina):
    def braukt(self):
        return "Zigulis: OK"
class WGolf(Automasina):
    '''

'''
class nosaukums:
    mainigais: str 
    
    def_init_(self, param) -> None:
    self.mainigais = param
    def funkcija(self, param1):
    self.mainigais
    return 0

objekts = nosaukums()
print(objekts.funkcija(0))
'''