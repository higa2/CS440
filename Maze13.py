import urllib2
from Maze import *

class MazeWithGhost(Maze):
    '''
    Creates a data structure to represent the maze problem.
    '''
    def __init__(self, txtFile):
        '''
        Initializes the maze as a two dimensional list.
        input: text file representing the maze
        printed output: none
        return: none
        '''
        i = 0 #row index
        data = urllib2.urlopen(txtFile)
        self.maze = []
        self.explored = []
        self.ghostState = []
        
        #ghostDirection will always have direction of next move
        self.ghostDirection = 1
        
        for line in data:
            j = 0 #column index
            self.maze.append([])
            for char in line:
                #labels goal state or goal states in maze
                if char == '.':
                    self.goal = (i,j)
                #labels initial state in maze
                elif char == 'P':
                    self.initialState = (i,j)
                elif char == 'G':
                    self.ghostState = (i,j)
                if char in ['P','.','%',' ','g','G']: 
                    self.maze[i].append(char)
                    j+=1
            i+=1
            
        #state is represented by y position, x position, ghost's y position, ghost's x position.    
        self.initialState = self.initialState + self.ghostState
        
        self.height = i #set the height
        self.width = j #set the width
        self.ghostDirection = 1 #initial direction of the ghost. +1 means the ghost is going right, -1 means the ghost is going left.
        
    def findChildren(self, node):
        '''
        Finds children of a node in maze.
        Input: Current node
        
        ed Output: none
        Returns: List of children
        '''
        children = []
        x = node[1] #agent's position
        y = node[0]
        g_x = node[3] #ghost's position
        g_y = node[2]
        
        #cut the path from the search if we ever run into a ghost
        if (y, x) == (g_y, g_x):
            return children
        
        #keep the ghost in walls.
        if self.maze[g_y][g_x+1] == '%':
            self.ghostDirection = -1
        elif self.maze[g_y][g_x-1] == '%':
            self.ghostDirection = 1
        
        #check if the left child valid and add to the list
        #player is moving left
        if x-1 >= 0:
            if self.maze[y][x-1] != '%': 
                children.append((y ,x-1 ,g_y, g_x + self.ghostDirection))
        
        #check if the upwards child valid and add to the list
        #player is moving up
        if y-1 >= 0:
            if self.maze[y-1][x] != '%': 
                children.append((y-1 ,x ,g_y, g_x + self.ghostDirection))
        
        #check if the right child valid and add to the list
        #player is moving right
        if x+1 < self.width:
            if self.maze[y][x+1] != '%':
                children.append((y ,x+1 ,g_y, g_x + self.ghostDirection))

        #check if the downward child is valid and add to the list
        #player is moving down
        if y+1 < self.height:
            if self.maze[y+1][x] != '%':
                children.append((y+1 ,x ,g_y, g_x + self.ghostDirection))
        
        return children
    
    def changeMazeWithPath(self, path):
        '''
        prints the maze with the path
        input: sequence of nodes representing the path taken by the algorithm from start to goal.
        printed output: printed maze with path as a sequence of "."
        return: none
        '''
        agentPath = []
        ghostPath = []
        for node in path:
            #separate player path
            agentPath.append((node[0], node[1]))
            
            #separate ghost path:
            ghostPath.append((node[2], node[3]))
        
        #change the maze representation to include the path.
        for row in range(self.height):
            for col in range(self.width):
                if (row,col) in agentPath:
                     self.maze[row][col] = "."
                if (row, col) == ghostPath[-1]:
                    self.maze[row][col] = 'G'
                elif (row, col) in ghostPath:
                    self.maze[row][col] = "g"

    def printImagesForGIF(self, path):
        #print one at a time
        i = 0
        for node in path:
            changeMazeWithPath([node])
            
                        
    def printMaze(self):
        for row in range(self.height):
            for col in range(self.width):
                print self.maze[row][col],
            print " "