class Car:
    def __init__(self, model, rent_per_day, available=True):
        self.model = model
        self.rent_per_day = rent_per_day
        self.available = available
    def rent(self, days):
        if self.available:
            self.available = False
            total_cost = self.rent_per_day * days
            print(f"Car rented. Total cost = ฿{total_cost}")
        else:
            print("Car not available")
    def return_car(self):
        self.available = True
        print("Car returned")
    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Model: {self.model}")
        print(f"Rent per day: ฿{self.rent_per_day}")
        print(f"Availability: {status}")