#Unlimited arguments or unlimited positional arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,6,8,24,45))

#unlimited keyworded arguments

# def calculate(**kwargs):
#     print(kwargs)
#
# calculate(add=3,multiply=5)

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)


class Car:
    def __init__(self, **kw):
        # the below will throw error if we are trying to print a empty value instead use .get
        # self.make = kw["make"]
        # self.model = kw["model"]

        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)