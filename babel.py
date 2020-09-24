import sys
import heapq

def create_edge(graph, node1, node2, word):
  if not graph.get(node1):
    graph[node1] = []

  graph[node1].append({
    'language': node2,
    'word': word
  })





def dijkstra(graph, start, target):
  distances = {}
  visited = {}

  for node in graph:
    distances[node] = {
      'distance': sys.maxsize,
      'word': None,
      'previous_node': None
    }

  distances[start]['distance'] = 0

  for node in graph:
    visited[node] = False

  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    node = heapq.heappop(queue)[1]

    if visited[node]:
      continue
      
    if node == target:
      return distances

    for edge in graph[node]:

      possibility = distances[node]['distance'] + len(edge['word'])
      current_weight = distances[edge['language']]['distance']

      if possibility < current_weight:
        distances[edge['language']]['distance'] = possibility
        distances[edge['language']]['word'] = edge['word']
        distances[edge['language']]['previous_node'] = node

        heapq.heappush(queue, (possibility, edge['language']))

n = int(input())

while n != 0:
  start, goal = map(str, input().split())

  graph = {}
  paths = []
  lengths = []


  for i in range(n):
    node1, node2, word = map(str, input().split())
    create_edge(graph, node1, node2, word)
    create_edge(graph, node2, node1, word)

  distances = dijkstra(graph, start, goal)
  print(distances)

