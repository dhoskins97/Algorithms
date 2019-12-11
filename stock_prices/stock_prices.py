#!/usr/bin/python

import argparse

def find_max_profit(prices):
  biggest = 1
  smallest = 0
  for i in range(1, len(prices)):
    if prices[biggest] < prices[i]:
      biggest = i
  
  for i in range(0, biggest):
    if prices[smallest] > prices[i]:
      smallest = i

  return prices[biggest] - prices[smallest]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))