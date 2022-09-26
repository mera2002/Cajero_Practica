
from queue import Empty
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

"Integrantes:"
# Merary Julissa Araujo Velasquez
# Nathaly Sarai Rodriguez Silva

#funcion para calcular el precio del producto y sus descuentos respectivos
def calcular_descuentos():
   try:
        precio = float(caja2.get())
        cantidad = int(caja3.get())
        cobro = precio * cantidad
        metodo_de_pago = cambo.get()
        descuentoporcentaje = Empty
        calculardescuento = Empty
        total = Empty
       
       #metodo if que nos ayudara a denifir los descuento segun sea el metodo de pago
        if metodo_de_pago == "":
            messagebox.showerror("Cajero","Seleccione un método de pago")
        
        #si paga con tarjeta de credito se hara un descuento del 20%
        elif metodo_de_pago == "Con Tarjeta":
            descuentoporcentaje = "20%"
            calculardescuento = cobro*0.20
            total = cobro-calculardescuento
            messagebox.showinfo("Cajero",f"La cantidad de producto es: {cantidad}, El precio del producto es: ${precio}, El metodo de pago es: {metodo_de_pago}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
       
       #si paga en efectivo se hara un descuento del 10%
        elif metodo_de_pago == "En Efectivo":
        #si el valor de la compra es menor a 20, no se hara ningun descuento
            if cobro < 20:
                descuentoporcentaje = "sin descuento"
                total = cobro
                messagebox.showinfo("Cajero",f"La cantidad de producto es: {cantidad}, El recio del producto es: ${precio}, El metodo de pago es: {metodo_de_pago}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
            
            else:
                descuentoporcentaje = "10%"
                calculardescuento = cobro*0.10
                total = cobro-calculardescuento
                messagebox.showinfo("Cajero",f"La cantidad de producto es: {cantidad}, El Precio del producto es: ${precio}, El metodo de pago es: {metodo_de_pago}, El descuento es: {descuentoporcentaje}, El total es: ${total}")
    
    #si el usuario no llena los datos no se cumplira ningun paraemetro y mostrara un mensaje        
   except:
        messagebox.showerror("Cajero","¡Llene todos los campos!, por favor")

#funcion salir, permitira al usuario salir de la app o cancelar el proceso 
def salir():
    mensaje = messagebox.askquestion("Salir","¿Desea salir?")
    if mensaje == "yes":
        interfaz.destroy()
    else:
        pass

#Formulario principal 
interfaz = Tk()
interfaz.title("Cajero") #Nombre del formulario que se le presentara al usuario
interfaz.resizable(0,0)
interfaz.configure(background='Pink') #Definicion del color del formulario que se le presentara al usuario

#definicion de las medidas 
ancho_ventana = 500 
alto_ventana = 300

x_ventana = interfaz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = interfaz.winfo_screenheight() // 2 - alto_ventana // 2

formulario = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
interfaz.geometry(formulario)



#Definicion de controles, textos y mensajes a mostrar en la app
txt0 = Label(interfaz,text="¡GRACIAS POR SU COMPRA!",bg='Plum',font='Luminari 14 bold')
txt3 = Label(interfaz,text="(seleccione) un método pago: ",bg='Pink',font='Bradley 10 bold')
txt1 = Label(interfaz,text=" Ingrese el precio del producto: ",bg='Pink',font='Bradley 9 bold')
caja2 = Entry(interfaz)
txt2 = Label(interfaz,text="Ingrese la cantidad de producto: ",bg='Pink',font='Bradley 9 bold')
caja3 = Entry(interfaz)
cambo = Combobox(interfaz,state="readonly")
cambo['values']=("En Efectivo","Con Tarjeta")
btn1 = Button(interfaz,text ="Comprar",command=calcular_descuentos,bg="Violet",font='Luminari 10 bold',fg="black")
btn2 = Button(interfaz,text ="Cancelar",command=salir,bg="Violet",font='Luminari 10 bold',fg="black")

#Mostrar controles, textos y mensajes antes definidos
txt2.place(x = 30,y = 70)
caja3.place(x = 220,y = 70,width = 150,height = 20)
txt1.place(x = 40,y = 50)
caja2.place(x = 220,y = 50,width = 150,height = 30)
cambo.place(x = 130,y = 140,width = 150)
txt3.place(x= 150,y= 120)
btn1.place(x = 50,y = 180,width = 150,height = 40)
btn2.place(x = 220,y = 180,width = 150,height = 40)
txt0.pack()
interfaz.mainloop()