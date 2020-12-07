import random
class SortingAlgorithm:
    def __init__(self, sets, Increase):
        self.increase = Increase
        self.sets = sets
    def BubbleSort(sets, Increase):
        if Increase is True:
            for j in range(1, len(sets)):
                for i in sets[0, j]:
                    if i > selts[sets.index(i) + 1]:
                        temp = sets[sets.index(i) + 1]
                        sets[sets.index(i) + 1] = i
                        sets[sets.index(i)] = temp
        else:
            for j in range(1, len(sets)):
                for i in sets[0, j]:
                    if i < sets[sets.index(i) + 1]:
                        temp = sets[sets.index(i) + 1]
                        sets[sets.index(i) + 1] = i
                        sets[sets.index(i)] = temp
        return(sets)
    def QuickSort(sets, Increase):
        if Increase is True:
            for i in range(0, 888):
                j = random.choice(sets)
                lessset = []
                moreset = []
                for m in sets:
                    if m <= j:
                        lessset.append(m)
                    else:
                        moreset.append(m)
                sets = lessset
                for i in moreset:
                    sets.append(i)
            return(sets)
        else:
            for i in range(0, 888):
                j = random.choice(sets)
                lessset = []
                moreset = []
                for m in sets:
                    if m <= j:
                        lessset.append(m)
                    else:
                        moreset.append(m)
                sets = moreset
                for i in lessset:
                    sets.append(i)
            return(sets)

class Sort(SortingAlgorithm):
    pass
    
            
sets = [1, 3, 2, 6, 4, 8, -5, 3.5, 13, 8]
sets = Sort.QuickSort(sets, True)
print(sets)

#below is online example, above is my own
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False
    def introduce_self(self):
        print("my name is " + self.name)

r2= Person("Tom", "sweet", False)
r1 = Person("Jerry", "friendly", True)
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_own = r2
p2.robot_own = r1

# print(p1.robot_own.introduce_self())

"""Try except finally code"""
try:
    print(param)
except NameError:
    print("This var is undefined.")
finally:
    print("This code has been executed.")
