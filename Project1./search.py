# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# # I based my A* searches on project one slides and looked up data sturctures on https://www.w3schools.com/python/python_lambda.asp

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    dfsStack = util.Stack()
    startState = problem.getStartState()

    if problem.isGoalState(startState):
        return None

    dfsStack.push((startState,[]))
    checked = []

    while not dfsStack.isEmpty():
        curr = dfsStack.pop()
        if curr[0] not in checked:
            if problem.isGoalState(curr[0]):
                return curr[1]
            checked.append(curr[0])
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                path = curr[1] + [(successor[1])] #add the previouse node explored to path
                dfsStack.push((successor[0],path))
                
    return None        
    #util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    bfsQ = util.Queue()
    startState = problem.getStartState()

    #if problem.isGoalState(startState):
    #    return None

    bfsQ.push((startState,[]))
    checked = []

    while not bfsQ.isEmpty():
        curr = bfsQ.pop()
        if curr[0] not in checked:
            if problem.isGoalState(curr[0]):
                return curr[1]
            checked.append(curr[0])
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                path = curr[1] + [(successor[1])] #add the previouse node explored to path
                bfsQ.push((successor[0],path))
                
    return None  


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    ucsPQ = util.PriorityQueue()
    startState = problem.getStartState()

    if problem.isGoalState(startState):
        return None

    ucsPQ.push((startState,[]), 0)
    checked = []

    while not ucsPQ.isEmpty():
        curr = ucsPQ.pop()
        if curr[0] not in checked:
            if problem.isGoalState(curr[0]):
                return curr[1]
            checked.append(curr[0])
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                path = curr[1] + [(successor[1])]
                cost = problem.getCostOfActions(path)
                ucsPQ.push((successor[0], path), cost)
    
    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    astarPQ = util.PriorityQueue()
    startState = problem.getStartState()

    if problem.isGoalState(startState):
        return None

    astarPQ.push((startState,[]), 0)
    checked = []

    while not astarPQ.isEmpty():
        curr = astarPQ.pop()
        if curr[0] not in checked:
            if problem.isGoalState(curr[0]):
                return curr[1]
            checked.append(curr[0])
            successors = problem.getSuccessors(curr[0])
            for successor in successors:
                path = curr[1] + [successor[1]]
                cost = problem.getCostOfActions(path)
                heu = heuristic(successor[0],problem)
                astarPQ.push((successor[0], path), cost + heu)

    return None

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
