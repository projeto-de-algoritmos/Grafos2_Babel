import sys
import heapq
import time

def create_edge(graph, node1, node2, word):
  if not graph.get(node1):
    graph[node1] = []

  graph[node1].append({
    'language': node2,
    'word': word
  })

def dijkstra(graph, start, target, socketio):
  distances = {}
  visited = {}

  for node in graph:
    distances[node] = {
      'distance': sys.maxsize,
      'word': None,
      'previous_node': None
    }
  
  try:
    distances[start]['distance'] = 0
  except KeyError:
    socketio.emit('update', {'ids': []})
    return []

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

        ids = []

        for distance in distances:
          if distances[distance]['word']:
            id = distances[distance]['word']
            ids.append(id)

        heapq.heappush(queue, (possibility, edge['language']))
        # socketio.emit('update', {'ids': ids})
        # time.sleep(1)




def create_path(start, goal, graph, socketio):
  distances = dijkstra(graph, start, goal, socketio)  
  ids = []

  if not (distances):
    socketio.emit('update', {'ids': []})
    return 'impossivel'
  
  node = distances[goal]['previous_node']
  path = []
  path.append(distances[goal])

  while node:
    path.append(distances[node])
    node = distances[node]['previous_node']

  for distance in path:
    if distance['word']:
      id = distance['word']
      ids.append(id)
  
  socketio.emit('update', {'ids': ids})
  return path


def build_and_solve(graph_data, socketio):
  graph = {}
  start = graph_data['start']
  goal = graph_data['goal']

  for edge in graph_data['graph']:
    node1 = edge['node1']
    node2 = edge['node2']
    word = edge['word']

    create_edge(graph, node1, node2, word)
    create_edge(graph, node2, node1, word)

  create_path(start, goal, graph, socketio)




