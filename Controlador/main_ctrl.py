from PyQt5 import QtCore, QtWidgets

from Vista import main_view_ui as mvui
class RootController():
    
    def __init__(self,Form,datos):
        self.tabla=mvui.Vista(Form)  
        self.llenarTablaMuestras(Form,datos,self.tabla)
        self.llenarTablaFrecuencias(Form,datos,self.tabla)

    def llenarTablaMuestras(self,Form,datos,tabla):
        self._translate = QtCore.QCoreApplication.translate
        self.tablaMuestra= tabla.getTablaMuestra()  
        self.tablaMuestra.setColumnCount(1)
        self.tablaMuestra.setRowCount(len(datos))

        self.item=QtWidgets.QTableWidgetItem()
        self.tablaMuestra.setHorizontalHeaderItem(0, self.item)
        self.item= self.tablaMuestra.horizontalHeaderItem(0)
        self.item.setText(self._translate("Form", "Respuesta"))

        for i in range(len(datos)):
            item=QtWidgets.QTableWidgetItem()
            self.tablaMuestra.setVerticalHeaderItem(i, item)
            item=QtWidgets.QTableWidgetItem()
            #fila  columna
            self.tablaMuestra.setItem(0,i , item)
        loop=1
        for i in range(len(datos)):
            item= self.tablaMuestra.verticalHeaderItem(i)
            item.setText(self._translate("Form", str(loop)))
            item1=self.tablaMuestra.item(i, 0)
            item1.setText(self._translate("Form",str(datos[i])))
            
            loop+=1 

    def llenarTablaFrecuencias(self, Form, datos,tabla):
        self._translate = QtCore.QCoreApplication.translate
        
        self.tablaFrecuencias=tabla.getTablaFrecuencias()
        self.tablaFrecuencias.setColumnCount(7)
        self.tablaFrecuencias.setRowCount(1)

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(0, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(0)
        item.setText(self._translate("Form", "Media"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(1, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(1)
        item.setText(self._translate("Form", "Mediana"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(2, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(2)
        item.setText(self._translate("Form", "Moda"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(3, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(3)
        item.setText(self._translate("Form", "Sesgo"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(4, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(4)
        item.setText(self._translate("Form", "Rango"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(5, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(5)
        item.setText(self._translate("Form", "Varianza"))

        item=QtWidgets.QTableWidgetItem()
        self.tablaFrecuencias.setHorizontalHeaderItem(6, item)
        item= self.tablaFrecuencias.horizontalHeaderItem(6)
        item.setText(self._translate("Form", "Desviacion Estandar"))