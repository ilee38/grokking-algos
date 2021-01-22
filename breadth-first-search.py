#!/usr/bin/env python3

"""
  BFS algorithm on a graph

"""
from collections import deque

def bfs(graph, start_node):
  done = set()
  search_queue = deque()
  search_queue.append(start_node)

  while search_queue:
    element = search_queue.popleft()
    if element not in done:
      if is_seller(element):
        return element
      else:
        done.add(element)
        search_queue += graph[element]
  return None


def is_seller(element):
  if element == 'thom':
    return True
  return False


def main():
  graph = {}
  graph['you'] = ['alice', 'bob', 'claire']
  graph['alice'] = ['peggy']
  graph['bob'] = ['anuj', 'peggy']
  graph['claire'] = ['johnny', 'thom']
  graph['anuj'] = []
  graph['peggy'] = []
  graph['johnny'] = []
  graph['thom'] = []

  print(bfs(graph, 'you'))


if __name__ == '__main__':
  main()

