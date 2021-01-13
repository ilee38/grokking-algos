#!/usr/bin/env python3

"""
  Simple recursive function
"""

def factorial(num):
  if num <= 1:
    return 1
  else:
    return num * factorial(num - 1)


def main():
  print(factorial(5))


if __name__ == '__main__':
  main()