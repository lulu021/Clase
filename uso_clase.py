#definir clase
class Municipio:
    #declarar atributos de la clase
    nom = ""
    cve = ""
    __pobTot = 0    #variable privada (doble guion bajo)
    _alt = 0        #solo puede ser usada en esta clase, atributos protegidos(guion bajo)
    sup = 0        
    
    # Definir constructor
    def __init__ (self, nombre, clave, pobTotal, altitud, superficie): #Deben de declararse las variables que se ocupan en la clase}
        self.nom = nombre
        self.cve = clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie




    # A todo atributo asimismo a los que sean privado o protegido se le deberá asignar un método GET y SET
    def getNom(self):
        return self.nom
    def setNom(self, nombre):
        try:
            nom = str(nombre)
            self.nom = nombre
        except:
            print("Introduce un municipio")



   #_______________________________________________________________________________________________________________
    def getCVE(self):
        return self.cve
    def setCVE(self, clave):
        try:
            cve = str(clave)
            self.cve = clave
        except:
            print("Escribe la clave de un municipio")
    #__________________________________________________________________________________________________________________
    def getPobTota(self):
        return self.__pobTot
    def setPobTota(self, pobTotal):
        try:
            __pobTot = str(pobTotal)
            self.__pobTot = pobTotal
        except:
            print("Escribe la poblacon total de un municipio")
    #___________________________________________________________________________________________________________________
    def getAltu(self):
        return self._alt
    def setAltu(self, altitud):
        try:
            _alt = str(altitud)
            self._alt = altitud
        except:
            print("Escribe la altura de un municipio")
    #___________________________________________________________________________________________________________________
    def getsuper(self):
        return self.sup
    def setsuper(self, superficie):
        try:
            sup = str(superficie)
            self.sup = superficie
        except:
            print("Escribe la superficie de un municipio")
            
    def info(self):
        print("El nombre del municipio es: ", self.nom, "y su clave inegi", self.cve, "y tiene una superficie de ", self.sup)
    def supKm(self, valor):
        if valor>10000:
            print("Es un municipio grande")
        else:
            print("Es un municipio pequeño")

Mun = Municipio("Toluca", "106", 74515, 4700, 45751)
print(Mun.getNom())    
Mun.setNom("Metepec")
print(Mun.getNom())        
print(Mun.getCVE())
print(Mun.getPobTota())
print(Mun.getAltu())
print(Mun.getsuper())
print(Mun.info())

    
class colonia(Municipio):
    ah = 0
    
    def __init__(self,areaH, nombre, clave, pobTotal, altitud, superficie):
        super().__init__(nombre,clave, pobTotal, altitud, superficie)
        self.ah = areaH = areaH
    #Metodos de la clase
    def getAH(self):
        return self.ah
    def setAH(self, ah):
        self.ah = ah
    #Metodos alternativos
    def infoAH(self, value):
        self.ah = self.ah+ value
        self.info()
        print(self.nom, "cuenta con ", self.ah, "áreas homogéneas")# self.nom es un atributo de la clase municicpio
        
col = colonia(5,"Toluca", "106", 7435435, 4700, 453634)
print(col.infoAH(3))
print(col.getNom())# la clase colonia no tiene el método getNom()pero es accesible mediante la herencia de la clase Municipio





