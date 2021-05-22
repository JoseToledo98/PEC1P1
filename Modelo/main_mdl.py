from PyQt5.QtCore import QObject, pyqtSignal

import os 

class Model(QObject):
    datos=[]
    def connect(self):
        
        #lectura de archivo txt donde estan los datos
        os.chdir("Modelo")   
        self.f=open("../Recursos/Datos.txt","r")
        #guardar la lectura separada por columas en una sola lista
        self.lineas= [linea.split(";") for linea in self.f]
        #cerrar el archivo despues de obtener los datos
        self.f.close()
        #hacer dos listas de datos para poder manejarlas mejor en la tabla
        for i in range(1,len(self.lineas)):
            b=table_mdl()
            self.estado= self.lineas[i][0]== "Si"
            if self.estado== True:
                b.setJuega(self.lineas[i][0])
                b.setGenero(self.lineas[i][1])
                b.setEdad(self.lineas[i][2])
                b.setTiempo(self.lineas[i][3])
                
                self.datos.append(b)
            else :
                b.setJuega("No")
                b.setGenero("  ")
                b.setEdad(" ")
                b.setTiempo(" ")
                
                self.datos.append(b)

        return self.datos


class table_mdl():
    def __init__(self):
        self.juega =""
        self.genero=""
        self.edad=0
        self.tiempo=0.0

    def getJuega(self):
        return self.juega
    def getGenero(self):
        return self.genero
    def getEdad(self):
        return self.edad
    def getTiempo(self):
        return self.tiempos
    def setJuega(self,newVar):
        self.juega = newVar
    def setGenero(self,newVar):
        self.genero = newVar
    def setEdad(self,newVar):
        self.edad = newVar
    def setTiempo(self,newVar):
        self.tiempos = newVar

    def toString(self, num):
        print(num,".- juega?: " + self.juega+", genero favorito: "+ self.genero+", que edad tiene?: "+self.edad+", Que tiempo juega: "+self.tiempos)       

