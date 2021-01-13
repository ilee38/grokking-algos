#!/usr/bin/env python3

"""
  Implementation of the selection sort algorithm.
  Note: selection sort is pretty bad! O(n^2) runtime
"""

def selection_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(i+1, len(arr)):
      if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr


def main():
  print(selection_sort([5,3,6,2,10,4,9,0,1,7,2,8,4]))


if __name__ == '__main__':
  main()
