# -*- coding: utf-8 -*-
# @Time   :2021-01-29 13:15
# @Author :zhulihua
# @File   :animal_exercise.py

class Animal:
    name = 'dog'
    color = 'brown'
    age = 3
    gender = 'female'
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
    #定义类方法
    def speak(self):
        print(f'{self.name} can speak')
    def run(self):
        print(f'{self.name} can run')

if __name__ == '__main__':
    #类的实例化
    animal = Animal('cici','white',5,'male')
    #调用类方法
    animal.speak()
    animal.run()
#print(f"animal's name is {animal.name},age is {animal.age},color is {animal.color},gender is {animal.gender}")



