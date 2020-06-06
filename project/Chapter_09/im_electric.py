from im_car import Car

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