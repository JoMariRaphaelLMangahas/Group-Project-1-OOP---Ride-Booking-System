import tkinter as tk
from tkinter import ttk, PhotoImage, LEFT, messagebox  # Added messagebox import
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkFont, CTkEntry
import pickle

from .view_bookings_window import ViewBookingsWindow
from .booking_interface import BookingInterface
from .booking_info_window import BookingInfoWindow
from .user_login_booking import AuthWindow
from .history_window import HistoryWindow

class RideApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.records = []
        self.view_bookings_window = None  # Initialize the window reference

        # Fonts
        font1 = CTkFont(family="Candara", size=70, weight="bold", slant="italic")

        # Make the window resizable
        self.attributes('-fullscreen', True)
        self.configure(bg="#F6D2E0")

        # Header frame (Logo, Name of the App) using customtkinter for a modern look
        self.header_frame = CTkFrame(self, corner_radius=10, fg_color="#C8E7F5", height=90, border_color="#C8E7F5", border_width=5)
        self.header_frame.pack(fill=tk.X)

        self.header_label = CTkLabel(self.header_frame, text="ZOOMERS", font=font1, text_color="#FFFFFF")
        self.header_label.place(relx=0.43, rely=0.5, anchor="w")

        self.header_img = tk.PhotoImage(file='assets/zoomers_logo.png')
        self.header_image_label = CTkLabel(self.header_frame, image=self.header_img, fg_color="#C8E7F5")
        self.header_image_label.place(relx=0.35, rely=0.5, anchor="w")

        # Motor frame
        self.motor_frame = tk.Frame(self, borderwidth=3, relief="groove")
        self.motor_frame.place(relx=0.50, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Motor icon
        self.motor_img = tk.PhotoImage(file='assets/motor.png')
        self.motor_image_label = tk.Label(self.motor_frame, image=self.motor_img, bg="#C8E7F5")
        self.motor_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Motor button
        self.motor_button = tk.Button(self, text="Book Motor", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Motor"))
        self.motor_button.place(relx=0.50, rely=0.49, anchor="center")

        # Car frame
        self.car_frame = tk.Frame(self, borderwidth=3, relief="groove")
        self.car_frame.place(relx=0.83, rely=0.3, relwidth=0.3, relheight=0.3, anchor="center")

        # Car icon
        self.car_img = tk.PhotoImage(file='assets/car.png')
        self.car_image_label = tk.Label(self.car_frame, image=self.car_img, bg="#C8E7F5")
        self.car_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Car button
        self.car_button = tk.Button(self, text="Book Car", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Car"))
        self.car_button.place(relx=0.83, rely=0.49, anchor="center")

        # Taxi cab frame
        self.taxi_cab_frame = tk.Frame(self, borderwidth=3, relief="groove")
        self.taxi_cab_frame.place(relx=0.50, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Taxi cab icon
        self.taxi_cab_img = tk.PhotoImage(file='assets/taxicab.png')
        self.taxi_cab_image_label = tk.Label(self.taxi_cab_frame, image=self.taxi_cab_img, bg="#C8E7F5")
        self.taxi_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Taxi cab button
        self.taxi_cab_button = tk.Button(self, text="Book Taxi Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Taxi Cab"))
        self.taxi_cab_button.place(relx=0.50, rely=0.89, anchor="center")

        # Premium cab frame
        self.prem_cab_frame = tk.Frame(self, borderwidth=3, relief="groove")
        self.prem_cab_frame.place(relx=0.83, rely=0.7, relwidth=0.3, relheight=0.3, anchor="center")

        # Premium cab icon
        self.prem_cab_img = tk.PhotoImage(file='assets/premcab.png')
        self.prem_cab_image_label = tk.Label(self.prem_cab_frame, image=self.prem_cab_img, bg="#C8E7F5")
        self.prem_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Premium cab button
        self.prem_cab_button = tk.Button(self, text="Book Premium Cab", font=("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=lambda: self.show_vehicle_details("Premium Cab"))
        self.prem_cab_button.place(relx=0.83, rely=0.89, anchor="center")

        # Profile button
        self.book_now_button = tk.Button(self, text="BOOK NOW", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command=self.open_book_now)
        self.book_now_button.place(relx=0.30, rely=0.15, anchor="ne")

        # Bookings button
        self.bookings_button = tk.Button(self, text="BOOKINGS", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command = self.open_view_bookings)
        self.bookings_button.place(relx=0.30, rely=0.30, anchor="ne")

        # History button
        self.history_button = tk.Button(self, text="HISTORY", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF", command=self.open_history)
        self.history_button.place(relx=0.30, rely=0.45, anchor="ne")

        # Feedback button
        self.feedback_button = tk.Button(self, text="FEEDBACK", font=("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.feedback_button.place(relx=0.30, rely=0.60, anchor="ne")

        # Log-out Button
        self.out_button = tk.Button(self, text="LOG OUT", font=("Candara", 20, "bold"), height=2, width=20, fg="#FFFFFF", bg="#000000", command=self.logout)
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
            pass
            # self.destroy()  # Close the current RideApp window
            # root = tk.Tk()
            # app = user_login_booking.MobileApp(root)
            # root.mainloop()



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
              "assets/MOTORPIC.png"),

            "Car": ("Zoom-Zone: Travel with a Zing!\n\n"
                    "\n"
                    "• Effortless journeys with our fleet.\n"
                    "\n"
                    "• Various vehicles for your comfort.\n"
                    "\n"
                    "• Flexible easy payment methods.",
                    "assets/CARPIC.png"),

            "Taxi Cab": ("Zoom-Cab: Lightning-Fast Rides!\n\n"
                         "\n"
                         "• Effortless booking for rapid transit.\n"
                         "\n"
                         "• Choose from standard and premium rides.\n"
                         "\n"
                         "• Metered fare with a minimal booking fee.",
                         "assets/TAXICABPIC.png"),

            "Premium Cab": ("Zoom-Wheel: Accelerating Your Commute!\n\n"
                            "• Swift transportation! (5 seater)\n"
                            "\n"
                            "• Onboard Wi-Fi for productive journeys.\n"
                            "\n"
                            "• Transparent pricing with no hidden fees.",
                            "assets/PREMIUMCABPIC.png")
        }

        detail_text, image_file = details.get(vehicle_type, ("No details available", ""))

        popup = tk.Toplevel(self)
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
        booking_window = BookingInfoWindow(self, vehicle_type)

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
            self.view_bookings_window = tk.Toplevel(self)
            self.view_bookings_window.title("View Bookings")
            self.view_bookings_window.geometry("800x600")  # Adjust the size as needed
            self.view_bookings_window.transient(self)
            self.view_bookings_window.grab_set()  # Make the window modal
            ViewBookingsWindow(self.view_bookings_window, self.records, self.save_records)
        else:
            self.view_bookings_window.lift()

    def open_book_now(self):
        booking_window = tk.Toplevel(self)
        BookingInterface(booking_window, self.records)

    def setup_gui(self):
        # Set up your main GUI here
        self.book_now_button = tk.Button(self, text="BOOK NOW", font=("Candara", 20, "bold"),
                                         height=2, width=20, bg="#FFFFFF", command=self.open_booking_app)
        self.book_now_button.pack(pady=20)

    def open_booking_app(self):
        booking_window = tk.Toplevel(self)  # Create a new Toplevel window
        BookingInterface(booking_window)

    def open_history(self):
        if self.history_window is None or not tk.Toplevel.winfo_exists(self.history_window):
            self.history_window = tk.Toplevel(self)
            self.history_window.title("Booking History")
            self.history_window.geometry("800x600")  # Adjust size as needed
            self.history_window.transient(self)
            self.history_window.grab_set()  # Make window modal
            HistoryWindow(self.history_window, self.records)
        else:
            self.history_window.lift()

if __name__ == "__main__":
    app = RideApp()
    app.mainloop()
