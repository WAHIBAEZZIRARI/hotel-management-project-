from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image, ImageTk

class RegistrationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL EZZIRARI')
        self.root.geometry("1200x900")
        self.root.resizable(False, False)

        self.background_image = Image.open("bgsign.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1200, height=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text='First Name :', background='black', foreground='white')
        self.label1.place(x=450, y=170)

        self.en1 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en1.place(x=450, y=220, width=300, height=40)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Second Name :', background='black', foreground='white')
        self.label2.place(x=450, y=270)

        self.en2 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en2.place(x=450, y=320, width=300, height=40)

        self.label3 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Email :', background='black', foreground='white')
        self.label3.place(x=450, y=370)

        self.en3 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en3.place(x=450, y=420, width="300", height=40)

        self.label4 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Password :', background='black', foreground='white')
        self.label4.place(x=450, y=470)

        self.en4 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en4.place(x=450, y=520, width=300, height=40)

        self.label5 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Confirm Password :', background='black', foreground='white')
        self.label5.place(x=450, y=570)

        self.en5 = Entry(self.canvas, justify=CENTER, bg="white", fg="black", bd=1, relief=SOLID, width="25")
        self.en5.place(x=450, y=620, width=300, height=40)

        self.b6 = Button(self.canvas, text='Submit', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief=SOLID, cursor='hand2', command=self.submit_form)
        self.b6.place(x=450, y=690, width=300, height=40)

        self.b2 = Button(self.canvas, text='Log in', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief=SOLID, cursor='hand2', command=self.switch_page)
        self.b2.place(x=450, y=760, width=300, height=40)

    def submit_form(self):
        firstname = self.en1.get()
        secondname = self.en2.get()
        email = self.en3.get()
        psd = self.en4.get()
        confirm_psd = self.en5.get()

        if psd != confirm_psd:
            messagebox.showerror("Error", "Password Error!")
            return

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wahiba2004wahiba",
            database="hotel_ezzirari"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM client WHERE email = %s", (email,))
        existing_user = mycursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Email already exists!")
            return
        
        sql = "INSERT INTO client (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        val = (firstname, secondname, email, psd)

        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "account created successfully!")

        self.en1.delete(0, 'end') 
        self.en2.delete(0, 'end')
        self.en3.delete(0, 'end')  
        self.en4.delete(0, 'end')  

        self.root.withdraw()


        self.switch_page()

    def switch_page(self):
        self.root.withdraw()
        subprocess.run(["python", "log-in.py"])
    

root = Tk()
app = RegistrationFormApp(root)
root.mainloop()
