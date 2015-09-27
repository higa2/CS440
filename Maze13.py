import urllib2

class Maze:
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
        self.height = i #set the height
        self.width = j #set the width
        
        # if there is a wall to the right of the ghost
        if self.maze[ghostState[0]][ghostState[1]+1] == '%':
            self.ghostDirection = -1
        
    def findChildren(self, node):
        '''
        Finds children of a node in maze.
        Input: Current node
        
        ed Output: none
        Returns: List of children
        '''
        children = []
        x = node[1]
        y = node[0]
        
        #check if the left child valid and add to the list
        #player is moving left
        if x-1 >= 0:
            if self.maze[y][x-1] != '%': 
                if (y,x-1) != (ghostState + (0,ghostDirection)):
                    if (y,x) != (ghostState + (0,ghostDirection)):
                        children.append((y,x-1))
        
        #check if the upwards child valid and add to the list
        #player is moving up
        if y-1 >= 0:
            if self.maze[y-1][x] != '%': 
                if (y,x) != (ghostState + (0,ghostDirection)):
                    children.append((y-1,x))
        
        #check if the right child valid and add to the list
        #player is moving right
        if x+1 < self.width:
            if self.maze[y][x+1] != '%':
                if (y,x+1) != (ghostState + (0,ghostDirection)):
                    if (y,x) != (ghostState + (0,ghostDirection)):
                        children.append((y,x+1))

        #check if the downward child is valid and add to the list
        #player is moving down
        if y+1 < self.height:
            if self.maze[y+1][x] != '%':
                if (y,x) != (ghostState + (0,ghostDirection)):
                    children.append((y+1,x))
                
        #update ghostState, ghostDirection should already have the correct next move direction
        #and not hit walls
        ghostState = ghostState + (0,ghostDirection)
        
        #update ghostDirection
        if self.maze[ghostState[0]][ghostState[1]+ghostDirection] == '%':
            ghostDirection = ghostDirection * (-1)
        
        return children
    
    def changeMazeWithPath(self, path):
        '''
        prints the maze with the path
        input: sequence of nodes representing the path taken by the algorithm from start to goal.
        printed output: printed maze with path as a sequence of "."
        return: none
        '''
        for row in range(self.height):
            for col in range(self.width):
                if (row,col) in path:
                     self.maze[row][col] = "."
                        
    def printMaze(self):
        for row in range(self.height):
            for col in range(self.width):
                print self.maze[row][col],
            print " "