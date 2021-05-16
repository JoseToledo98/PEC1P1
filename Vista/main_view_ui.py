from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import  QPushButton
class Vista():
    
    
    
    

    def __init__(self,form):

        self.tablaMuestra(form)
        self.tablaFrecuencias(form)
        self.botones(form)

    def tablaMuestra(self,Form):
        self.labelTablaMuestras= QtWidgets.QLabel(Form)
        self.labelTablaMuestras.setText("Tabla de Muestras")
        self.labelTablaMuestras.setFixedWidth(160)
        self.labelTablaMuestras.move(10,7)
        self.tablamuestra =QtWidgets.QTableWidget(Form)
        self.tablamuestra.setGeometry(QtCore.QRect(10, 30, 160, 645))
        self.tablamuestra.setObjectName("tablaMuestra")
        
    def tablaFrecuencias(self,Form):
    
        self.labelTablaFrecuencias= QtWidgets.QLabel(Form)
        self.labelTablaFrecuencias.setText("Tabla de Frecuencias")
        self.labelTablaFrecuencias.setFixedWidth(160)
        self.labelTablaFrecuencias.move(200,75)
        self.tablafrecuencias =QtWidgets.QTableWidget(Form)
        self.tablafrecuencias.setGeometry(QtCore.QRect(200,100, 900.001, 115))
        self.tablafrecuencias.setObjectName("tablaFrecuencias")
        
    def botones(self,Form):
        self.labelTablaMuestras= QtWidgets.QLabel(Form)
        self.labelTablaMuestras.setText("Diagramas")
        self.labelTablaMuestras.setFixedWidth(160)
        self.labelTablaMuestras.move(320,300)
        self.btnHistograma = QPushButton('Histograma', Form)
        self.btnHistograma.setToolTip('Muestra la grafica de histograma de los datos')
        self.btnHistograma.move(400,350)

        self.btnHistograma = QPushButton('Poligono de frecuerncia', Form)
        self.btnHistograma.setToolTip('Muestra el diagrama de Poligono de Frecuencia de los datos')
        self.btnHistograma.move(520,350)
        
        self.btnHistograma = QPushButton('Ojivas', Form)
        self.btnHistograma.setToolTip('Muestra el diagrama de ojiva de los datos')
        self.btnHistograma.move(640,350)

        self.btnHistograma = QPushButton('Diagrama de barras', Form)
        self.btnHistograma.setToolTip('Muestra el diagrama de barras de los datos')
        self.btnHistograma.move(760,350)

        self.btnHistograma = QPushButton('Diagramas Circulares', Form)
        self.btnHistograma.setToolTip('Muestra el diagrama circular de los datos')
        self.btnHistograma.move(880,350)
    
    def getTablaMuestra(self):

        return self.tablamuestra  

    def getTablaFrecuencias(self):
        
        return self.tablafrecuencias  









