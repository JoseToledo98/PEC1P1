from PyQt5.QtCore import QObject, pyqtSignal
import os 

class Model(QObject):

    def connect(self):
        
        #lectura de archivo txt donde estan los datos
        os.chdir("Modelo")   
        self.f=open("../Recursos/Datos.txt","r")
        #guardar la lectura separada por columas en una sola lista
        self.lineas= [linea.split() for linea in self.f]
        #cerrar el archivo despues de obtener los datos
        self.f.close()
        #hacer dos listas de datos para poder manejarlas mejor en la tabla
        self.muestras=self.lineas[:len(self.lineas)//2]
        self.respuestas=self.lineas[len(self.lineas)//2:]
        self.respuesta=self.respuestas[0]
        self.respuesta.pop(0)
        self.respuesta= sorted(self.respuesta)
        
        return self.respuesta
