#!/usr/bin/env python3

def binary_search(list, item):
  lo = 0
  hi = len(list) - 1

  while lo <= hi:
    mid = (lo + hi) // 2
    guess = list[mid]
    if guess == item:
      return mid
    elif guess > item:
      hi = mid - 1
    else:
      lo = mid + 1
  return None


def main():
  list = [1, 3, 5, 7, 9]
  print(binary_search(list, 3))
  print(binary_search(list, -1))


if __name__ == "__main__":
  main()