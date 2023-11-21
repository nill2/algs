import random

class testClass:
    def __init__(self,inputList):
        self.myList = inputList
        
    def Sample(self):
        values = []
        weights = []
        for i in self.myList:
            values.append(i[0])
            weights.append(i[1])
        
        print(random.choices(values, weights))
        
if __name__ == '__main__':
    testSapmle = [["a",0.1],["b",0.2],["c",0.7]]
    test_c = testClass(testSapmle)
    test_c.Sample()