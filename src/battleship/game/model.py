'''
Created on Jan 21, 2010

@author: victorhg
'''
class Position():
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Board:
    def __init__(self, numRows, numColumns):
        self.numRows = numRows
        self.numColumns = numColumns
        self.positions = dict.fromkeys(range(0, numRows*numColumns), False)
    
    def hitAtPosition(self, position):
        index = self.convertToIndex(position.row, position.column)
        isAlive = self.positions[index]
        if isAlive:
            self.positions[index] = False
        return isAlive
    
    def hastBoatsAlive(self):
        self.count = 0
        def countAliveCells(cell):
            if self.positions[cell]:
                self.count += 1
        map(countAliveCells, self.positions )
        return self.count > 0
    
    def __str__(self):
        strPrint = ""
        for cell in self.positions:
            if not self.positions[cell]:
                alive = '-'
            else:
                alive = '#'
        
            value = self.getColumnIndex(cell)
            if value == (self.numColumns - 1):
                alive += '\n'
            else:
                alive += ' '
        
            strPrint += alive
        strPrint += '\n'
        return strPrint
    
    def setBoatPosition(self, position):
        self.positions[self.convertToIndex(position.row, position.column)] = True;
        
    def convertToIndex(self, row, column):
        return (row * self.numColumns) + column
    
    def indexToRowColumn(self, index):
        rowIndex = index / self.numColumns
        columnIndex = index % self.numColumns
        return rowIndex, columnIndex
        
    
    def getRowIndex(self, position):
        rowIndex = position / self.numColumns
        return rowIndex

    def getColumnIndex(self, position):
        columnIndex = position % self.numColumns
        return columnIndex