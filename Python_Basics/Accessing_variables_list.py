#!/usr/bin/python

cars = ['Honda','Bmw','Audi']
length=len(cars)

print(cars)

cars.insert(1,"Jeep")
print(cars)

cars.append("Benz")
print(cars)

y = cars.pop()
print(y)

print('*#'*20)
cars.sort()
print(cars)
length=len(cars)
print(length)