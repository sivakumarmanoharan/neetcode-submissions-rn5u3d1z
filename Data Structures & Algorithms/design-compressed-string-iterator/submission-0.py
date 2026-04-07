class StringIterator:

    def __init__(self, compressedString: str):
        '''
        1. Defined a map of strings to separate the number of chars as pairs [('N',1),('e',2)]
        '''
        self.str_map = [[m.group(1), int(m.group(2))] 
                        for m in re.finditer(r'([A-Za-z])(\d+)', compressedString)]
        self.index = 0  # pointer to current character
    def next(self) -> str:
        '''
        1. Using the map defined, checks the first string and how many times it is iterated. 
        2. If it is called once, the count would be decreased and returns the char
        3. Once the count becomes zero it iterates to the next character and returns it
        '''
        while self.index < len(self.str_map):
            char, count = self.str_map[self.index]

            if count > 0:
                self.str_map[self.index][1] -= 1
                return char
            else:
                self.index += 1

        return ' '  

    def hasNext(self) -> bool:
        '''
        1. This checks the map index, if it reaches the end of the list and checks the count. If it is zero, it returns False
        2. Else it returns true
        '''
        while self.index < len(self.str_map) and self.str_map[self.index][1] == 0:
            self.index += 1

        return self.index < len(self.str_map)



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
