from tkinter.constants import N
import mysql.connector
from datetime import datetime

class Client:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="45237823", database="compradores")

    def __str__(self):
        datos=self.consulta()        
        aux=""
        return aux

    def dateNow(self):
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt = now.strftime("%d/%m/%Y")
        return dt


    def DeTable (self,ID):
        cur = self.cnn.cursor()
        sql='''DROP TABLE `{}`;'''.format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n
    
    def STab (self, ID):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM `{}`".format(ID))
        datos = cur.fetchall()
        cur.close()    
        return datos

    def newTable (self,ID ):
        cur = self.cnn.cursor()
        sql= "CREATE TABLE `compradores`.`{}` (`N` INT NOT NULL AUTO_INCREMENT,`Fecha` DATE NULL,`Remision` VARCHAR(15) NULL,`F_E` VARCHAR(15) NULL,`Cant` INT NULL,`Cl_Fisc` VARCHAR(15) NULL,`VR_Fra` VARCHAR(15) NULL,`Fecha_Venc` DATE NULL,`R_Caja1` VARCHAR(15) NULL,`Fecha_a1` DATE NULL,`Abono1` INT NULL,`R_caja2` VARCHAR(15) NULL,`Fecha_a2` DATE NULL,`Abono2` INT NULL,`VF_Fra` VARCHAR(15) NULL,`VR_Acum` INT NULL,PRIMARY KEY (`N`),UNIQUE INDEX `N_UNIQUE` (`N` ASC) VISIBLE);".format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        
        return n
    def B_esp(self,n,db,es):
        cur = self.cnn.cursor()
        sql = "SELECT {} FROM {} WHERE N = {}".format(es,db,n)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos


    def consulta (self,s):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM {}".format(s)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos
    def maxI (self,s):
        if s == "sa":
            cur = self.cnn.cursor()
            sql= "select N from facturasa where N = (select MAX(N) from facturasa); ".format(s)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
        if s == "sb":
            cur = self.cnn.cursor()
            sql= "select N from facturasb where N = (select MAX(N) from facturasb); ".format(s)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
        return datos
    def resum (self,na,ini,end):
            cur = self.cnn.cursor()
            sql="SELECT * FROM `compradores`.`{}` WHERE Fecha >= '{}' AND Fecha <= '{}';".format(na,ini,end)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
            return datos

    def buscar (self, Id,k):
        if k == 1:
            cur = self.cnn.cursor()
            sql= "SELECT * FROM resibo WHERE RC = '{}'".format(Id)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
        else:
            cur = self.cnn.cursor()
            sql= "SELECT * FROM s_vc WHERE ID = '{}'".format(Id)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
            
        return datos

    def insfa(self,ID,N,F,V,D,s):

        if s == "sa":
            cur = self.cnn.cursor()
           # sql='''INSERT INTO `facturasa` (`ID`, `Nombre`, `Fecha`, `Valor`, `Descripcion`) VALUES ('1', 'asd', 'asds', '12', '456');'''
            sql='''INSERT INTO `facturasa` (`ID`, `Nombre`, `Fecha`, `Valor`, `Descripcion`) VALUES ('{}','{}','{}','{}','{}');'''.format(ID,N,F,V,D)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()

        if s == "sb":
            cur = self.cnn.cursor()
            sql='''INSERT INTO `facturasb` (`ID`, `Nombre`, `Fecha`, `Valor`, `Descripcion`) VALUES ('{}','{}','{}','{}',{});'''.format(ID,N,F,V,D)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()


        return n    

    def insTab (self,Nombre,FEc,Rems,F_E,Can,cl_f,Vr_fr,Fec_ven,VR_Ff):

        dt= str(self.dateNow())
        cur = self.cnn.cursor()
        sql='''INSERT INTO `compradores`.`{}` (`Fecha`, `Remision`, `F_E`, `Cant`, `Cl_Fisc`, `VR_Fra`, `Fecha_Venc`,  `VF_Fra`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(Nombre,FEc,Rems,F_E,Can,cl_f,Vr_fr,Fec_ven,VR_Ff)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def insertat (self,Nombre, ID,Cel, Valor,des ):
        cur = self.cnn.cursor()
        sql='''INSERT INTO `s_vc` (`Nombre`, `ID`, `Celular`, `Des`, `Valor`) VALUES ('{}', '{}', '{}', '{}', '{}');'''.format(Nombre,ID,Cel,des,Valor)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina (self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM s_vc WHERE ID = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        
        return n   

    def modifica (self, ID,Valor,s ):
        cur = self.cnn.cursor()
        sql='''UPDATE `{}` SET `Valor` = '{}' WHERE `ID`= {}'''.format(s,Valor,ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
    def abono1 (self, Nom,R_c1,F_1,A1,VR_fac,Var_ac,N ):
        cur = self.cnn.cursor()
        sql='''UPDATE `compradores`.`{}` SET `R_Caja1` = '{}', `Fecha_a1` = '{}', `Abono1` = '{}', `VF_Fra` = '{}', `VR_Acum` = '{}' WHERE (`N` = '{}');'''.format(Nom,R_c1,F_1,A1,VR_fac,Var_ac,N )
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
    def abono2 (self, Nom,R_c1,F_1,A1,VR_fac,Var_ac,N ):
        cur = self.cnn.cursor()
        sql='''UPDATE `compradores`.`{}` SET `R_Caja2` = '{}', `Fecha_a2` = '{}', `Abono2` = '{}', `VF_Fra` = '{}', `VR_Acum` = '{}' WHERE (`N` = '{}');'''.format(Nom,R_c1,F_1,A1,VR_fac,Var_ac,N )
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
    def acumula(self,Name,N,Val):
        cur = self.cnn.cursor()
        sql='''UPDATE `compradores`.`{}` SET `VR_Acum` = '{}' WHERE (`N` = '{}');'''.format(Name,Val,N)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()

        cur = self.cnn.cursor()
        sql='''UPDATE `compradores`.`s_vc` SET `Valor` = '{}' WHERE (`Nombre` = '{}');'''.format(Val,Name)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()

        return n   
