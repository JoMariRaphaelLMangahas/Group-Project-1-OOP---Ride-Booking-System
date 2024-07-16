import datetime
import pickle
import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from geopy.distance import distance
import tkinter.messagebox as messagebox
from view_bookings_app import ViewBookingsApp

class BookingApp:
    def __init__(self, master, records):
        self.master = master
        self.master.title("Booking a Cab")
        self.records = records
        self.setup_gui()

        self.records = self.load_data()
        self.input_fields = {}
        self.map_view = None

        self.geolocator = Nominatim(user_agent="booking_app")

        # Initialize last booking number
        self.last_booking_number = len(self.records) + 1 if self.records else 1

        self.create_widgets()
        self.center_window()

    def load_data(self):
        try:
            with open("booking_data.dat", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open("booking_data.dat", "wb") as file:
            pickle.dump(self.records, file)

    def add_booking(self):
        if not all(self.input_fields[field_name].get() for field_name in ('month', 'day', 'year', 'hour', 'minute', 'pick_up_address', 'destination', 'vehicle_type')):
            messagebox.showerror("Error", "Please fill in all the required information.")
            return

        date_str = f"{self.input_fields['month'].get()}-{self.input_fields['day'].get()}-{self.input_fields['year'].get()}"
        time_str = f"{self.input_fields['hour'].get()}:{self.input_fields['minute'].get()}"
        date = datetime.datetime.strptime(date_str, "%B-%d-%Y").date()
        time = datetime.datetime.strptime(time_str, "%H:%M").time()

        pick_up_address = self.input_fields['pick_up_address'].get()
        destination = self.input_fields['destination'].get()
        vehicle_type = self.input_fields['vehicle_type'].get()

        booking_number = self.last_booking_number  # Use the last booking number
        booking = (booking_number, "Pending", date, time, pick_up_address, destination, vehicle_type)
        self.records.append(booking)

        self.add_pinpoints_and_path(pick_up_address, destination, vehicle_type)

        self.last_booking_number = self.last_booking_number + 1  # Increment the last booking number

        self.save_data()

    def geocode_address(self, address):
        try:
            location = self.geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            else:
                print(f"Geocoding failed for address: {address}")
                return None
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Geocoding error: {e}")
            return None

    def add_pinpoints_and_path(self, pick_up_address, destination, vehicle_type):
        pickup_coords = self.geocode_address(pick_up_address)
        destination_coords = self.geocode_address(destination)

        if pickup_coords and destination_coords:
            self.map_view.set_marker(pickup_coords[0], pickup_coords[1], text=pick_up_address)
            self.map_view.set_marker(destination_coords[0], destination_coords[1], text=destination)
            self.map_view.set_path([pickup_coords, destination_coords], color="blue")

            pickup_point = (pickup_coords[0], pickup_coords[1])
            destination_point = (destination_coords[0], destination_coords[1])
            dist = distance(pickup_point, destination_point).kilometers

            cost = self.calculate_fare(dist, vehicle_type)

            record = list(self.records[-1])
            record.append(f"{dist:.2f} km")
            record.append(f"\u20b1{cost:.2f}")
            self.records[-1] = tuple(record)

    def calculate_fare(self, distance_km, vehicle_type):
        vehicle_class = {
            "Motor": MotorFare,
            "Car": CarFare,
            "Taxi Cab": TaxiCabFare,
            "Premium Cab": PremiumCabFare
        }.get(vehicle_type, BaseFare)

        return vehicle_class().calculate_fare(distance_km)
    
    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=True, fill="both")

        tk.Label(self.frame, text="Date:").grid(row=0, column=0, padx=5, pady=5)
        date_frame = tk.Frame(self.frame)
        date_frame.grid(row=0, column=1, padx=5, pady=5)

        month_names = [datetime.date(2000, month, 1).strftime('%B') for month in range(1, 13)]
        self.input_fields['month'] = ttk.Combobox(date_frame, values=month_names, width=10)
        self.input_fields['month'].set(datetime.datetime.now().strftime('%B'))
        self.input_fields['month'].pack(side=tk.LEFT)

        self.input_fields['day'] = ttk.Combobox(date_frame, values=[str(day).zfill(2) for day in range(1, 32)], width=3)
        self.input_fields['day'].set(str(datetime.datetime.now().day).zfill(2))
        self.input_fields['day'].pack(side=tk.LEFT)

        self.input_fields['year'] = ttk.Combobox(date_frame, values=[str(year) for year in range(2023, 2031)], width=5)
        self.input_fields['year'].set(datetime.datetime.now().year)
        self.input_fields['year'].pack(side=tk.LEFT)

        tk.Label(self.frame, text="Time:").grid(row=1, column=0, padx=5, pady=5)
        time_frame = tk.Frame(self.frame)
        time_frame.grid(row=1, column=1, padx=5, pady=5)

        self.input_fields['hour'] = ttk.Combobox(time_frame, values=[str(hour).zfill(2) for hour in range(0, 24)], width=3)
        self.input_fields['hour'].set(str(datetime.datetime.now().hour).zfill(2))
        self.input_fields['hour'].pack(side=tk.LEFT)

        self.input_fields['minute'] = ttk.Combobox(time_frame, values=[str(minute).zfill(2) for minute in range(0, 60, 5)], width=3)
        self.input_fields['minute'].set('00')
        self.input_fields['minute'].pack(side=tk.LEFT)

        tk.Label(self.frame, text="Pick-up address:").grid(row=2, column=0, padx=5, pady=5)
        self.input_fields['pick_up_address'] = tk.Entry(self.frame)
        self.input_fields['pick_up_address'].grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Destination:").grid(row=3, column=0, padx=5, pady=5)
        self.input_fields['destination'] = tk.Entry(self.frame)
        self.input_fields['destination'].grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Vehicle Type:").grid(row=4, column=0, padx=5, pady=5)
        self.input_fields['vehicle_type'] = ttk.Combobox(self.frame, values=["Motor", "Car", "Taxi Cab", "Premium Cab"])
        self.input_fields['vehicle_type'].grid(row=4, column=1, padx=5, pady=5)

        add_booking_button = tk.Button(self.frame, text="Add Booking", command=self.add_booking)
        add_booking_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        view_bookings_button = tk.Button(self.frame, text="View Bookings", command=self.open_view_bookings)
        view_bookings_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        tk.Label(self.frame, text="Map:").grid(row=7, column=0, columnspan=3, padx=5, pady=5)
        self.map_view = TkinterMapView(self.frame, width=400, height=300)
        self.map_view.grid(row=8, column=0, columnspan=3, padx=5, pady=5)
        self.map_view.set_position(14.5995, 120.9842)
        self.map_view.set_zoom(11)
        self.map_view.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    def open_view_bookings(self):
        view_window = tk.Toplevel(self.master)
        ViewBookingsApp(view_window, self.records, self.save_data)

    def setup_gui(self):
        # Define your booking app GUI here
        self.master.geometry("400x650")
        self.center_window()
        self.label = tk.Label(self.master)
        self.label.pack(pady=20)

# Base fare class and subclasses for different vehicle types
class BaseFare:
    def calculate_fare(self, distance_km):
        return 0

class MotorFare(BaseFare):
    def calculate_fare(self, distance_km):
        if distance_km <= 2:
            return 50
        else:
            return 50 + (distance_km - 2) * 10 + distance_km * 2

class CarFare(BaseFare):
    def calculate_fare(self, distance_km):
        return 50 + distance_km * 18 + distance_km * 10

class TaxiCabFare(BaseFare):
    def calculate_fare(self, distance_km):
        return 40 + distance_km * 13.5 + distance_km * 5

class PremiumCabFare(BaseFare):
    def calculate_fare(self, distance_km):
        return 100 + distance_km * 40 + distance_km * 100

def main():
    master = tk.Tk()  # Or tk.Toplevel() if this is not your main application window
    records = []  # Initialize or load your records here
    app = BookingApp(master, records)
    master.mainloop()

if __name__ == "__main__":
    main()
