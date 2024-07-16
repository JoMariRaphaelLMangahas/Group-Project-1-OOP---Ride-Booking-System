class Record:
    def __init__(self, booking_number = 0, status = "", date = "", time = "", pick_up_address = "", destination = "", vehicle_type = "", distance = 0.0, cost = 0.0, driver = ""):
        self.booking_number = None # ID
        self.status: str = None
        self.date: str = None
        self.time: str = None
        self.pick_up_address: str = None
        self.destination: str = None
        self.vehicle_type: str = None
        self.distance: float = None
        self.cost: float = None
        self.driver: tsr = None

    def from_tuple(self, record: tuple):
        try:
            self.booking_number = record[0]
            self.status = record[1]
            self.date = record[2]
            self.time = record[3]
            self.pick_up_address = record[4]
            self.destination = record[5]
            self.vehicle_type = record[6]
            self.distance = record[7]
            self.cost = record[8]
            self.driver = record[9]
        except Exception as e:
            print(f"Error converting tuple to record: {e}")
        except IndexError as e:
            print(f"Error accessing tuple to record: {e}")

    def to_tuple(self) -> tuple:
        return (self.booking_number, self.status, self.date, self.time, self.pick_up_address, self.destination, self.vehicle_type, self.distance, self.cost, self.driver)