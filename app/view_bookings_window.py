import tkinter as tk
from tkinter import ttk, messagebox
import pickle

from .driver_interface import DriverInterface

class ViewBookingsWindow(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("View Bookings")
        self.master = master

        self.db = self.master.db
        self.records = self.master.records
        self.load_callback = self.master.load_records

        self.create_widgets()
        self.load_records()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        columns = ("Booking Number", "Status", "Date", "Time", "Pick-up address", "Destination", "Vehicle Type", "Distance", "Cost", "Driver")
        self.treeview = ttk.Treeview(self.frame, columns=columns, show="headings")

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

        self.treeview.pack(side="left", expand=True, fill="both")

        yscrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.treeview.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=yscrollbar.set)

        xscrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.treeview.xview)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.config(xscrollcommand=xscrollbar.set)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.find_driver_button = tk.Button(button_frame, text="Find a Driver", command=self.find_driver)
        self.find_driver_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.complete_button = tk.Button(button_frame, text="Complete Booking", command=self.complete_booking)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = tk.Button(button_frame, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, text="Delete Selected Booking", command=self.delete_selected_booking)
        delete_button.pack(side=tk.LEFT, padx=10)

        delete_all_button = tk.Button(button_frame, text="Delete All Bookings", command=self.delete_all_bookings)
        delete_all_button.pack(side=tk.LEFT, padx=10)

        # Add the View Bookings button to refresh the data
        view_bookings_button = tk.Button(button_frame, text="View Bookings", command=self.load_records)
        view_bookings_button.pack(side=tk.LEFT, padx=10)


    def display_records(self):
        for record in self.records:
            # self.treeview.insert("", "end", values=record.to_treeview_tuple())
            print(record.to_treeview_tuple())

    def complete_booking(self):
        pass
        # selected_item = self.treeview.selection()
        # if selected_item:
        #     index = self.treeview.index(selected_item)
        #     if 0 <= index < len(self.records):
        #         if self.records[index][1] == "Completed":
        #             messagebox.showinfo("Already Completed", f"The booking number {self.records[index][0]} is already marked as completed.")
        #             return

        #         if len(self.records[index]) > 9:
        #             driver_id = self.records[index][9]
        #             if driver_id:
        #                 self.remove_driver_from_interface(driver_id)

        #         self.records[index] = tuple(list(self.records[index][:1]) + ["Completed"] + list(self.records[index][2:]))
        #         self.update_treeview()
        #         self.load_records()
        #         self.load_callback()

        #         self.update_button_states(index)
        #     else:
        #         messagebox.showwarning("Invalid Index", "Selected index is out of range.")
        # else:
        #     messagebox.showwarning("No Selection", "Please select a booking to mark as completed.")

    def cancel_booking(self):
        pass

        # selected_item = self.treeview.selection()
        # if selected_item:
        #     index = self.treeview.index(selected_item[0])
        #     if 0 <= index < len(self.records):
        #         if self.records[index][1] == "Cancelled":
        #             messagebox.showinfo("Already Cancelled", f"The booking number {self.records[index][0]} is already marked as cancelled.")
        #             return

        #         if len(self.records[index]) > 9:
        #             driver_id = self.records[index][9]
        #             if driver_id:
        #                 self.remove_driver_from_interface(driver_id)

        #         self.records[index] = tuple(list(self.records[index][:1]) + ["Cancelled"] + list(self.records[index][2:]))
        #         self.update_treeview()
        #         self.load_records()
        #         self.load_callback()

        #         self.update_button_states(index)
        #     else:
        #         messagebox.showwarning("Invalid Index", "Selected index is out of range.")
        # else:
        #     messagebox.showwarning("No Selection", "Please select a booking to mark as cancelled.")

    def find_driver(self):
        pass
        # selected_item = self.treeview.selection()
        # if selected_item:
        #     index = self.treeview.index(selected_item)
        #     if 0 <= index < len(self.records):
        #         status = self.records[index][1]
        #         if status == "Completed":
        #             messagebox.showinfo("Already Completed", f"The booking number {self.records[index][0]} is already marked as completed.")
        #         elif status == "Cancelled":
        #             messagebox.showinfo("Already Cancelled", f"The booking number {self.records[index][0]} is already marked as cancelled.")
        #         else:
        #             driver_root = tk.Toplevel(self)
        #             driver_interface = DriverInterface(driver_root, self.choose_driver)
        #             driver_root.grab_set()
        #     else:
        #         messagebox.showwarning("Invalid Index", "Selected index is out of range.")
        # else:
        #     messagebox.showwarning("No Selection", "Please select a booking to find a driver.")

    def remove_driver_from_interface(self, driver_id):
        # Implement logic to remove driver_id from DriverInterface
        # This might involve modifying DriverInterface or using a callback to DriverInterface
        print(f"Removing driver {driver_id} from DriverInterface...")

    def delete_selected_booking(self):
        pass
        # selected_item = self.treeview.selection()
        # if selected_item:
        #     item_id = selected_item[0]
        #     item_index = self.treeview.index(item_id)

        #     # Remove the driver from the interface if assigned
        #     if len(self.records[item_index]) > 9:
        #         driver_id = self.records[item_index][9]
        #         if driver_id:
        #             self.remove_driver_from_interface(driver_id)

        #     # Delete the record from the list
        #     del self.records[item_index]

        #     # Update the treeview
        #     self.update_treeview()

        #     # Save the updated records
        #     self.save_records()

        # else:
        #     messagebox.showwarning("No Selection", "Please select a booking to delete.")

    def delete_all_bookings(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all bookings?"):
            self.records.clear()
            self.update_treeview()
            self.load_callback()

    def update_treeview(self):
        # Clear current treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Populate treeview with updated records
        self.display_records()

    def choose_driver(self, driver_id):
        selected_item = self.treeview.selection()
        if selected_item:
            index = self.treeview.index(selected_item)
            self.records[index] = tuple(list(self.records[index][:9]) + [driver_id])
            self.update_treeview()
            self.load_callback()
        else:
            messagebox.showwarning("No Selection", "Please select a booking.")

    def load_records(self):
        self.records = self.db.load_records()

    def save_records(self):
        with open("booking_data.dat", "wb") as file:
            pickle.dump(self.records, file)

    def handle_driver_assignment(self, index, action):
        # action: "complete" or "cancel"
        driver_id = self.records[index][9]
        if driver_id:  # If a driver is assigned
            if action == "complete" or action == "cancel":
                # Remove driver from DriverInterface (dummy implementation)
                # You need to implement a mechanism to remove the driver from DriverInterface
                print(f"Removing driver {driver_id} from DriverInterface...")

    def update_button_states(self, index):
        if index < 0 or index >= len(self.records):
            return

        status = self.records[index][1]

        if status == "Completed" or status == "Cancelled":
            self.complete_button.config(state=tk.DISABLED)
            self.cancel_button.config(state=tk.DISABLED)
            self.find_driver_button.config(state=tk.DISABLED)
        else:
            self.complete_button.config(state=tk.NORMAL)
            self.cancel_button.config(state=tk.NORMAL)
            self.find_driver_button.config(state=tk.NORMAL)

