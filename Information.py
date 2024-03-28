from tkinter import *
from tkinter import messagebox  
from PIL import Image, ImageTk
import mysql.connector
import subprocess

class ReservationInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL EZZIRARI") 
        self.root.geometry("1200x675")
        self.root.iconbitmap("hotel.ico")
        self.root.resizable(False, False)

        self.background_image = Image.open("bgsign.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1200, height=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        self.label = Label(self.canvas, font=('calibri', 20, 'bold'), text='Votre Reservation', foreground='white', background='black')
        self.label.place(x=500, y=180)

        self.label0 = Label(self.canvas, font=('calibri', 20, 'bold'), text=' User Email :', foreground='white', background='black')
        self.label0.place(x=250, y=260)
        
        self.reservation_number_labels = Label(self.canvas, font=('calibri', 20), background='black', foreground='white')
        self.reservation_number_labels.place(x=600, y=260)


        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text=' Reservation Code :', foreground='white', background='black')
        self.label1.place(x=250, y=310)
        
        self.reservation_number_label = Label(self.canvas, font=('calibri', 20), background='black', foreground='white')
        self.reservation_number_label.place(x=600, y=310)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Reservation Date:', foreground='white', background='black')
        self.label2.place(x=250, y=370)
        self.reservation_date_label = Label(self.canvas, font=('calibri', 20), background='black', foreground='white')
        self.reservation_date_label.place(x=600, y=370)

        self.label3 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Type de Chambre:', background='black', foreground='white')
        self.label3.place(x=250, y=430)
        self.room_type_label = Label(self.canvas, font=('calibri', 20), background='black', foreground='white')
        self.room_type_label.place(x=600, y=430)

        self.label4 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Prix Totale:', background='black', foreground='white')
        self.label4.place(x=250, y=500)
        self.total_price_label = Label(self.canvas, font=('calibri', 20), background='black', foreground='white')
        self.total_price_label.place(x=600, y=500)

        self.b6 = Button(self.canvas, text='Log-out', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief=SOLID, cursor='hand2', command=self.switch_page)
        self.b6.place(x=450, y=600, width=300, height=40)
        
        # Call method to fetch and display reservation info
        self.display_reservation_info()

    def display_reservation_info(self):
        try:
            # Connect to the database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="wahiba2004wahiba",
                database="hotel_ezzirari"
            )
            
            # Create a cursor to execute SQL queries
            mycursor = mydb.cursor()

            

            # Execute a query to retrieve reservation info from the reservation table
            # Joining client table with user_selections and filtering by email
            mycursor.execute("SELECT  email, id, booking_date, room, total_price FROM user_selections where email = (select email from connexion order by id desc limit 1)")


            # Fetch all records
            reservations = mycursor.fetchall()

            if not reservations:
                messagebox.showinfo("No Reservation", "No reservations found for this email.")
            else:
                # Display the fetched data in the labels
               for reservation_info in reservations:
                    self.reservation_number_labels.config(text=reservation_info[0])
                    self.reservation_number_label.config(text=reservation_info[1])
                    self.reservation_date_label.config(text=reservation_info[2])
                    self.room_type_label.config(text=reservation_info[3])
                    self.total_price_label.config(text=reservation_info[4])


        except mysql.connector.Error as error:
            print("Error fetching data from MySQL table:", error)

    def switch_page(self):
        root.withdraw()
        subprocess.run(["python", "log-in.py"])

root = Tk()
app = ReservationInfo(root)
root.mainloop()
