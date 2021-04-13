class House:
    sides = 4
    groud_floor = True
    roof = True


# print(House.sides)
# print(House.groud_floor)
# print(House.roof)

class Car:
    wheels_count = 4

    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def ride(self):
        return f'{self.brand} {self.model} {self.color} is driving'


# toyota = Car('toyota', 'red', 'camry')
# ford = Car('ford', 'yellow', 'escort')
# vw = Car('vw', 'green', 'golf')
#
# print(toyota.brand)
# print(toyota.color)
# print(toyota.model)
# print(toyota.wheels_count)
# print(toyota.ride())
#
# print('-' * 50)
# print(ford.brand)
# print(ford.color)
# print(ford.model)
# print(ford.wheels_count)
# print(ford.ride())
#
#
# print('-' * 50)
# print(vw.brand)
# print(vw.color)
# print(vw.model)
# print(vw.wheels_count)
# print(vw.ride())


class CarWithTrailer(Car):
    def __init__(self, brand, color, model, has_trailer):
        super().__init__(brand, color, model)
        self.has_trailer = has_trailer

    def ride_with_trailer(self):
        return f'{self.brand} {self.model} {self.color} is driving. Does it has trailer - {self.has_trailer}'

    def ride(self):
        return 'kdkkdkdkdkdkkd'


car_with_trailer = CarWithTrailer('MAN', 'gray', '101', True)
#
# print(car.brand)
# print(car.color)
# print(car.model)
# print(car.wheels_count)
# print(car.ride())
# print(car.ride_with_trailer())


class TruckMixin:
    wheels_count = 10

    def __init__(self, brand, color, model, truck_trailer):
        super().__init__(brand, color, model)
        self.truck_trailer = truck_trailer

    def is_truck(self):
        print(id(self))
        return f'Is a truck - {hasattr(self, "truck_trailer")}'


class Truck(TruckMixin, Car):
    ...


truck = Truck('MAN', 'gray', '101', 'truck_r')
# truck2 = Truck('MAN', 'gray', '101', 'truck_r')
#
# print(truck.brand, truck.color)
# print(truck.color)
# print(truck.model)
# print(truck.wheels_count)
# print(truck.ride())
# print(truck.is_truck())
# print(id(truck))
# print(Truck.__mro__)
# print(getattr(truck, 'truck_trailer'))
# print(truck.truck_trailer)
# print(getattr(truck, 'truck_ter', 'aaaaaa'))
# # print(truck.truck_ter)
# print(setattr(truck, 'truck_trailer', '11111'))
# print(truck.truck_trailer)
#
# #   Вот так вот плохо
# print(setattr(truck, 'truck_t', '222222'))
# print(truck.truck_t)
# truck2.truck_t = 222
# print(truck2.truck_t)


# Полиморфизм


class Bike:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def ride(self):
        return f'Bike is riding color - {self.color}, brand - {self.brand}, model - {self.model}'


car = Car('toyota', 'red', 'camry')
bike = Bike('bmw', 'green', 'mount')


def print_ride_text(obj):
    print(obj.ride())


# print_ride_text(car)
# print_ride_text(bike)
# print_ride_text(truck)
# print_ride_text(car_with_trailer)
