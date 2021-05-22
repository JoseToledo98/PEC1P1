class frecuences_ctrl:
    def __init__(self,datos):
        self.generos=[]
        self.edades=[]
        self.tiempos=[]
        self.edadesAccion=[]
        self.edadesCarreras=[]
        self.edadesClasicos=[]
        self.edadesDeportes=[]
        self.edadesRoles=[]
        self.edadesTiros=[]
        self.separacionDatos(datos)
        self.medianaEdades(self.edadesAccion,self.edadesCarreras,self.edadesClasicos,self.edadesDeportes,self.edadesRoles,self.edadesTiros)
        self.modasEdades(self.edadesAccion,self.edadesCarreras,self.edadesClasicos,self.edadesDeportes,self.edadesRoles,self.edadesTiros)
        self.varianzaEdades(self.edadesAccion,self.edadesCarreras,self.edadesClasicos,self.edadesDeportes,self.edadesRoles,self.edadesTiros)
        self.mediasEdades(self.edadesAccion,self.edadesCarreras,self.edadesClasicos,self.edadesDeportes,self.edadesRoles,self.edadesTiros)
        
    def separacionDatos(self,datos):
        
        for i in range(len(datos)):
            self.estado= datos[i].getJuega()=="No"
            if self.estado == False:
                
                self.estado=datos[i].getGenero()== "Accion y aventuras"
                if self.estado == True:
                    self.edadesAccion.append(float(datos[i].getEdad())) 

                self.estado=datos[i].getGenero()== "Carreras y vuelos"
                if self.estado == True:
                    self.edadesCarreras.append(float(datos[i].getEdad()))

                self.estado=datos[i].getGenero()== "Clasicos"
                if self.estado == True:
                    self.edadesClasicos.append(float(datos[i].getEdad())) 

                self.estado=datos[i].getGenero()== "Deportes"
                if self.estado == True:
                    self.edadesDeportes.append(float(datos[i].getEdad()))

                self.estado=datos[i].getGenero()== "Roles"
                if self.estado == True:
                    self.edadesRoles.append(float(datos[i].getEdad()))
                self.estado=datos[i].getGenero()== "Tiros"
                if self.estado == True:
                    self.edadesTiros.append(float(datos[i].getEdad()))    

    
    def mediasEdades(self,edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros):

        self.promAccion= self.calculoProm(edadesAccion)
        self.promCarreras= self.calculoProm(edadesCarreras)
        self.promClasicos= self.calculoProm(edadesClasicos)
        self.promDeportes= self.calculoProm(edadesDeportes)
        self.promRoles= self.calculoProm(edadesRoles)
        self.promTiros= self.calculoProm(edadesTiros)

        self.mediaGeoAcc=self.calculoMediaG(edadesAccion)
        self.mediaGeoCarr=self.calculoMediaG(edadesCarreras)
        self.mediaGeoCla=self.calculoMediaG(edadesClasicos)
        self.mediaGeoDep=self.calculoMediaG(edadesDeportes)
        self.mediaGeoRol=self.calculoMediaG(edadesRoles)
        self.mediaGeoTir=self.calculoMediaG(edadesTiros)        
        print( self.mediaGeoAcc," " ,self.mediaGeoCarr," " ,self.mediaGeoCla," " ,self.mediaGeoDep," " ,self.mediaGeoRol," " ,self.mediaGeoTir)
        self.TruncadaEdades(edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros,.20)
    def calculoMediaG(self, lista):
        import math
        self.mediaGeaometrica=math.pow((self.multiplicacionLista(lista))/((len(lista)-1)),1/(len(lista)-1))
        return self.mediaGeaometrica

    def calculoProm(self, lista):
        self.promedio=round((sum(lista))/(len(lista)-1),4)
        return self.promedio
    
    def multiplicacionLista(self, datos):
        self.resultado=1
        for i in range(len(datos)):
            self.resultado=self.resultado*datos[i]
        return self.resultado
    
    def TruncadaEdades(self,edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros,promedio):
        self.truncAcc=self.calcularTruncada(edadesAccion,promedio)
        self.truncCar=self.calcularTruncada(edadesCarreras,promedio)
        self.truncCla=self.calcularTruncada(edadesClasicos,promedio)
        self.truncDep=self.calcularTruncada(edadesDeportes,promedio)
        self.truncRol=self.calcularTruncada(edadesRoles,promedio)
        self.truncTir=self.calcularTruncada(edadesTiros,promedio)

        
    
    def calcularTruncada(self,lista,promedio):
        lista.sort()
        self.restar=len(lista)*promedio
        for i in range(int(self.restar)):
            lista.pop()
            lista.pop(0)
        self.resultado= self.calculoProm(lista)
        return self.resultado

    def medianaEdades(self,edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros): 
        self.medianaAcc=self.calculoMediana(edadesAccion)
        self.medianaCar=self.calculoMediana(edadesCarreras)
        self.medianaCla=self.calculoMediana(edadesClasicos)
        self.medianaDep=self.calculoMediana(edadesDeportes)
        self.medianaRol=self.calculoMediana(edadesRoles)
        self.meidianaTir=self.calculoMediana(edadesTiros)

    def calculoMediana(self,lista):
        self.modulo =len(lista)%2
        self.mediana=0.0
        if self.modulo == 0:
            self.meidana=((lista[int((len(lista)-1)/2)])+(lista[int((len(lista)-1)/2)+1]))/2
        else:
            self.meidana=lista[int((len(lista)-1)/2)]
        return self.mediana

    def modasEdades(self,edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros):
        self.modaAccion= self.calculoModa(edadesAccion)
        self.modaCarreras= self.calculoModa(edadesCarreras)
        self.modaClasicos= self.calculoModa(edadesClasicos)
        self.modaDeportes= self.calculoModa(edadesDeportes)
        self.modaRoles= self.calculoModa(edadesRoles)
        self.modaTiros= self.calculoModa(edadesTiros)
        

    def calculoModa(self,lista):
        from statistics import mode
        self.moda=mode(lista)
        return self.moda

    def varianzaEdades(self,edadesAccion,edadesCarreras,edadesClasicos,edadesDeportes,edadesRoles,edadesTiros):
        self.varianzaAccion=self.calculoVarianza(edadesAccion)
        self.varianzaCarreras=self.calculoVarianza(edadesCarreras)
        self.varianzaClasicos=self.calculoVarianza(edadesClasicos)
        self.varianzaDeportes=self.calculoVarianza(edadesDeportes)
        self.varianzaRoles=self.calculoVarianza(edadesRoles)
        self.varianzaTiros=self.calculoVarianza(edadesTiros)
        self.desviacionEstandarEdades(self.varianzaAccion,self.varianzaCarreras,self.varianzaClasicos,self.varianzaDeportes,self.varianzaRoles,self.varianzaTiros)
    
    def calculoVarianza(self,lista):
        import math
        self.resultado=0.0
        for i in range(len(lista)-1):
            self.promedio=self.calculoProm(lista)
            self.error=lista[i]-self.promedio
            self.resultado=self.resultado+(math.pow((self.error-self.promedio),2))
        self.resultado=self.resultado/(len(lista)-1)
        print("resultado: ",self.resultado)
        return self.resultado        
    
    def desviacionEstandarEdades(self,varianzaAccion,varianzaCarreras,varianzaClasicos,varianzaDeportes,varianzaRoles,varianzaTiros):
        self.desviacionAcc=self.calculoDesviacion(varianzaAccion)
        self.desviacionCar=self.calculoDesviacion(varianzaCarreras)
        self.desviacionCla=self.calculoDesviacion(varianzaClasicos)
        self.desviacionDep=self.calculoDesviacion(varianzaDeportes)
        self.desviacionRol=self.calculoDesviacion(varianzaRoles)
        self.desviaciontir=self.calculoDesviacion(varianzaTiros)
    
    def calculoDesviacion(self,varianza):
        from math import pow
        print("varianza: ",varianza)
        self.resultado= pow(varianza,1/2)
        return self.resultado