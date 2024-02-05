
class strClass:
    def getString(self):
        self.input_string = input()
    def printString(self):
        print(self.input_string.upper())
str = strClass()
str.getString()
str.printString()
