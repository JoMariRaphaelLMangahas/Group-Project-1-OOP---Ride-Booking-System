class Record:
    def __init__(self, booking_number = 0, status = "", date = "", time = "", pick_up_address = "", destination = "", vehicle_type = "", distance = 0.0, cost = 0.0, driver = ""):
        self.booking_number: int = None # ID
        self.status: str = None
        self.date: str = None
        self.time: str = None
        self.pick_up_address: str = None
        self.destination: str = None
        self.vehicle_type: str = None
        self.distance: float = None
        self.cost: float = None
        self.driver: str = None

    def from_tuple(self, record: tuple):
        try:
            for i, field in enumerate(record):
                match index:
                    case 0:
                        self.booking_number = field
                    case 1:
                        self.status = field
                    case 2:
                        self.date = field
                    case 3:
                        self.time = field
                    case 4:
                        self.pick_up_address = field
                    case 5:
                        self.destination = field
                    case 6:
                        self.vehicle_type = field
                    case 7:
                        self.distance = field
                    case 8:
                        self.cost = field
                    case 9:
                        self.driver = field
        except Exception as e:
            print(f"Error converting tuple to record: {e}")
        except IndexError as e:
            print(f"Error accessing tuple to record: {e}")

    def to_tuple(self) -> tuple:
        return (self.booking_number, self.status, self.date, self.time, self.pick_up_address, self.destination, self.vehicle_type, self.distance, self.cost, self.driver)

    def to_treeview_tuple(self) -> tuple:
        return (str(self.booking_number),
            self.status,
            self.date,
            self.time,
            self.pick_up_address,
            self.destination,
            self.vehicle_type,
            f"{self.distance:.2f} km",
            f"\u20b1{self.cost:.2f}",
            self.driver
        )