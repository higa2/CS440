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
        self.paths
        self.maze = maze
        self.numNodesVisited #keeps track of number of nodes visited.
        self.explored
        raise NotImplementedError #added this line so that an object from this class cannot be created.
     
    def calculatePathCost ( self,node, child ):
        if node[2]==node[2]:
            return 1 #forwardCost
        else:
            return 1 #turnCost
        
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
            node, pathCost, path = self.chooseNodeFromFrontier()
            
            #check if goal state is reached
            if self.goalState(node):
                return path, pathCost
            
#             pathCost += 1 #update the path cost 
            #put the children of the current state on to the frontier.
            for child in self.maze.findChildren(node):
                newPathCost = pathCost
                newPathCost += self.calculatePathCost(node,child)  #change the last 2 parameters according to the heuristic function
                if not self.duplicateDetection(child, newPathCost):
                    self.addNodeToFrontier(child, newPathCost, path + (node,))
                    self.explored.append(node)
        return -1
    
   
                
    
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
    
class MazeSearch_12_2(MazeSearch):
    
    def calculatePathCost ( self,node, child ):
        if node[2]==node[2]:
            return 2 #forwardCost
        else:
            return 1 #turnCost
        
class MazeSearch_12_3(MazeSearch):
    
    def calculatePathCost ( self,node, child ):
        if node[2]==node[2]:
            return 1 #forwardCost
        else:
            return 2 #turnCost