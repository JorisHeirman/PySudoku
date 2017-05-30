import json

WIDTH = 9
FULLSUDOKU = {1, 2, 3, 4, 5, 6, 7, 8, 9}
FILE = 'sudoku1.json'
FILL = "x"
matrix = [[FILL]*WIDTH for i in range(9)]
borders = [2,5,8]
counter = 0

class Sudoku:

    def __init__(self):
        self.matrix = [[FILL]*WIDTH for i in range(WIDTH)]
        with open(FILE) as data_file:
            json_object = json.load(data_file)
            for key in json_object:
                value = json_object[key]
                for v in value:
                    self.setNumber(int(key), int(v), int(value[v]))

    def printCanvas(self):
        for i in range(WIDTH):
            print ""
            for j in range(WIDTH):
                print self.matrix[i][j],

    def setNumber(self, x, y, number):
        self.matrix[x][y] = number

    def isNumber(self , x , y):
        try:
            value = self.matrix[x][y]
            if value == FILL:
                return False
            else:
                return True
        except Exception as e:
            return False

    def listHorizontalLine(self, x):
        nums = []
        for i in range(WIDTH):
            value = self.matrix[x][i]
            if (value != FILL):
                nums.append(value)
        return nums

    def listVerticalLine(self, y):
        nums = []
        for i in range(WIDTH):
            value = self.matrix[i][y]
            if (value != FILL):
                nums.append(value)
        return nums

    def findSquare(self, x, y):
        nums =[]
        for b in borders:
            for bo in borders:
                if x <= b and y <= bo:
                    nums = [b, bo]
                    return  nums
        return False


    def listSquare(self, coordinate):
        z = coordinate[0]+1
        a = coordinate[1]+1
        x = coordinate[0]-2
        y = coordinate[1]-2
        nums = []
        for i in range( x, z):
            for j in range(y, a):
                value = self.matrix[i][j]
                if (value != FILL):
                    nums.append(value)
        return nums

    def search(self, x, y):
        horizontal = set(self.listHorizontalLine(x))
        vertical = set(self.listVerticalLine(y))
        square = set(self.listSquare(self.findSquare(x,y)))
        result = (horizontal | vertical | square)
        numbers = FULLSUDOKU - result
        if len(numbers) == 1:
            number =  numbers.pop()
            return number
        return False

    def startSolve(self):
        for i in range(WIDTH):
            for j in range(WIDTH):
                if not self.isNumber(i, j):
                    k = self.search(i , j)
                    if not k:
                        print ""
                    else:
                        self.setNumber(i , j , k)
