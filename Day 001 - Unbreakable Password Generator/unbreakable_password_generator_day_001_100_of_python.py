# -*- coding: utf-8 -*-
"""Unbreakable Password Generator - Day 001/100 of Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IymtdyCaYBaHMNnMJOxSVNJwFM-V1g0

<h1>Password Generator Recipe</h1>
"""

print('''
🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑
\t\tWelcome to Unbreakable Password Generator!
We will help you find your best of the best password for all of your accounts.
🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑
''')

firstName = str(input('What is your first name?\nType here: ')).lower()
lastName = str(input('What is your last name?\nType here: ')).lower()
birthMonth = str(input('In what month you were born?\nType here: ')).lower()
gender = str(input('Female/Male?\nType here: ')).lower()
favAnimal = str(input('What is your favourite animal?\nType here: ')).lower()
number = int(input('What is your last 2 digits phone number?\nType here: '))
progLang = str(input('What is your favourite programming language?\nType here: ')).lower()

username = firstName[0] + firstName[-1] + lastName[-2] + lastName[1] + favAnimal + gender[0] + progLang[::-1] + birthMonth[-2:] + str(number)

username