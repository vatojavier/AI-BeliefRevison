from itertools import chain, combinations


class Agent:
    KB = []

    def __init__(self, *arg):

        for disjunction in arg:
            self.KB.append(disjunction)

    def addformula(self, formula):
        if formula not in self.KB:
            self.KB.append(formula)

    def revision(self, p):
        """Does resolution with all the subsets of the KB, when finding one subset with empty clause:
           set KB to it and add p"""

        remainders = []
        p = self.powerset(self.KB)  # All subsets of KB

        for i in p:
            print(list(i))
            if self.resolution(list(i), p):
                remainders.append(list(i))   # Its a remainder

        return remainders

    #  Replace with Zeeshan's code
    def resolution(self, kb, p):
        """Checks whether the new formula is logically entailed by the KB resolution(KB,not(p)):
            if resolution gives empty clause (TRUE), p is consistent and expansion is done,
            otherwise, Revision is done"""

        #if empty clause:
            #expansion(p)
        #else:
            #revision(p)
        pass


    @staticmethod
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

