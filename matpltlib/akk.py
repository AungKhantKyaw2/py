# import calendar
# utensil = {"cup", "bowl", "spoon"}
# dishes = {"knife", "folk", "plate", "cup", "bowl"}
# yy=2024
# mm=12
# print(calendar.month(yy,mm))
# utensil.add("aung")
# utensil.remove("spoon")
# dishes.update(utensil)
# dinner_table = utensil.union(dishes)
# print(dishes.difference(utensil))
# print(dishes.intersection(utensil))
# dishes.intersection_update(utensil)
# print(dishes)
# for x in dinner_table:
#     print(x)
#
# name= "AungGod"
# first_name= name[0:].upper()
# last_chracter = name[-1]
# print(first_name)
# print(last_chracter)

# def hello(name1,name2,age):
#     print("have a nice day")
#     print(name1+"God"+name2+"\ooo"+str(age))
# hello("Aung","Pro player",1)
# def show(a1,a2,a3):
#     print("Aung"+a1+a3+a2)
# show(a1="is",a3="player",a2="dota2")

# def add1(*stuff):
#     Sum1 = 0
#     stuff = list(stuff)
#     stuff[1]=0
#     for i in stuff:
#         Sum1 += i
#     return Sum1

# def hello(**aung):
#     print("Hello")
#     for key,value in aung.items():
#         print(key)
# hello(title= "aung",name= "Khant",A="kyaw")

#str formnat
# animal="cow"
# item="moon"
# print("the {} jumped over the {}".format(animal,item))
# print("the {1} jumped over the {0}".format(animal,item))
# print("the {animal} jumped over the {item}".format(animal='cow',item='moon'))
#
# text= "the {} jumped over the {}"
# print(text.format(item,animal))
# name = "Aung"
# print("hello ,my name is {}".format(name))
# print("Hello, my name is {0:10}.nice to meet u".format(name))
# print("Hello, my name is {:<10}.nice to meet u".format(name))
# print("Hello, my name is {:>10}.nice to meet u".format(name))
# print("Hello, my name is {:^10}.nice to meet u".format(name))
# number = 3100
# print("the number is {:.3f}".format(number)) # 3 decimal digits
# print("the number is {:,}".format(number)) #thousands spearator
# print("the number is {:b}".format(number))# binary
# print("the number is {:o}".format(number))# octal
# print("the number is {:x}".format(number))#hexadecimal
# print("the number is {:E}".format(number))#scientific notation
#
# import random
# x=random.randint(1,6)
# z=random.random()#floating point 0 to 1
# y=random.uniform(0,10) # floating point 0 to 10
# print(y,x)
# Mylist=[1,2,3]
# a= random.choice(Mylist)
# print(a)
# cards =[1,2,3,4,5,6,7,8,9,10,"J","K","Q","A"]
# random.shuffle(cards)
# print(cards)

#expection= event detected during excution that interrupt  the flow of a program
# try:
#     numerator=int(input("enter the number to divide:"))
#     denominator=int(input("enter the number divide by"))
#     result= numerator/denominator
# except ZeroDivisionError as a:
#     print(a)
#     print("u cant divide by zero!")
# except ValueError as a:
#     print(a)
#     print("enter only number")
# except Expection as a:
#     print(a)
#     print("something wrong! Try again. ")
# else:
#     print(result)
# finally:
#     print("This will alaways execute")
# #
# import os
# path = "C:\\Users\\USER\\Documents\\test"
# if os.path.exists(path):
#     print("The location exists")
#     if os.path.isfile(path):
#         print("this is the file")
#     if os.path.isdir(path):
#         print("this is the directory")
# else:
#     print("the location not exist")
# import os

# Define the directory path
# import os
# path = "C:\\Users\\USER\\Documents\\test.txt"
#
# # Check if the directory exists
# if os.path.exists(path):
#     print("The location exists")
#
#     # Check if the path is a file
#     if os.path.isfile(path):
#         print("This is a file")
#
#     # Check if the path is a directory
#     elif os.path.isdir(path):
#         print("This is a directory")
#
# else:
#     # If the directory does not exist, create it
#     os.makedirs(path)
#     print("Created directory:", path)
#
# # Create the file "text.txt" in the directory
# file_path = os.path.join(path, "text.txt")
# with open(file_path, "w") as file:
#     file.write("This is a new text file.")
#     print("Created file:", file_path)
# try:
#     with open('C:\\Users\\USER\\Documents\\test\\text.tx') as file:
#         print(file.read())
# except FileNotFoundError:
#         print("the  file is not found")
# # print(file.closed)
# t1="anjing dog"
# # with open('test.txt','w') as file:
# #     file.write(t1)
# with open('test.txt','a') as file:
#     file.write(t1)
# import shutil
# t1= 'i am god'
# shutil.copyfile('test.txt','content.txt')
# shutil.copy2('test.txt','C:\\Users\\USER\Documents\\test1.txt')
# with open('C:\\Users\\USER\Documents\\test1.txt','a') as file:
#     file.write(t1)
# shutil.copy2('C:\\Users\\USER\Documents\\test1.txt','C:\\Users\\USER\\PycharmProjects\\pythonProject')
# import os
# source="folder"
# destination="C:\\Users\\USER\\folder"
#
# try:
#     if os.path.exists(destination):
#         print("there is destination file")
#     else:
#         os.replace(source,destination)
#         print("the file is removed")
# except  FileNotFoundError:
#     print(source+"was removed")

import os
# import shutil
#
# path ="folder"
# try:
#     # os.remove(path) # remove path doesn't remove empty folder
#    # os.rmdir(path) # remove directory
#      shutil.rmtree(path)# delete entring file containing other sub file
# except FileNotFoundError:
#     print("there is no file")
# except PermissionError:
#     print("you do not have permission to delete")
# except OSError:
#     print("you cannot using that file with this function")
# else:
#     print(path+"was deleted")

# import messages
# messages.bye()
# messages.hello()
# import messages as msg
# msg.bye()
# msg.hello()

# from messages import hello,bye
# from messages import*
# bye()
# hello()
# help("modules")

import random
# choices = ['rock','scissors','paper']
# while True:
#       computer = random.choice(choices)
#       player = None
#
#       while player not in choices:
#             player = input("rock or scissors or paper?:").lower()
#       if player == computer:
#          print("computer",computer)
#          print("player",player)
#          print("Tie")
#       elif player == "rock":
#            if computer == "scissors":
#             print("computer", computer)
#             print("player", player)
#             print("player win!")
#       if computer == "paper":
#             print("computer", computer)
#             print("player", player)
#             print("player lose!")
#       elif player == "scissors":
#            if computer == "paper":
#                print("computer", computer)
#                print("player", player)
#                print("player win!")
#            if computer == "rock":
#                print("computer", computer)
#                print("player", player)
#                print("player lose!")
#       elif player == "paper":
#              if computer == "rock":
#                print("computer", computer)
#                print("player", player)
#                print("player win!")
#              if computer == "scissors":
#                print("computer", computer)
#                print("player", player)
#                print("player lose!")
#       play_again = input("play again or not (Yes/No?)").lower()
#
#       if play_again == "no":
#             break
#
# print("Bye")
# def new_game():
#     guesses= []
#     correct_guess=0
#     question_num = 1
#     for b in question.keys():
#         print("---------------")
#         print(b)
#         for a in option[question_num-1]:
#             print(a)
#         guess=input("Enter(A,B,C,D)")
#         guess = guess.upper()
#         guesses.append(guess)
#         correct_guess += check_answer(question.get(b), guess)
#         question_num += 1
#     display_score(correct_guess , guesses)
#
# #
# def check_answer(answer, guess):
#     if answer == guess:
#         print("CORRECT")
#         return 1
#     else:
#         print("wrong!")
#         return 0
# def display_score(correct_guess, guesses):
#     print("-------------------")
#     print("RESULTS!")
#     print("----------------")
#     print("ANSWERS:" ,end="")
#     for i in question:
#         print(question.get(i), end=" ")
#     print()
#     print("Guesses:", end=" ")
#     for i in guesses:
#         print(i,end=" ")
#     print()
#     score =int((correct_guess/len(question))*100)
#     print("your score is" +str(score)+"%")
#
# def play_again():
#     response =  input('Do u want to answer again!(YES/NO)')
#     response=response.upper()
#     if response== "YES":
#         return True
#     else:
#         return False
#
#
# question={
# 'who created the Python?' : 'A',
# 'what is python created' : 'B',
# 'python is tributed to which cedy group' : 'C',
# 'Is earth around?' : 'D'
# }
#
# option =[
# ["A.A1","B.B1" ,"C,C1" ,"D,D1"],
# ["A.B2" ,"B.B2","C.C2" ,"D.D2"],
# ["A.A3" ,"B.B3" ,"C.C3" ,"D.D3"],
# ["A.A4" ,"B.B4", "C.C4", "D.D4"]
# ]
# new_game()
#
# while play_again():
#     new_game()
#
# print("Bye")

# from classfile import Car
# car_1 = Car("Chevy", "Corvette", 2021, "blue")
# car_2 = Car("Ahevy", "Aorvette", 2022, "Ylue")
# # print(car_1.make)
# # print(car_1.color)
# # print(car_2.year)
# # print(car_1.model)
# car_1.wheel =2
# # car_1.stop()
# # car_1.drive()
# # car_2.drive()
# print(car_1.wheel)
# print(car_2.wheel)

# class Animal:
#
#     def __init__(self, alive, variety ,Generic):
#         self.alive = alive  # Set the alive attribute
#         self.variety = variety  # Set the variety attribute
#         self.Generic = Generic
#     def eat(self):
#         print(f"The {self.variety} is eating.")
#         print(f"the {self.alive}")
#
#     def sleep(self):
#         print(f"The {self.variety} is sleeping.")
#         print(f"the {self.alive}")
#
#
# class Rabbit(Animal):
#     variety = "Rabbit"
#     alive = "alive"
#
# class Fish(Animal):
#     variety = "Fish"
#     alive = "alive"
#
# class Hawk(Animal):
#     variety = "Hawk"
#     alive = "alive"
# rabbit = Rabbit("alive", "Rabbit","Generic")
# fish = Fish("alive", "Fish","Generic")
# hawk = Hawk("alive", "Hawk","Generic")
#
# fish.eat()
# hawk.eat()
# print(fish.alive)
#
# class Animal:
#     alive = True
#     def eat(self):
#         print(f"The animal  is eating.")
#
#
#     def sleep(self):
#         print(f"The animal is sleeping.")
#
#
# class Rabbit(Animal):
#       def run(self):
#           print("the rabbit is running")
#
# class Fish(Animal):
#       def swim(self):
#           print("the fish is swimming")
# class Hawk(Animal):
#       def fly(self):
#           print("The hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()
#
# class Organism:
#     alive =True
#
# class Animal(Organism):
#      def eat(self):
#         print("the dog is eatiing")
#
# class Dog(Animal):
#      def bark(self):
#         print("the dog is barking")
#
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()
#
#
# class Prey:
#
#       def flee(self):
#           print("the animal flees")
#
# class Predator:
#
#       def hunt(self):
#           print("the animal is hunting")
#
# class Rabbit(Prey):
#        pass
#
# class  Hawk(Predator):
#        pass
#
# class  Fish(Prey,Predator):
#        pass
#
# rabbit = Rabbit()
#
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.hunt()

# class Car:
#
#     def turn_on(self):
#         print("You start the Enginee")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the Enginee")
#         return self
#
# car = Car()
#
# car.turn_on()\
#     .turn_off()\
#     .brake()\
#     .drive()
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#     def __init__(self, length,width):
#         super().__init__(length, width)  # Square has equal length and width
#
#     def area(self):
#         return self.length * self.width  # Area of square is length squared
#
# class Cube(Rectangle):
#     def __init__(self, length,width, height):
#         super().__init__(length,width)  # Cube has equal length, width, and height
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height  # Volume of cube is length squared times height
#
# # Create instances
# area1 = Square(2,2)
# volume1 = Cube(2, 2,2)
#
# # Calculate and print area and volume
# print("Area of the square:", area1.area())
# print("Volume of the cube:", volume1.volume())

#
# print(area1.area())
# print(volume1.volume())
#
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def go(self):
#         print("you drive the car")
#     def stop(self):
#         print("you stop the car")
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You ride the motorcycle")
#
#     def stop(self):
#         print("You ride the motorcycle")
#
# # vehicle= Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()
#
# class Car:
#       color = None
# class Motocycle:
#       color = None
# def changecolor(vehicle,color):
#     vehicle.color = color
#
# Car_1 = Car()
# Car_2 = Car()
# Car_3 = Car()
# changecolor(Car_1,"The car is Red")
# changecolor(Car_2,"The car is Red")
# changecolor(Car_3,"The car is Red")
# bike_1 = Motocycle()
# bike_2 = Motocycle()
# bike_3 = Motocycle()
# changecolor(bike_1,"The motocycle is Red")
# changecolor(bike_2,"The motocycle is Red")
# changecolor(bike_3,"The motocycle is Red")
# print(Car_1.color)
# print(Car_2.color)
# print(Car_3.color)
# print(bike_1.color)
# print(bike_2.color)
# print(bike_3.color)
#
# class Duck:
#     def walk(self):
#         print("The duck is walking")
#     def talk(self):
#         print("The duck is qwuacking")
#
# class Chicken:
#     def walk(self):
#         print("The chicken is walking")
#     def talk(self):
#         print("The chicken is clucking")
#
# class Input:
#     def __init__(self, IN):
#         self.IN = IN
#
# class Person(Input):
#     alive = True
#
#     def __init__(self, IN):
#         super().__init__(IN.upper())  # Pass the input to the Input class constructor and convert to uppercase
#
#     def catch(self):
#         if self.IN != "CHICKEN":  # Access the input from the superclass
#             duck.talk()
#             duck.walk()
#             print("The duck is caught")
#         else:
#             chicken.talk()
#             chicken.walk()
#             print("The chicken is caught")
#
# # Create instances of the classes
# duck = Duck()
# chicken = Chicken()
#
# # Get input from the user
# IN = input("Say that you get ")
#
# # Create an instance of Person with the input
# person = Person(IN)
#
# # Call the catch method with the input
# person.catch()
# print(Person.alive)

#Warlus  operator  :=

# new to Python 3.8
# assignment expression aka warlus operator
#assigns values to variables as part of a larger expression

# foods = list()
# while True:
#     food = input("What food do u like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# foods = list()
# while food := input("what kinds of food do u like ?:") != "quit":
#     foods.append(food)
# print(foods)

# def hello():
#     print("hello")
# hi = hello
# print(hello)
# hi()
# print(hi)
#
# say = print
# say("WHO")
# a = 1
# def loud(text):
#     return text.lower()
# def soft(text):
#     return text.upper()
#
# def hello(func,func_name):
#     text = func("hello")
#     print(text)
#     print(f"ur use function is {func_name}")
#
# hello(loud,"loud")
# hello(soft,"soft")
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))
# def apply_operation(operation, x, y):
#     return operation(x, y)
#
# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# result1 = apply_operation(add, 5, 3)
# print("Result of addition:", result1)  # Output: 8
#
# result2 = apply_operation(subtract, 5, 3)
# print("Result of subtraction:", result2)  # Output: 2
#lambda arguments : expression #  x : x+2,iteration
#
# x=4
# even_value = lambda x:print(2) if x % 2 == 0 else None
# #
# even_value(x)
# double = lambda x:x+2
# multiply = lambda x,y : x*y
# add = lambda x,y,z : x+y+z
# division = lambda x,y,z : (x/y)/z
# full_name =lambda first_name , second_name: first_name+"      "+second_name
# age_check = lambda age : print("adult") if age > 18 else print("not adult")
# age_check(25)
# age_check1 = lambda age : True if age > 18 else False
# print(age_check1(18))
# sort() METHOD = USED WITH LIST
#sort() Function = used with iterables

# students =["aung","IY","IZY","Pro"]
# students.sort(reverse=True)
#
# for i in students:
#     print(i)
# in tuple
# students = ("aung", "IY", "IZY", "Pro")
# sorted_student = sorted(students,reverse=True)
#
# for i in students:
#     print(i)

#
# students = (("aung","F",0),
#             ("IY","D",20),
#             ("IZY","C",40),
#             ("Pro","A",100))
# grades = lambda grade:(grade[1],grade[2])
# students_sorted =sorted (students,key=grades,reverse=True)
# # age_mapping = {'F':20,'D':20,'C':40,'A':100}
# age_mapping = {0:20,20:40,40:60,100:80}
# for i in students_sorted:
#     print(i)
# for student in students_sorted:
#     name, grade, score = student
#     age = age_mapping[score]
#     print(f"{name}'s age is {age}")

#map function (function, iterable)

# store = [("shirt",20),
#          ("watch",200),
#          ("phone",500)]
# to_euro = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data :(data[0],data[1]/0.82)
#
# store_dollars = map(to_euro,store)
# for i in store_dollars:
#     print(i)
#filter(function,iterable)
# friends = [("Aung",19),
#            ("Kya",25),
#            ("Min",36),
#            ("Khaing Gyi",30)
#         ]
# age = lambda data: data[1]>= 18
#
# drinking_buddies = list(filter(age,friends))
#
# for i in drinking_buddies:
#     print(i)
#reduce()=apply a function to iterable and reduce it  to a single cumulmative value
#reduce(function,iterable)

# import functools
# # letters = ["H","E","L","L","O"]
# # word = functools.reduce(lambda x,y:x+y,letters)
# # print(word)
# factorial = [5,4,3,2,1]
# number = functools.reduce(lambda x,y: x*y , factorial)
# print(number)

#list comprehension
#lsit =[expression for  item iterable ]
#list =[expression for item iterable if conditional]
#list = [expression if/else for item iteralbe]
# square = []
# for i in range(1,11,2):
#     square.append(i*i)
# print(square)
#
# squares = [i*i for i in range(1,11)]
# print(squares)

# students = [100,90,80,70,60,50,40,30,20,10,0]
#
# # passed_students = list(filter(lambda x: x >=60,students))
# # passed_students = [i for i in students if i >=60]
# passed_students = [i if i >=60 else "Failed" for i in students]
# print(passed_students)