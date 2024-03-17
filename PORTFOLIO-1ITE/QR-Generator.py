from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("QR kód generátor")
root.geometry("500x550")

def create_code():
    input_path = filedialog.asksaveasfilename(title="Uložit obrázek", 
        filetyp=(("PNG soubor", ".png"), ("Všechny soubory", "*.*")))
    
    if input_path:
        if input_path.endswith(".png"):
            #creates qr from entry box
            get_code = pyqrcode.create(my_entry.get())
            #saves as png
            get_code.png(input_path, scale=5)

        else:
            #adds .png to filename
            input_path = f"{input_path}.png"
            #creates qr from entry box
            get_code = pyqrcode.create(my_entry.get())
            #saves as png
            get_code.png(input_path, scale=5)
        #puts qr on screen
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        #adds image to label
        my_label.config(image=get_image)
        #deletes entry
        my_entry.delete(0, END)
        #flashes up a finished message
        my_entry.insert(0, "Dokončeno")


def clear_all():
    my_entry.delete(0, END)
    my_label.config(image="")


my_entry = Entry(root, font=("Arial", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Vytvoř si QR kód!", command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text="Vymazat", command=clear_all)
my_button2.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)



root.mainloop()