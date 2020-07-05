import math
from queue import PriorityQueue


#I used the idea in here https://dbader.org/blog/priority-queues-in-python

def shortest_path(graph, start, goal):
    
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)
    
    prev = {start: None}
    score = {start: 0}

    while not pathQueue.empty():
        curr = pathQueue.get()

        if curr == goal:
            generatePath(prev, start, goal)

        for node in graph.roads[curr]:
            updateScore = score[curr] + heuristicMeasure(graph.intersections[curr], graph.intersections[node])
            
            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + heuristicMeasure(graph.intersections[curr], graph.intersections[node])
                pathQueue.put(node, totalScore)
                prev[node] = curr

    return generatePath(prev, start, goal)


#returning distance from start to goal
def heuristicMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def generatePath(prev, start, goal):
    curr = goal
    path = [curr]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path