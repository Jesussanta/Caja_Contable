from fpdf import FPDF
So = "s_vc"
def impri(nam,N,Fecha,Remision,F_E,Cant,Cl_Fisc,VR_Fra,Fecha_Venc,R_Caja1,Fecha_a1,Abono1,VF_Fra,VR_Acum):
        
        f= str()
        da=str(1)#date)
        pdf = FPDF(orientation= 'L', unit= 'mm', format= 'A4')
        pdf.add_page()
        pdf.add_font('Popp', '', 'Poppins-Regular.ttf', uni=True)
        if So == "s_vc":
            pdf.image('F_vc.jpeg', x = 0, y = 0, h = 210, w = 297)
        else:
            pdf.image('F_oc.jpeg', x = 0, y = 0, h = 210, w = 297)
        pdf.set_font('Popp', '', 15)
        f1= str(So)
        if len(R_Caja1) > 8:
            pdf.text(x=250, y=30, txt=R_Caja1)
        else:
            pdf.text(x=255, y=30, txt=R_Caja1)
            
        pdf.text(x=155, y= 30, txt=Fecha)
        pdf.text(x=50, y= 45, txt=nam)
        #pdf.text(x=255, y= 40, txt="3")
        #pdf.text(x=255, y= 25, txt="4")
        #Seller.insfa(i,n,da,v3,d,So)
        
        t="../../f/{}.pdf".format(R_Caja1)
        pdf.output(t)
N=4
datos=[(1, '1', '12', '15', 2, '12', '15', '2', 'asd2', '20/23', 11, '1111', 'sadas', 1, '0', 0), (2, 'asd', 'sadds', 'asd', 2123, 'qsdas', '45245', '12as', None, None, None, None, None, None, '45245', 0), (3, 'asd', 'dfgfd', 'dgfd', 65, 'fgf', '5675', 'sdfsdf', None, None, None, None, None, None, '5675', 0), (4, 'asd', 'asdas', 'asd', 65, '2599', '239', '236326', 'RC_0012', '15/78', 30, None, None, None, '209', 209), (5, '1', '2', '1', 21, '2', '12', '21', 'RC_001', '15/09', 5, 'RC_002', '15/9', 5, '2', 2), (6, '15', '12', '1', 54, '12', '1', '214', 'RC_003', '16/9', 0, None, None, None, '1', 3)]

print(datos[N-1])
N,Fecha,Remision,F_E,Cant,Cl_Fisc,VR_Fra,Fecha_Venc,R_Caja1,Fecha_a1,Abono1,R_caja2,Fecha_a2,Abono2,VF_Fra,VR_Acum=datos[N-1]

impri("Ptuo",N,Fecha,Remision,F_E,Cant,Cl_Fisc,VR_Fra,Fecha_Venc,R_Caja1,Fecha_a1,Abono1,VF_Fra,VR_Acum)

