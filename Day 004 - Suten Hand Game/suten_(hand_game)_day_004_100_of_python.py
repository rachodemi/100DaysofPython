# -*- coding: utf-8 -*-
"""Suten (Hand Game) - Day 004/100 of Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VAPUrwAVIuf_lssbWQItllN_-AhBc3_
"""

# Suten (Hand Game)
# Thumb -> Elephant
# Index Finger -> Human
# Pinkie -> Ant

import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

lst = ['Thumb','Index Finger','Pinkie']

player = random.choice(lst)
computer = random.choice(lst)

if player == 'Thumb' and computer == 'Index Finger':
  print(f'You got {player}!')
  img = mpimg.imread('elephant.png')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('human.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print('Elephant vs Human.....')
  print('You win!')
elif computer == 'Thumb' and player == 'Index Finger':
  print(f'You got {player}!')
  img = mpimg.imread('human.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('elephant.png')
  imgplot = plt.imshow(img)
  plt.show()
  print('Human vs Elephant.....')
  print('You lose.')
elif player == 'Index Finger' and computer == 'Pinkie':
  print(f'You got {player}!')
  img = mpimg.imread('human.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('ant.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print('Human vs Ant.....')
  print('You win!')
elif computer == 'Index Finger' and player == 'Pinkie':
  print(f'You got {player}!')
  img = mpimg.imread('ant.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('human.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print('Ant vs Human.....')
  print('You lose.')
elif player == 'Pinkie' and computer == 'Thumb':
  print(f'You got {player}!')
  img = mpimg.imread('ant.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('elephant.png')
  imgplot = plt.imshow(img)
  plt.show()
  print('Ant vs Elephant.....')
  print('You win!')
elif computer == 'Pinkie' and player == 'Thumb':
  print(f'You got {player}!')
  img = mpimg.imread('elephant.png')
  imgplot = plt.imshow(img)
  plt.show()
  print(f'Computer got {computer}!')
  img = mpimg.imread('ant.jpg')
  imgplot = plt.imshow(img)
  plt.show()
  print('Elephant vs Ant.....')
  print('You lose.')