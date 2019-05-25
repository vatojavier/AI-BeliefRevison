from itertools import chain, combinations
class Agent:
    KB = []

    def __init__(self, *arg):

        for disjunction in arg:
            self.KB.append(disjunction)

    def addformula(self, formula):
        if formula not in self.KB:
            self.KB.append(formula)

    def revision(self):
        a = []
        p = self.powerset(self.KB)
        #a.append(*p)

        for i in p:
            #print(type(list(i)))
            a.append(list(i))   #Maybe remove list(i)
            #print(type(a))

        print(a)
        return a

    def powerset(self,iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

