class Municipio:
    #Se declaran atributos de la clase
    nom=""
    cve =""
    __pobTot = 0 #Doble guion bajoson atributos privados
    _alt= 0 #Un guion bajo son atributos protegidos
    sup= 0
    #Defnir constructor
    def __init__(self, nombre, clave, pobTotal, altitud, superficie):
        self.nom = nombre
        self.cve= clave
        self.__pobTot = pobTotal
        self._alt = altitud
        self.sup = superficie
        
    #A todo atributo que sea privado o protegido se le debeberá asignar un metodo GET(obtenerse) y SET(asignarse)
    def getNom(self):
        return self.nom
    def setNom(self,nombre):
        try:
            nom= str(nombre)
            self.nom= nombre
        except:
            print("Introduce un municipio")
            
Mun = Municipio("Toluca", "106", 7435435, 4700, 453634)
print(Mun.getNom())
 