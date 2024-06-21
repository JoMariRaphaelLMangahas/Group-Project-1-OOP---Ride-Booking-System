import tkinter as tk
from tkinter import ttk, PhotoImage, LEFT, messagebox  # Added messagebox import
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkFont, CTkEntry
from view_bookings_app import ViewBookingsApp
import pickle
from main_booking_app import BookingApp

class BookingWindow(tk.Toplevel):
    def __init__(self, master=None, vehicle_type=""):
        super().__init__(master)
        self.title(f"{vehicle_type} Booking Window")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(background="#C8E7F5")
        self.records = self.load_data()

        font2 = CTkFont(family="Inter", size=20)

        self.booking_window_frame = CTkFrame(self, width=449, height=434, border_width=2, fg_color="#F6D2E0")
        self.booking_window_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Pick-up Address
        self.pickup_label = CTkLabel(self.booking_window_frame, text="Pick-up Address:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.1, anchor="w")

        self.pickup_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.1, anchor="w")

        # Drop-off Address
        self.dropoff_label = CTkLabel(self.booking_window_frame, text="Drop-off Address:", text_color="#000000", font=font2)
        self.dropoff_label.place(relx=0.1, rely=0.2, anchor="w")

        self.dropoff_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.dropoff_entry.place(relx=0.5, rely=0.2, anchor="w")

        # Pick-up Date
        self.pickup_date_label = CTkLabel(self.booking_window_frame, text="Pick-up Date:", text_color="#000000", font=font2)
        self.pickup_date_label.place(relx=0.1, rely=0.3, anchor="w")

        self.pickup_date_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_date_entry.place(relx=0.5, rely=0.3, anchor="w")

        # Pick-up Time
        self.pickup_time_label = CTkLabel(self.booking_window_frame, text="Pick-up Time:", text_color="#000000", font=font2)
        self.pickup_time_label.place(relx=0.1, rely=0.4, anchor="w")

        self.pickup_time_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_time_entry.place(relx=0.5, rely=0.4, anchor="w")

        # Submit button
        self.submit_button = CTkButton(self.booking_window_frame, text="Submit", fg_color="#000000", text_color="#C8E7F5")
        self.submit_button.place(relx=0.5, rely=0.9, anchor="center")

        # Center the booking window
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def load_data(self):
        try:
            with open("booking_data.dat", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

class RideApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Zoomers")
        self.records = []
        self.view_bookings_window = None  # Initialize the window reference

        # Fonts
        font1 = CTkFont(family="Candara", size=70, weight="bold", slant="italic")

        # Make the window resizable
        self.master.attributes('-fullscreen', True)
        self.master.configure(bg="#F6D2E0")

        # Header frame (Logo, Name of the App) using customtkinter for a modern look
        self.header_frame = CTkFrame(master, corner_radius=10, fg_color="#C8E7F5", height=90, border_color="#C8E7F5", border_width=5)
        self.header_frame.pack(fill=tk.X)

        self.header_label = CTkLabel(self.header_frame, text="ZOOMERS", font=font1, text_color="#FFFFFF")
        self.header_label.place(relx=0.43, rely=0.5, anchor="w")

        self.header_img = tk.PhotoImage(file='zoomers_logo.png')
        self.header_image_label = CTkLabel(self.header_frame, image=self.header_img, fg_color="#C8E7F5")
        self.header_image_label.place(relx=0.35, rely=0.5, anchor="w")

        # Motor frame
        self.motor_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.motor_frame.place(relx=0.50, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Motor icon
        self.motor_img = tk.PhotoImage(file='motor.png')
        self.motor_image_label = tk.Label(self.motor_frame, image=self.motor_img, bg="#C8E7F5")
        self.motor_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Motor button
        self.motor_button = tk.Button(master, text="Book Motor", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Motor"))
        self.motor_button.place(relx=0.50, rely=0.49, anchor="center")

        # Car frame
        self.car_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.car_frame.place(relx=0.83, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Car icon
        self.car_img = tk.PhotoImage(file='car.png')
        self.car_image_label = tk.Label(self.car_frame, image=self.car_img, bg="#C8E7F5")
        self.car_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Car button
        self.car_button = tk.Button(master, text="Book Car", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Car"))
        self.car_button.place(relx=0.83, rely=0.49, anchor="center")

        # Taxi cab frame
        self.taxi_cab_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.taxi_cab_frame.place(relx=0.50, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Taxi cab icon
        self.taxi_cab_img = tk.PhotoImage(file='taxicab.png')
        self.taxi_cab_image_label = tk.Label(self.taxi_cab_frame, image=self.taxi_cab_img, bg="#C8E7F5")
        self.taxi_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Taxi cab button
        self.taxi_cab_button = tk.Button(master, text="Book Taxi Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Taxi Cab"))
        self.taxi_cab_button.place(relx=0.50, rely=0.89, anchor="center")

        # Premium cab frame
        self.prem_cab_frame = tk.Frame(master, borderwidth=3, relief="groove")
        self.prem_cab_frame.place(relx=0.83, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Premium cab icon
        self.prem_cab_img = tk.PhotoImage(file='premcab.png')
        self.prem_cab_image_label = tk.Label(self.prem_cab_frame, image=self.prem_cab_img, bg="#C8E7F5")
        self.prem_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Premium cab button
        self.prem_cab_button = tk.Button(master, text="Book Premium Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Premium Cab"))
        self.prem_cab_button.place(relx=0.83, rely=0.89, anchor="center")

        # Profile button
        self.book_now_button = tk.Button(master, text="BOOK NOW", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command=self.open_book_now)
        self.book_now_button.place(relx=0.30, rely=0.15, anchor="ne")

        # Bookings button
        self.bookings_button = tk.Button(master, text="BOOKINGS", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command = self.open_view_bookings)
        self.bookings_button.place(relx=0.30, rely=0.30, anchor="ne")

        # History button
        self.history_button = tk.Button(master, text="HISTORY", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command=self.open_history)
        self.history_button.place(relx=0.30, rely=0.45, anchor="ne")

        # Feedback button
        self.feedback_button = tk.Button(master, text="FEEDBACK", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.feedback_button.place(relx=0.30, rely=0.60, anchor="ne")

        # Log-out Button
        self.out_button = tk.Button(master, text="LOG OUT", font=("Candara", 20, "bold"), height=2, width=20, fg="#FFFFFF", bg="#000000", command=self.logout)
        self.out_button.place(relx=0.30, rely=0.75, anchor="ne")

        # Bind the label and frame together
        self.prem_cab_frame.bind("<Configure>", self.on_frame_configure)
        self.prem_cab_image_label.bind("<Configure>", self.on_label_configure)

        # Initialize records
        self.records = self.load_data()

        self.view_bookings_window = None  # To store reference of ViewBookingsApp window if needed

    def logout(self):
        confirm = messagebox.askokcancel("Log Out", "Are you sure you want to log out?")
        if confirm:
            self.master.destroy()  # Close the current RideApp window
            import user_login_booking
            root = tk.Tk()
            app = user_login_booking.MobileApp(root)
            root.mainloop()



    def on_frame_configure(self, event):
        # Get the new size of the frame
        width = event.width
        height = event.height

        # Adjust the size of the label to match the frame
        self.prem_cab_image_label.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def on_label_configure(self, event):
        # Get the new size of the label
        width = event.width
        height = event.height

        # Adjust the size of the frame to match the label
        self.prem_cab_frame.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def show_vehicle_details(self, vehicle_type):
        details = {
            "Motor": ("Zoom-Wheel: Fast and Stress-Free!\n"
              "\n"
              "• Enjoy motorbike rides on-demand.\n"
              "\n"
              "• Arrive at your destination smoothly.\n"
              "\n"
              "• Experience the easy booking.",
              "MOTORPIC.png"),

            "Car": ("Zoom-Zone: Travel with a Zing!\n\n"
                    "\n"
                    "• Effortless journeys with our fleet.\n"
                    "\n"
                    "• Various vehicles for your comfort.\n"
                    "\n"
                    "• Flexible easy payment methods.",
                    "CARPIC.png"),

            "Taxi Cab": ("Zoom-Cab: Lightning-Fast Rides!\n\n"
                         "\n"
                         "• Effortless booking for rapid transit.\n"
                         "\n"
                         "• Choose from standard and premium rides.\n"
                         "\n"
                         "• Metered fare with a minimal booking fee.",
                         "TAXICABPIC.png"),

            "Premium Cab": ("Zoom-Wheel: Accelerating Your Commute!\n\n"
                            "• Swift transportation! (5 seater)\n"
                            "\n"
                            "• Onboard Wi-Fi for productive journeys.\n"
                            "\n"
                            "• Transparent pricing with no hidden fees.",
                            "PREMIUMCABPIC.png")
        }

        detail_text, image_file = details.get(vehicle_type, ("No details available", ""))

        popup = tk.Toplevel(self.master)
        popup.title(f"{vehicle_type} Details")
        popup.geometry("500x650")
        popup.configure(bg="#C8E7F5")

        header, details = detail_text.split('\n\n', 1)

        header_label = tk.Label(popup, text=header, font=("Candara", 16, "bold"), bg="#C8E7F5", justify="center")
        header_label.place(relx=0.5, rely=0.08, anchor="center", relwidth=0.9)

        detail_label = tk.Label(popup, text=details, font=("Lucida Console", 11), bg="#C8E7F5", justify=LEFT, wraplength=450, pady=5)
        detail_label.place(relx=0.5, rely=0.71, anchor="center", relwidth=0.9)

        if image_file:
            image = PhotoImage(file=image_file)
            image_label = tk.Label(popup, image=image, bg="#C8E7F5")
            image_label.image = image
            image_label.place(relx=0.5, rely=0.37, anchor="center")

        book_button = tk.Button(popup, text="BOOK NOW", font=("Helvetica", 13, "bold"), bg="#F6D2E0", command=lambda: self.open_booking_window(vehicle_type, popup))
        book_button.place(relx=0.5, rely=0.86, anchor="center", relwidth=0.6)

        close_button = tk.Button(popup, text="CANCEL", font=("Helvetica", 11), command=popup.destroy)
        close_button.place(relx=0.5, rely=0.92, anchor="center", relwidth=0.6)

        self.center_popup(popup)

    def center_popup(self, popup):
        popup.update_idletasks()
        width = popup.winfo_width()
        height = popup.winfo_height()
        x = (popup.winfo_screenwidth() - width) // 2
        y = (popup.winfo_screenheight() - height) // 2
        popup.geometry(f"{width}x{height}+{x}+{y}")


    def open_booking_window(self, vehicle_type, popup):
        popup.destroy()  # Close the details popup
        booking_window = BookingWindow(self.master, vehicle_type)

    def save_data(self):
        with open("booking_data.dat", "wb") as file:
            pickle.dump(self.records, file)
        
    def load_data(self):
        try:
            with open("booking_data.dat", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
    
    def save_records(self):
        with open("booking_data.dat", "wb") as file:
            pickle.dump(self.records, file)
    
    def open_view_bookings(self):
        if self.view_bookings_window is None or not tk.Toplevel.winfo_exists(self.view_bookings_window):
            self.view_bookings_window = tk.Toplevel(self.master)
            self.view_bookings_window.title("View Bookings")
            self.view_bookings_window.geometry("800x600")  # Adjust the size as needed
            self.view_bookings_window.transient(self.master)
            self.view_bookings_window.grab_set()  # Make the window modal
            ViewBookingsApp(self.view_bookings_window, self.records, self.save_records)
        else:
            self.view_bookings_window.lift()
    
    def open_book_now(self):
        booking_window = tk.Toplevel(self.master)
        BookingApp(booking_window, self.records)

    def setup_gui(self):
        # Set up your main GUI here
        self.book_now_button = tk.Button(self.master, text="BOOK NOW", font=("Candara", 20, "bold"),
                                         height=2, width=20, bg="#FFFFFF", command=self.open_booking_app)
        self.book_now_button.pack(pady=20)

    def open_booking_app(self):
        booking_window = tk.Toplevel(self.master)  # Create a new Toplevel window
        BookingApp(booking_window)
    
    def open_history(self):
        if self.history_window is None or not tk.Toplevel.winfo_exists(self.history_window):
            self.history_window = tk.Toplevel(self.master)
            self.history_window.title("Booking History")
            self.history_window.geometry("800x600")  # Adjust size as needed
            self.history_window.transient(self.master)
            self.history_window.grab_set()  # Make window modal
            HistoryApp(self.history_window, self.records)
        else:
            self.history_window.lift()

class HistoryApp:
    def __init__(self, root, records):
        self.root = root
        self.records = records
        self.root.title("Booking History")

        self.create_widgets()
        self.display_history()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        # Define columns with fixed widths
        columns = ("Booking Number", "Status", "Date", "Time", "Pick-up address", "Destination", "Vehicle Type", "Distance", "Cost", "Driver")
        self.treeview = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Configure column headings and set fixed widths
        column_widths = {
            "Booking Number": 120,
            "Status": 100,
            "Date": 100,
            "Time": 100,
            "Pick-up address": 200,
            "Destination": 200,
            "Vehicle Type": 100,
            "Distance": 100,
            "Cost": 100,
            "Driver": 100
        }

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=column_widths[col], anchor='center')

        # Pack the Treeview widget
        self.treeview.pack(side="left", expand=True, fill="both")

        # Add vertical scrollbar
        yscrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.treeview.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=yscrollbar.set)

        # Add horizontal scrollbar
        xscrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.treeview.xview)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.config(xscrollcommand=xscrollbar.set)

    def display_history(self):
        for record in self.records:
            if record[1] == "Completed" or record[1] == "Cancelled":
                self.treeview.insert("", "end", values=record)

if __name__ == "__main__":
    master = tk.Tk()  # Or tk.Toplevel() if this is not your main application window
    app = RideApp(master)
    master.mainloop()