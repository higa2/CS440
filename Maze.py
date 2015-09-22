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
                if char == 'P' or char == '.' or char == '%' or char == ' ': 
                    self.maze[i].append(char)
                    j+=1
            i+=1
        self.height = i #set the height
        self.width = j #set the width
        
    def findChildren(self, node):
        '''
        Finds children of a node in maze.
        Input: Current node
        Printed Output: none
        Returns: List of children
        '''
        children = []
        x = node[1]
        y = node[0]
        
        #check if the left child valid and add to the list
        if x-1 >= 0:
            if self.maze[y][x-1] != '%':
                children.append((y,x-1))
        
        #check if the upwards child valid and add to the list
        if y-1 >= 0:
            if self.maze[y-1][x] != '%':
                children.append((y-1,x))
        
        #check if the right child valid and add to the list
        if x+1 < self.width:
            if self.maze[y][x+1] != '%':
                children.append((y,x+1))

        #check if the downward child is valid and add to the list
        if y+1 < self.height:
            if self.maze[y+1][x] != '%':
                children.append((y+1,x))
        return children
    
    def printMazeWithPath(self, path):
        '''
        prints the maze with the path
        input: sequence of nodes representing the path taken by the algorithm from start to goal.
        printed output: printed maze with path as a sequence of "."
        return: none
        '''
        for row in range(self.height):
            for col in range(self.width):
                if (row,col) in path:
                    print ".",
                else:
                    print self.maze[row][col],
            print " "