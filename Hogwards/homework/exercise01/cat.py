# -*- coding: utf-8 -*-
# @Time   :2021-01-29 16:06
# @Author :zhulihua
# @File   :cat.py

from Hogwards.homework.exercise01.animal_exercise import Animal
class Cat(Animal):
    def __init__(self):
        self.kind = 'short hair'
        super().__init__('Harry')
    #在子类中添加新方法 catch_mouse
    def catch_mouse(self):
        print(f'{self.name}会捉老鼠')
    #重写你类的 speak()方法
    def speak(self):
        pirnt(f'{self.name}会喵喵叫')
if __name__ == '__main()__':
    cat = Cat()
    cat.speak()
