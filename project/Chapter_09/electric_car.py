class Car():
    '''汽车'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reding) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reding:
            self.odometer_reding = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reding += miles

class Battery():

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印电瓶容量'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        '''指出电瓶续航'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

class ElectricCar(Car):
    '''Represent aspects of a car,specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''初始化Car父类属性'''
        super().__init__(make, model, year)
        self.battery = Battery()

my_teasla = ElectricCar('tesla', 'model s', 2016)
print(my_teasla.get_descriptive_name())
my_teasla.battery.describe_battery()
my_teasla.battery.get_range()
