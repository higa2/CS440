class MazeSearch:
    '''
    Base class outlining functions that the inherited search classes should contain.
    Should not be created or implemented.
    '''
    def __init__(self, maze):
        '''
        Initializes the maze finding algorithm class. 
        input: A Maze object.
        output: none
        return: none
        '''
        self.frontier #number of nodes that are waiting to be visited
        self.pathCosts
        self.parent = [[(0,0) for j in range(self.maze.width)] for i in range(maze.height)]
        self.maze = maze
        self.numNodesVisited #keeps track of number of nodes visited.
        self.explored
        raise NotImplementedError #added this line so that an object from this class cannot be created.
    
    def pathFinder(self):
        '''
        Finds path in maze from initial state to goal state.
        input: none
        output: none
        return: returns a sequence of nodes in the maze representing a path and the path cost.
        '''
        self.addNodeToFrontier(self.maze.initialState, 0) #adds the initial node to the frontier
        while not self.emptyFrontier() :#checks if frontier is empty
            self.numNodesVisited+=1
            node, pathCost = self.chooseNodeFromFrontier()
            
            #check if goal state is reached
            if self.goalState(node):
                return self.backTrace(node), pathCost
            
            pathCost += 1 #update the path cost 
            #put the children of the current state on to the frontier.
            for child in self.maze.findChildren(node):
                if not self.duplicateDetection(child, pathCost):
                    self.addNodeToFrontier(child, pathCost)
                    self.parent[child[0]][child[1]] = node
                    self.explored.append(node)
        return -1
    
    def backTrace(self, node):
        '''
        Go back through the list of nodes that were visited and returns the path as a sequence of nodes from 
        goal to initial state.
        input: the goal state node.
        output: none
        return: the path from goal to initial state.
        '''
        path = []
        curNode = node
        
        #check the initial state has not been reached
        while curNode != self.maze.initialState:
            path.append(curNode) #add the current node to the path
            parent = self.parent[curNode[0]][curNode[1]]
            curNode = parent #go from the current node to the parent node.
        return path
    
    def duplicateDetection(self, node, pathCost):
        '''
        Implement strategy for detecting duplicate states.
        input: node
        printed output: none
        return: true if a duplicate of the node is detected and we do want to not add that node to the 
        frontier. 
        If a duplicate is detected and we want to keep the node on the frontier and remove the existing node, 
        the function returns false and change the frontier.
        '''
        raise NotImplementedError
    
    def addNodeToFrontier(self, node, pathCost):
        '''
        Adds node to the frontier. The data structure representing a frontier might differ
        for different search strategies.
        input: none
        printed output: none
        return: none
        '''
        raise NotImplementedError
        
    def chooseNodeFromFrontier(self):
        '''
        Implements a strategy for choosing a node from the frontier
        input: none
        printed: none
        return: node chosen by strategy and the path cost 
        '''
        raise NotImplementedError
        
    def emptyFrontier(self):
        '''
        Checks if the frontier is empty.
        input: none
        printed output: none
        return: true if the frontier is empty
        '''
        raise NotImplementedError
        
    def goalState(self, node):
        '''
        Checks if the goal state has been reached
        '''
        raise NotImplementedError
        
    def nodesVisited(self):
        '''
        Returns the number of nodes visited to solve the maze.
        '''
        return self.numNodesVisited