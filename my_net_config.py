import os
from tkinter import *
import time
import sys


def enable_ethernet():
    os.system("netsh interface set interface Wi-Fi admin=disable")
    os.system("netsh interface set interface Ethernet admin=enable")
    print("INTERNET POR CABLE HABILITADO")
    print("EL PROGRAMA SE CERRARA AUTOMATICAMENTE EN 2 SEGUNDOS ...")
    time.sleep(2)
    sys.exit()
	

def enable_wifi():
    os.system("netsh interface set interface Ethernet admin=disable")
    os.system("netsh interface set interface Wi-Fi admin=enable")
    print("INTERNET POR WI-FI HABILITADO")
    print("EL PROGRAMA SE CERRARA AUTOMATICAMENTE EN 2 SEGUNDOS ...")
    time.sleep(2)
    sys.exit()


if __name__ == "__main__":

    os.system("netsh interface show interface")

    raiz = Tk()
    raiz.title("CONFIGURACION DE TU ACCESO A INTERNET")
    raiz.geometry("660x400+550+250")
    raiz.resizable(False, False)
    raiz.config(bg="blue")
    miFrame=Frame()
    miFrame.pack()
    miFrame.config(bg='#0059b3')
    miFrame.config(width="660", height="400")

    miLabel=Label(miFrame, text="BIENVENIDO")
    miLabel.config(bg='#0059ff', font=("Arial", 30, 'bold'), fg="white")
    miLabel.place(x=200, y=20)

    miLabel=Label(miFrame, text="POR FAVOR, SELECCIONA TU ACCESO A INTERNET:")
    miLabel.config(bg='#0059b3', font=("Arial", 16, 'bold'), fg="white")
    miLabel.place(x=50, y=100)

    miBoton_cable=Button(raiz, text="CABLE")
    miBoton_cable.place(x=50, y=150)
    miBoton_cable.config(width="15", height="3")
    miBoton_cable.config(fg="black", font=("Arial", 20, 'bold'), cursor="hand2")
    miBoton_cable.config(command=enable_ethernet)

    miBoton_wifi=Button(raiz, text="WI-FI")
    miBoton_wifi.place(x=350, y=150)
    miBoton_wifi.config(width="15", height="3")
    miBoton_wifi.config(fg="black", font=("Arial", 20, 'bold'), cursor="hand2")
    miBoton_wifi.config(command=enable_wifi)

    dia_hoy = time.strftime("%A, %d de %B del %Y")
    miLabel=Label(miFrame, text="La fecha de hoy es:  " + dia_hoy)
    miLabel.config(bg='#0059b3', font=("Arial", 12), fg="white")
    miLabel.place(x=50, y=320)

    raiz.mainloop()

