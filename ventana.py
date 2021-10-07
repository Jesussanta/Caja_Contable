from logging import disable
from tkinter import *
from tkinter import ttk
from fpdf import FPDF
from mysql.connector.utils import validate_normalized_unicode_string
from compradores import * 

class Ventana(Frame):
    
    Seller = Client()
    So = "s_vc"
     
    def __init__(self, master=None):
        
        super().__init__(master,width=1580, height=720)
        self.master = master
        self.pack()
        self.create_widgets()
        #self.habili(5)

    def datos(self,k):
        datos = self.Seller.consulta(k)
        #print(datos)
        self.cretGrip(datos,2)

    def addWin(self):
        winAdd = Toplevel(self)
        winAdd.geometry("350x400+500+200")
        winAdd.title("Añadir")
        winAdd.resizable(False,False)
        va=95
        vb=50
        frame2 = Frame(winAdd,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=350, height=400)                        
        addName=Label(winAdd, text="Nombre",bg="#2F3E45",fg="white")
        addName.place(x=va,y=20+vb)     
        self.EnName=Entry(frame2)
        self.EnName.place(x=va,y=41+vb,width=160, height=20)    
        addID=Label(winAdd, text="ID",bg="#2F3E45",fg="white")
        addID.place(x=va,y=70+vb)     
        self.EnID=Entry(frame2)
        self.EnID.place(x=va,y=91+vb,width=160, height=20)    
        addCel=Label(winAdd, text="Celular",bg="#2F3E45",fg="white")
        addCel.place(x=va,y=120+vb)     
        self.EnCel=Entry(frame2)
        self.EnCel.place(x=va,y=141+vb,width=160, height=20)   
        addVal=Label(winAdd, text="Valor",bg="#2F3E45",fg="white")
        addVal.place(x=va,y=170+vb)     
        self.EnVal=Entry(frame2)
        self.EnVal.place(x=va,y=191+vb,width=160, height=20)  
        self.winAdd=winAdd
        addDes=Label(winAdd, text="Descripcion",bg="#2F3E45",fg="white")
        addDes.place(x=va,y=220+vb)     
        self.EnDes=Entry(frame2)
        self.EnDes.place(x=va,y=241+vb,width=160, height=20)  
        self.EnName.focus()
        
        self.winAdd=winAdd
        addBot=Button(winAdd, text="Agregar",command=self.addWinBot,bg="#05867B", fg="white",relief=FLAT)
        addBot.place(x=va+50,y=280+vb,width=60, height=30) 
    def addWinBot(self):
        nam=self.EnName.get()
        print(self.EnName.get() + "-"+self.EnID.get()+ "-"+self.EnCel.get()+ "-"+self.EnVal.get())
        if len(nam.split(" ")) > 1:
            nam=nam.replace(" ","_")
        nam=nam.lower()
        self.Seller.insertat(nam,self.EnID.get(),self.EnCel.get(),self.EnVal.get(),self.EnDes.get())
        self.Seller.newTable(nam)
        self.datos("s_vc")
        self.winAdd.destroy()
        
    def delWin(self):
        winDel = Toplevel(self)
        winDel.geometry("350x400")
        winDel.title("Eliminar")
        winDel.resizable(False,False)
        va=95
        vb=80
        frame2 = Frame(winDel,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=350, height=400)                    
        delLab=Label(winDel, text="Se eliminara todo registro de forma permanente \n asi como el historial de facturas. ",bg="#2F3E45",fg="white")    
        delLab.place(x=va-35,y=vb-30)  
        delName=Label(winDel, text="Nombre",bg="#2F3E45",fg="white")
        delName.place(x=va,y=20+vb)     
        self.deName=Entry(frame2)
        self.deName.place(x=va,y=41+vb,width=160, height=20)    
        delID=Label(winDel, text="ID",bg="#2F3E45",fg="white")
        delID.place(x=va,y=70+vb)     
        self.delID=Entry(frame2)
        self.delID.place(x=va,y=91+vb,width=160, height=20)    
        self.winDel=winDel
        self.deName.focus()
        addBot=Button(winDel, text="Aceptar",command=self.delWinBot,bg="#05867B", fg="white",relief=FLAT)
        addBot.place(x=va+50,y=280,width=60, height=30) 
    def delWinBot(self):
        nam=self.deName.get()
        if len(nam.split(" ")) > 1:
            nam=nam.replace(" ","_")
        nam=nam.lower()
        print(nam)
        self.Seller.elimina(self.delID.get())
        self.Seller.DeTable(nam)
        #self.clGrip()
        self.datos("s_vc")
        self.winDel.destroy()
    
    def sehWin(self):
        winSeh = Toplevel(self)
        winSeh.geometry("350x400")
        winSeh.title("Buscar")
        winSeh.resizable(False,False)
        va=95
        vb=80
        frame2 = Frame(winSeh,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=350, height=400)                    
        seLab=Label(winSeh, text="Escribir ID de factura o Nombre de cliente. ",bg="#2F3E45",fg="white")    
        seLab.place(x=va-35,y=vb-30)  
        self.seName=Entry(frame2)
        self.seName.place(x=va,y=41+vb,width=160, height=20)    
        self.winSeh=winSeh
        addBot=Button(winSeh, text="Todo",command=self.seWinBot,bg="#05867B", fg="white",relief=FLAT)
        addBot.place(x=va,y=280,width=60, height=30) 
        seBot=Button(winSeh, text="Cliente",command=self.seWinBot1,bg="#05867B", fg="white",relief=FLAT)
        seBot.place(x=va+90,y=280,width=60, height=30) 
        self.seName.focus()

    def seWinBot(self):
        nam=self.seName.get()
        if len(nam.split(" ")) > 1:
                nam=nam.replace(" ","_")
        nam=nam.lower()
        self.namer=nam
        self.resum()
        self.winSeh.destroy()
               
    def seWinBot1(self):
        nam=self.seName.get()
        if nam == '':
            self.datos("s_vc")
            self.winSeh.destroy()
        
        else:        
            if len(nam.split(" ")) > 1:
                nam=nam.replace(" ","_")
            nam=nam.lower()
            datos = self.Seller.STab(nam)
            self.cretGrip(datos,3)
            self.winSeh.destroy()
    def resum(self):
        winRes = Toplevel(self)
        winRes.geometry("350x400")
        winRes.title("Resumen")
        winRes.resizable(False,False)
        va=95
        vb=80
        frame2 = Frame(winRes,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=350, height=400)                    
        delLab=Label(winRes, text="Ingresar fecha inicial y final \n para la busqueda (yyyy/mm/dd)",bg="#2F3E45",fg="white")    
        delLab.place(x=va-35,y=vb-30)  
        serStart=Label(winRes, text="Inicio",bg="#2F3E45",fg="white")
        serStart.place(x=va,y=20+vb)     
        self.seSt=Entry(frame2)
        self.seSt.place(x=va,y=41+vb,width=160, height=20)    
        delID=Label(winRes, text="Fin",bg="#2F3E45",fg="white")
        delID.place(x=va,y=70+vb)     
        self.seEnd=Entry(frame2)
        self.seEnd.place(x=va,y=91+vb,width=160, height=20)    
        self.winRes=winRes
        self.seSt.focus()
        addBot=Button(winRes, text="Busca",command=self.ResWinBot,bg="#05867B", fg="white",relief=FLAT)
        addBot.place(x=va+50,y=280,width=60, height=30) 

    def ResWinBot(self):
        ini=self.seSt.get()
        end=self.seEnd.get()
        print(self.namer+ini+end)
        datos = self.Seller.resum(self.namer,str(ini),str(end))
        self.cretGrip(datos,3)
        self.winRes.destroy()





    def chaWin(self):
        winCha = Toplevel(self)
        winCha.geometry("350x400")
        winCha.title("Buscar")
        winCha.resizable(False,False)
        va=95
        vb=80
        frame2 = Frame(winCha,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=350, height=400)                    
        seLab=Label(winCha, text="Escribir el nombre de cliente. \n  y seleccione la accion a realizar. ",bg="#2F3E45",fg="white")    
        seLab.place(x=va-10,y=vb-30)  
        self.chaName=Entry(frame2)
        self.chaName.place(x=va-20,y=41+vb,width=200, height=20)    
        self.winCha=winCha        
        self.chaName.focus()
        chaBot=Button(winCha, text="Nuevo",command=self.chaWinBot,bg="#05867B", fg="white",relief=FLAT)
        chaBot.place(x=va+90,y=280,width=60, height=30) 
        chaBot1=Button(winCha, text="Abonos1",command=self.chaWinBot1,bg="#05867B", fg="white",relief=FLAT)
        chaBot1.place(x=va,y=260,width=60, height=30) 
        chaBot2=Button(winCha, text="Abonos2",command=self.chaWinBot2,bg="#05867B", fg="white",relief=FLAT)
        chaBot2.place(x=va,y=300,width=60, height=30) 
    def win_ab(self,c):
        #crear metodo
        winAb = Toplevel(self)
        winAb.geometry("580x100")
        winAb.title("Abono")
        winAb.resizable(False,False)
        frame2 = Frame(winAb,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=580, height=200)       
        v=20
        nam=self.chaName.get()
        if c==1:
            chaLab6=Label(winAb, text="N",bg="#2F3E45",fg="white")    
            chaLab6.place(x=v,y=10)  
            self.gri_N=Entry(frame2)
            self.gri_N.place(x=v,y=50,width=100, height=20)   
            
            chaLab7=Label(winAb, text="R_caja1",bg="#2F3E45",fg="white")    
            chaLab7.place(x=110+v,y=10)  
            self.griRC_1=Entry(frame2)
            self.griRC_1.place(x=110+v,y=50,width=100, height=20)   

            chaLab8=Label(winAb, text="Fecha_a1 ",bg="#2F3E45",fg="white")    
            chaLab8.place(x=220+v,y=10)  
            self.griFa_1=Entry(frame2)
            self.griFa_1.place(x=220+v,y=50,width=100, height=20)   
            chaLab9=Label(winAb, text="V Abono1",bg="#2F3E45",fg="white")    
            chaLab9.place(x=330+v,y=10)  
            self.V_A=Entry(frame2)
            self.V_A.place(x=330+v,y=50,width=100, height=20)     
            cha=Button(winAb, text="Aplicar",command=self.cha,bg="#05867B", fg="white",relief=FLAT)
            cha.place(x=460+v,y=30,width=60, height=30) 

            
        if c ==2:
            chaLab6=Label(winAb, text="N",bg="#2F3E45",fg="white")    
            chaLab6.place(x=v,y=10)  
            self.gri_N=Entry(frame2)
            self.gri_N.place(x=v,y=50,width=100, height=20)   
            
            chaLab7=Label(winAb, text="R_caja2",bg="#2F3E45",fg="white")    
            chaLab7.place(x=110+v,y=10)  
            self.griRC_1=Entry(frame2)
            self.griRC_1.place(x=110+v,y=50,width=100, height=20)   

            chaLab8=Label(winAb, text="Fecha_a2 ",bg="#2F3E45",fg="white")    
            chaLab8.place(x=220+v,y=10)  
            self.griFa_1=Entry(frame2)
            self.griFa_1.place(x=220+v,y=50,width=100, height=20)   
            chaLab9=Label(winAb, text="V Abono2",bg="#2F3E45",fg="white")    
            chaLab9.place(x=330+v,y=10)  
            self.V_A=Entry(frame2)
            self.V_A.place(x=330+v,y=50,width=100, height=20)   
            cha2=Button(winAb, text="Aplicar",command=self.cha2,bg="#05867B", fg="white",relief=FLAT)
            cha2.place(x=460+v,y=30,width=60, height=30) 

              
        self.winAb = winAb     
    def cha(self):
        N=self.gri_N.get()
        if N == "1" :
            v_ac=0
        else:
            nv = int(N)-1
            vac=self.Seller.B_esp(str(nv),self.nam,"VR_Acum")
            if vac[0][0] is None:
                v_ac=0
            else:
                v_ac=vac[0][0]
        
        v_f=self.Seller.B_esp(N,self.nam,"VF_Fra")
        v_fac=v_f[0][0]
        
        ab1=int(self.V_A.get())
        v_fac=int(v_fac)-ab1
        VAC=int(v_ac)+int(v_fac)
        self.Seller.abono1(self.nam,self.griRC_1.get(),self.griFa_1.get(),str(ab1),str(v_fac),str(VAC),N)
        datos = self.Seller.STab(self.nam)
        self.cretGrip(datos,3)
        print(datos)
        self.acumlate(N)
        self.winAb.destroy()

    def cha2 (self):
        N=self.gri_N.get()
        if N == "1" :
            v_ac=0
        else:
            nv = int(N)-1
            vac=self.Seller.B_esp(str(nv),self.nam,"VR_Acum")
            if vac[0][0] is None:
                v_ac=0
            else:
                v_ac=vac[0][0]
       
        v_f=self.Seller.B_esp(N,self.nam,"VF_Fra")
        v_fac=v_f[0][0]
        
        ab1=int(self.V_A.get())
        v_fac=int(v_fac)-ab1
        VAC=int(v_ac)+int(v_fac)
        self.Seller.abono2(self.nam,self.griRC_1.get(),self.griFa_1.get(),str(ab1),str(v_fac),str(VAC),N)
        datos = self.Seller.STab(self.nam)
        self.cretGrip(datos,3)
        print(datos)
        self.acumlate(N)
        self.winAb.destroy()
    def chaWinBot2(self):
        nam=self.chaName.get()
        if len(nam.split(" ")) > 1:
            nam=nam.replace(" ","_")
        nam=nam.lower()
        self.nam=nam
        datos = self.Seller.STab(nam)
        self.cretGrip(datos,3)
        self.win_ab(2)
        self.winCha.destroy()
    def chaWinBot1(self):
        nam=self.chaName.get()
        if len(nam.split(" ")) > 1:
            nam=nam.replace(" ","_")
        nam=nam.lower()
        self.nam=nam
        datos = self.Seller.STab(nam)
        
        self.cretGrip(datos,3)
        self.win_ab(1)
        self.winCha.destroy()
    def chaWinBot(self):
        nam=self.chaName.get()
        if len(nam.split(" ")) > 1:
            nam=nam.replace(" ","_")
        nam=nam.lower()
        self.nam=nam
        datos = self.Seller.STab(nam)
        self.cretGrip(datos,3)
        print(datos)
        self.gripWin()
        self.winCha.destroy()
    def gripWin(self):
        winGrip = Toplevel(self)
        winGrip.geometry("900x100")
        winGrip.title("Nueva Factura")
        winGrip.resizable(False,False)
        frame2 = Frame(winGrip,bg="#2F3E45" )
        frame2.place(x=0,y=0,width=1580, height=200)       
        v=20
        chaLab=Label(winGrip, text="Fecha",bg="#2F3E45",fg="white")    
        chaLab.place(x=10,y=10)  
        self.griFech=Entry(frame2)
        self.griFech.place(x=10,y=50,width=100, height=20)    

        chaLab1=Label(winGrip, text="Remision",bg="#2F3E45",fg="white")    
        chaLab1.place(x=100+v,y=10)  
        self.griRe=Entry(frame2)
        self.griRe.place(x=100+v,y=50,width=100, height=20)    
          
        chaLab2=Label(winGrip, text="F_E",bg="#2F3E45",fg="white")    
        chaLab2.place(x=210+v,y=10)  
        self.griF_E=Entry(frame2)
        self.griF_E.place(x=210+v,y=50,width=100, height=20)    

        chaLab2=Label(winGrip, text="Cantidad",bg="#2F3E45",fg="white")    
        chaLab2.place(x=320+v,y=10)  
        self.gricant=Entry(frame2)
        self.gricant.place(x=320+v,y=50,width=100, height=20)   

        chaLab3=Label(winGrip, text="CL_Fisc",bg="#2F3E45",fg="white")    
        chaLab3.place(x=430+v,y=10)  
        self.griCL=Entry(frame2)
        self.griCL.place(x=430+v,y=50,width=100, height=20)    

        chaLab4=Label(winGrip, text="VR_Fra",bg="#2F3E45",fg="white")    
        chaLab4.place(x=540+v,y=10)  
        self.griVr=Entry(frame2)
        self.griVr.place(x=540+v,y=50,width=100, height=20)   
        
        chaLab5=Label(winGrip, text="Fecha_Venc",bg="#2F3E45",fg="white")    
        chaLab5.place(x=650+v,y=10)  
        self.griF_V=Entry(frame2)
        self.griF_V.place(x=650+v,y=50,width=100, height=20)   

        self.winGrip=winGrip     

        GripBot=Button(winGrip, text="Añadir",command=self.griWinBot,bg="#05867B", fg="white",relief=FLAT)
        GripBot.place(x=800,y=30,width=60, height=30) 
    
    def griWinBot(self):
               
        self.Seller.insTab(self.nam,self.griFech.get(),self.griRe.get(),self.griF_E.get(),self.gricant.get(),self.griCL.get(),self.griVr.get(),self.griF_V.get(),self.griVr.get())
        datos = self.Seller.STab(self.nam)
        
        N=str(datos[-1][0])
        if N != "1" :
            V=int(self.acumlate(N))
        else:
            V=0
        self.clGrip()
        
        datos = self.Seller.STab(self.nam)
        self.cretGrip(datos,3)
        self.winGrip.destroy()
    def acumlate(self,N):
        if N == "1" :
            v_ac=0
        else:
            nv = int(N)-1
            vac=self.Seller.B_esp(str(nv),self.nam,"VR_Acum")
            if vac[0][0] is None:
                v_ac=0
            else:
                v_ac=vac[0][0]
        self.Seller.acumula(self.nam,str(N),str(v_ac))
        return v_ac
    def habilib(self,bn):
        if bn == 1: #add
            self.btnAdd.configure(bg="#2F3E45",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 2: #del
            self.btnDelet.configure(bg="#2F3E45",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn == 3: #chan
            self.btnChan.configure(bg="#2F3E45",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
        elif bn ==4: #show
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#2F3E45",fg="white")
        else:
            self.btnAdd.configure(bg="#20292E",fg="white")
            self.btnDelet.configure(bg="#20292E",fg="white")
            self.btnChan.configure(bg="#20292E",fg="white")
            self.btnShow.configure(bg="#20292E",fg="white")
            #self.txtName.configure(state="normal")

    def clGrip(self):
        for i in self.grid.get_children():
            self.grid.delete(i)
    def cBox(self):
        self.txtName.delete(0,END)
        self.txtID.delete(0,END)
        self.txtValue.delete(0,END)
        self.txtDes.delete(0,END)
    def Busc(self):

        val=list(self.txtID.get())
        print(val)

        if val[0] == "f":
            self.f="factura"+self.So
            
            v=self.txtID.get()
            self.vf=v.split("-")
            print(self.vf)

            if self.txtID.get() == "f":
                
                self.datos(self.f)
                
            else:
                try:
                    print(self.f)
                    Fa = self.Seller.buscar(self.vf[1],self.f,1);

                    self.grid.heading("#0", text="# Factura", anchor=CENTER)
                    self.grid.heading("col1", text="ID ", anchor=CENTER)
                    self.grid.heading("col2", text="Nombre", anchor=CENTER)
                    self.grid.heading("col3", text="Fecha ", anchor=CENTER)
                    self.grid.heading("col4", text="Valor / Descripcion", anchor=CENTER)
                    self.grid.insert("",END, text= str(Fa[0]), values=(str(Fa[1]),str(Fa[2]),str(Fa[3]),str(Fa[4])))
                    self.grid.insert("",END, text= str(""), values=(str(""),str(""),str(""),Fa[5]))
                    print("6")
                except:
                    self.lbl4.config(text="ID inexistente.")
                    self.datos(self.f)
        else:
            
            if self.txtID.get() == "0":
                self.datos(self.So)
            else:
                try:
                    datos = self.Seller.STab(self.txtID.get());
                    self.grid.heading("col2", text="Fecha", anchor=CENTER)
                    for row in datos:
                       self.grid.insert("",END, text= row[0], values=(row[1],row[2],row[3],row[4]))
                    
                except:
                    self.lbl4.config(text="ID inexistente.")
                    self.datos(self.So)
    def impri(self,v1,v2,v3,n,i,Nu,d):
        
        f= str(self.So+ " - "+ str(Nu))
        da=self.Seller.dateNow()
        pdf = FPDF(orientation= 'P', unit= 'mm', format= 'A4')
        pdf.add_page()
        pdf.add_font('Popp', '', 'Poppins-Regular.ttf', uni=True)
        if self.So == "s_vc":
            pdf.image('F_vc.png', x = 10, y = 10, w = 190, h = 280)
        else:
            pdf.image('F_oc.png', x = 10, y = 10, w = 190, h = 280)
        pdf.set_font('Popp', '', 15)
        f1= str(self.So+ str(Nu))
        if len(f) > 8:
            pdf.text(x=160, y=40, txt=f)
        elif len(f) > 12:
            pdf.text(x=150, y=40, txt=f)
        else:
            pdf.text(x=165, y=40, txt=f)
            
        pdf.text(x=68, y= 82, txt=n)
        pdf.text(x=164, y= 125, txt=v1)
        pdf.text(x=40, y= 125, txt=i)
        pdf.text(x=97, y= 125, txt=n)
        pdf.text(x=164, y= 141, txt=v2)
        pdf.text(x=164, y= 157, txt=v3)
        pdf.text(x=40, y= 157, txt=i)
        pdf.text(x=97, y= 157, txt=n)
        pdf.text(x=164, y= 230, txt=v3)
        pdf.text(x=12, y= 62, txt=da)
        
        pdf.text(x=22, y= 242, txt="Descripcíon:")
        pdf.text(x=25, y= 250, txt=d)

        print(self.So)
        self.Seller.insfa(i,n,da,v3,d,self.So)
        
        t="./f/{}-{}.pdf".format(f1,i)
        pdf.output(t)
    def Val(self):
        
        vAc=self.Seller.buscar(self.txtID.get(),self.So,2)
        nV = self.txtValue.get()
        print(vAc)
        nR=str(float(vAc[3]) + float(nV))
        desc = self.txtDes.get()

        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(vAc[3]),str(vAc[4])))
        self.grid.insert("",END, text= str(""), values=(str(""),str(""),str(nV),desc))
        self.grid.insert("",END, text= str(vAc[0]), values=(str(vAc[1]),str(vAc[2]),str(nR)))
      
        self.Seller.modifica(vAc[1],str(nR),self.So)
        self.Seller.insTab(vAc[1],str(nR),desc)
        
        try:
            N=self.Seller.maxI(self.So)
            if N == NONE:
                v = 0
            else:
                a=list(N)
                print(a)
                v=int(a[0])+1
            
            self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),str(v),desc)
        
            
        except:
            self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),str(1),desc)
            
        
        self.lbl4.config(text="Valor actualizado.")
        #self.impri(str(vAc[3]),str(nV),str(nR),str(vAc[2]),str(vAc[1]),)

        self.cBox()
  
    def bAdd(self):
        self.addWin()
        self.habilib(1)  
    def bChan(self):        
        self.chaWin()
        self.clGrip()
        self.habilib(3)    
    def bDelet(self):
        self.delWin()
        self.habilib(2)   
      #  self.cBox()
    def bShow(self):
        self.sehWin()
        self.habilib(4)    
#        self.cBox()
    def bSave(self): 
        self.clGrip()
        self.gripb()
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        if self.cont ==1: #Add
            try:

                self.Seller.inserta(self.txtID.get(),self.txtName.get(),self.txtValue.get(),self.So,self.txtDes.get())
                self.Seller.newTable(self.txtID.get(),self.txtValue.get(),self.txtDes.get())
                self.lbl4.config(text="")
                self.cBox()
                self.datos(self.So)
                
            except:
                self.lbl4.config(text="Valores invalidos.")

        elif self.cont ==2: #Delet
            try:
                print("1")
                self.Seller.elimina(self.txtID.get(),self.So)
                print("1")
                self.lbl4.config(text="")
                self.cBox()
                self.datos(self.So)

            except:
                self.lbl4.config(text="ID inexistente.")


        elif self.cont == 3: #Show
            self.Busc()
            
        
        elif self.cont == 4: #Change
           try:
               self.lbl4.config(text="")
               self.Val()
           except:
               self.lbl4.config(text="ID Erronea.")
    
    def cretGrip(self,dat,k):
       
        if k ==1: #buscart
            #print("holos5")
            self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))        
            self.grid.column("#0",width=20)
            self.grid.column("col1",width=60, anchor=CENTER)
            self.grid.column("col2",width=100, anchor=CENTER)
            self.grid.column("col3",width=90, anchor=CENTER)
            self.grid.column("col4",width=100, anchor=CENTER)
            self.grid.column("col5",width=100, anchor=CENTER)

            self.grid.heading("#0", text="#", anchor=CENTER)
            self.grid.heading("col1", text="Nombre", anchor=CENTER) 
            self.grid.heading("col2", text="ID", anchor=CENTER)
            self.grid.heading("col3", text="Celular", anchor=CENTER)
            self.grid.heading("col4", text="Descripcíon", anchor=CENTER)
            self.grid.heading("col5", text="Valor", anchor=CENTER)
            self.grid.place(x=110,y=0,width=1460, height=715)
            self.grid.insert("",END, text= str(dat[0]), values=(str(dat[1]),str(dat[2]),str(dat[3]),str(dat[4]),str(dat[5])))
        elif k ==2:
            #print("holosasd5")
            self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))        
            self.grid.column("#0",width=20)
            self.grid.column("col1",width=60, anchor=CENTER)
            self.grid.column("col2",width=100, anchor=CENTER)
            self.grid.column("col3",width=90, anchor=CENTER)
            self.grid.column("col4",width=100, anchor=CENTER)
            self.grid.column("col5",width=100, anchor=CENTER)

            self.grid.heading("#0", text="#", anchor=CENTER)
            self.grid.heading("col1", text="Nombre", anchor=CENTER)
            self.grid.heading("col2", text="ID", anchor=CENTER)
            self.grid.heading("col3", text="Celular", anchor=CENTER)
            self.grid.heading("col4", text="Descripcíon", anchor=CENTER)
            self.grid.heading("col5", text="Valor", anchor=CENTER)
            self.grid.place(x=110,y=0,width=1460, height=715)
            for row in dat:
                self.grid.insert("",END, text= row[0], values=(row[1],row[2],row[3],row[4],row[5]))

        else:
            print("CHAOS16")        
            self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13","col14","col15"))        
            self.grid.column("#0",width=20)
            self.grid.column("col1",width=60, anchor=CENTER)
            self.grid.column("col2",width=90, anchor=CENTER)
            self.grid.column("col3",width=60, anchor=CENTER)
            self.grid.column("col4",width=90, anchor=CENTER)
            self.grid.column("col5",width=90, anchor=CENTER)
            self.grid.column("col6",width=60, anchor=CENTER)
            self.grid.column("col7",width=90, anchor=CENTER)
            self.grid.column("col8",width=60, anchor=CENTER)
            self.grid.column("col9",width=90, anchor=CENTER)
            self.grid.column("col10",width=90, anchor=CENTER)
            self.grid.column("col11",width=60, anchor=CENTER)
            self.grid.column("col12",width=90, anchor=CENTER)
            self.grid.column("col13",width=90, anchor=CENTER)
            self.grid.column("col14",width=90, anchor=CENTER)
            self.grid.column("col15",width=90, anchor=CENTER)
            
            self.grid.heading("#0", text="N", anchor=CENTER)
            self.grid.heading("col1", text="Fecha", anchor=CENTER)
            self.grid.heading("col2", text="Remision", anchor=CENTER)
            self.grid.heading("col3", text="F_E", anchor=CENTER)
            self.grid.heading("col4", text="Cant", anchor=CENTER)
            self.grid.heading("col5", text="Cl_Fisc", anchor=CENTER)
            self.grid.heading("col6", text="VR_Fra", anchor=CENTER)
            self.grid.heading("col7", text="Fecha_Venc", anchor=CENTER)
            self.grid.heading("col8", text="R_caja1", anchor=CENTER)
            self.grid.heading("col9", text="Fecha_a1", anchor=CENTER)
            self.grid.heading("col10", text="Abono1", anchor=CENTER)      
            self.grid.heading("col11", text="R_caja2", anchor=CENTER)
            self.grid.heading("col12", text="Fecha_a2", anchor=CENTER)
            self.grid.heading("col13", text="Abono2", anchor=CENTER)
            self.grid.heading("col14", text="VR/Fra", anchor=CENTER)
            self.grid.heading("col15", text="VR_Acum", anchor=CENTER)
            self.grid.place(x=110,y=0,width=1460, height=715)
            for row in dat:
                self.grid.insert("",END, text= str(row[0]), values=(str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13]),str(row[14]),str(row[15])))
    def create_widgets(self):
        frame1 = Frame(self, bg="#20292E")
        frame1.place(x=0,y=0,width=100, height=920)        
        v=80
        self.btnAdd=Button(frame1,text="Añadir", command=self.bAdd, bg="#20292E", fg="white",relief=FLAT, )
        self.btnAdd.place(x=0,y=140+v,width=110, height=30 )        
        self.btnDelet=Button(frame1,text="Eliminar", command=self.bDelet, bg="#20292E", fg="white",relief=FLAT)
        self.btnDelet.place(x=0,y=210+v,width=110, height=30)        
        self.btnShow=Button(frame1,text="Explorar", command=self.bShow, bg="#20292E", fg="white",relief=FLAT)
        self.btnShow.place(x=0,y=280+v,width=110, height=30)
        self.btnChan=Button(frame1,text="Modificar", command=self.bChan, bg="#20292E", fg="white",relief=FLAT)
        self.btnChan.place(x=0,y=650,width=110, height=30)    

        frame2 = Frame(self,bg="#2F3E45" )
        frame2.place(x=100,y=0,width=1480, height=920)                        
        #lbl1 = Label(frame2,text="ID: ",bg="#2F3E45",fg="white")        
        #lbl1.place(x=30,y=5+100)        
        #self.txtID=Entry(frame2)
        #self.txtID.place(x=30,y=25+100,width=160, height=20)                
        #lbl2 = Label(frame2,text="Nombre: ",bg="#2F3E45",fg="white")

V1 = Tk()
V1.wm_title("Caja")
app = Ventana(V1) 
app.mainloop()
    
        