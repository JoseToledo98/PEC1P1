from PyQt5 import QtCore, QtGui, QtWidgets
from Controlador import main_ctrl as _mcrtl
from Modelo import main_mdl as _modelo
from Controlador import frecuences_ctrl as _frcCtrl
if __name__=="__main__":
    import sys , math
    _translate = QtCore.QCoreApplication.translate
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    Form.setWindowTitle(_translate("Form", "Proyecto estadistica "))
    Form.resize(1200, 700)
    m=_modelo.Model()
    datos=m.connect()
    ex = _mcrtl.RootController(Form,datos)
    _frecuencias  = _frcCtrl.frecuences_ctrl(datos)
    #Form.show()
    #sys.exit(app.exec_())




