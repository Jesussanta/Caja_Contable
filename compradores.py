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
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
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

    def newTable (self,ID,Valor,des ):
        cur = self.cnn.cursor()
        sql=''' CREATE TABLE `{}` (`#` INT NOT NULL AUTO_INCREMENT,`ID` INT NOT NULL, `Fecha` TEXT NOT NULL, `Valor` FLOAT NOT NULL,`Descripcion` TEXT,PRIMARY KEY (`#`), UNIQUE INDEX `#_UNIQUE` (`#` ASC) VISIBLE);'''.format(ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        self.insTab(ID,Valor,des)
        return n

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

    def buscar (self, Id,s,k):
        if k == 1:
            cur = self.cnn.cursor()
            sql= "SELECT * FROM {} WHERE N = {}".format(s,Id)
            cur.execute(sql)
            datos = cur.fetchone()
            cur.close()    
        else:
            cur = self.cnn.cursor()
            sql= "SELECT * FROM {} WHERE ID = {}".format(s,Id)
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


    
    def insTab (self,ID, Valor,des ):

        dt= str(self.dateNow())
        cur = self.cnn.cursor()
        sql='''INSERT INTO `{}` (`ID`,`Fecha`, `Valor`, `Descripcion`) VALUES ('{}','{}', '{}', '{}');'''.format(ID, ID, dt, Valor,des)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def inserta (self,ID, Nombre, Valor,s,des ):
        cur = self.cnn.cursor()
        sql='''INSERT INTO `{}` (`ID`, `Nombre`, `Valor`, `Descrip`) VALUES ('{}', '{}', '{}', '{}')'''.format(s,ID, Nombre, Valor,des)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina (self,Id,s):
        cur = self.cnn.cursor()
        sql='''DELETE FROM {} WHERE ID = {}'''.format(s,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        self.DeTable(Id)
        return n   

    def modifica (self, ID,Valor,s ):
        cur = self.cnn.cursor()
        sql='''UPDATE `{}` SET `Valor` = '{}' WHERE `ID`= {}'''.format(s,Valor,ID)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
