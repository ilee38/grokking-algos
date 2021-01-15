#!/usr/bin/env python3

"""
  Quicksort algorithm
  Note: always choose the pivot's value randomly. This will ensure we get the
  average case runtime for quicksort O(n log n).
"""
def quicksort(arr):
  if len(arr) < 2:
    return arr

  pivot = arr[0]
  less_than_pivot = [i for i in arr[1:] if i <= pivot]
  greater_than_pivot = [i for i in arr[1:] if i > pivot]

  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


def main():
  print(quicksort([10,5,3,2]))


if __name__ == '__main__':
  main()