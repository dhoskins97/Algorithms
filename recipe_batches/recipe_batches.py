#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  tracker = []
  for item in recipe:
    if item in ingredients:
      tracker.append(int(ingredients[item] / recipe[item]))
    else:
      tracker.append(0)

  smallest = 0
  for i in range(0, len(tracker)):
    if tracker[i] < tracker[smallest]:
      smallest = i
  
  return tracker[smallest]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))