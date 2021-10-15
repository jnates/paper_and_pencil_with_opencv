from PIL import Image
from PIL import ImageTk
from tkinter import Tk, Label, Frame, PhotoImage, Button, Toplevel, messagebox
from tkinter import ttk


class Interfaz():

    window = None

    def __init__(self):

        self.window = Tk()
        self.window.title("VISIÓN POR COMPUTADORA")
        self.window.resizable(False,False)
        self.window.geometry("1000x800")
        self.window.config(bg="beige",bd=10,relief="ridge")

        #Centered window calculation

        window_Width   = self.window.winfo_reqwidth()
        window_Height  = self.window.winfo_reqheight()
        position_right = int(window_Width*3 - window_Width/2)
        position_down  = int(window_Height  - window_Height/2)
        
        self.window.geometry("+{}+{}".format(position_right, position_down))

        menu = Label(self.window, text="MENU", bg= "beige", font=("Helvetica",9, "bold"))
        menu.place(x=480,y=280)

        typeautor = Label(self.window, text="ELABORADO POR:", bg="beige",font=("Helvetica",9, "bold"))
        typeautor.place(x=620,y=730)

        autor = Label(self.window, text="ING.JUAN DAVID NATES HUERTAS", bg="beige",font=("Helvetica",9, "bold"))
        autor.place(x=725, y=730)
        
        imagen = PhotoImage(file="./img/logo_tecnosoft.png")

        button_type = ttk.Style()
        button_type.configure("Peligro.TButton", foreground="#ff0000")
        button_type.map("Peligro.TButton", foreground=[("active", "#FFA500")])
        button = ttk.Button(text="Tablero en Cámara", style="Peligro.TButton",width=20)
        button.place(x=440, y=450)

        logo = Label(self.window, image=imagen,bg="beige")
        logo.place(x=10,y=2,width=260,height=240)

        self.window.mainloop()

if __name__ == '__main__':
    proyecto = Interfaz()

