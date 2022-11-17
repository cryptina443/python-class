#import
import math

def calc_buns(amount):
  '''Calculates minimum number of packets of buns and left over'''
  buns = 10
  min_packet_of_buns = total / buns
  round = math.ceil(min_packet_of_buns)
  left_over_bun = (buns * round) - total
  return round, left_over_bun
  
  
def calc_dogs(amount):
  '''Calculates minimum number of packages of hot dogs needed and left over'''
  dogs = 8
  min_packet_of_dogs = total / dogs
  round = math.ceil(min_packet_of_dogs)
  left_over_dogs = (dogs * round) - total
  return round, left_over_dogs


#main
if __name__ == '__main__':
  #accepts input from user
  num_people = int(input('How many people are attending the cookout? '))
  num_food = int(input('How many hot dogs will they be given? '))
  print()
  
  #calculates total, calls functions and assigns to multiple variables as there two function outputs
  total = num_people * num_food
  min_bun, left_bun  = calc_buns(total)
  min_dog, left_dog = calc_dogs(total)
  
  #displays info requested
  print(f'The minimum number of packages of hot dogs required: {min_dog}')
  print(f'The minimum number of packages of hot dog buns required: {min_bun}')
  print()
  print(f'The number of hot dogs that will be left over: {left_bun}')
  print(f'The number of hot dog buns that will be left over: {left_dog}')