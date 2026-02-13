import random


class Student:


   def __init__(self, name, year):
       self.name = name
       self.year = year
       self.skills = 5
       self.money = random.randint(100, 500)


   def hello(self):
       print(f'Hi. My name is {self.name}! I am {self.year}')
       print(f'My skills is {self.skills:.2f}')
       print(f'i have {self.money} ₴')


   def grow_up(self):
       self.year += 1


   def study(self):
       self.skills += 0.3




   def chill(self):
       self.skills -= 0.2
       expenses = random.randint(100, 500)
       self.money -= expenses
       print(f'-{expenses} ₴')


   def work(self):
       self.skills += 0.1
       self.money += 500


mark = Student("Mark", 13)


for day in range(1,366):
   print(f'======= Day {day} =======')


   choise = random.randint(0,2)


   if choise == 0:
       mark.study()
       print('Studying...📗')
   elif choise == 1:
       mark.work()
       print('Working...🦺')


   else:
       mark.chill()
       print('Chilling...😎')






mark.grow_up()
mark.hello()



