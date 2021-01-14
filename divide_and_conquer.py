#!/usr/bin/env python3

"""
  Divide and conquer section
"""

def recursive_sum(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  else:
    return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return 1
  else:
    return 1 + recursive_count(arr[1:])


def find_max(arr):
  if len(arr) == 0:
    return None
  elif len(arr) == 1:
    return arr[0]
  else:
    if arr[0] > find_max(arr[1:]):
      return arr[0]
    else:
      return find_max(arr[1:])


def main():
  print(recursive_sum([2,4,6]))
  print(recursive_count([2,4,6,5,7,8]))
  print(find_max([2,4,6,25,5,7,8]))


if __name__ == "__main__":
  main()