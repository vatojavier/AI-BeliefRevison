from itertools import chain, combinations


class Agent:
    KB = set()

    def __init__(self, *arg):

        for disjunction in arg:
            self.add_formula(disjunction)

    def add_formula(self, formula):
        """Basically this is Expansion"""

        formula = frozenset(formula)
        if not formula.issubset(self.KB):
            self.KB.add(formula)

    def agm_revison(self, formula):
        """Checks whether the new formula is logically entailed by the KB resolution(KB,not(p)):
            if resolution gives empty clause (TRUE), p is consistent and expansion is done,
            otherwise, Revision is done"""

        if resolution(self.KB, formula):  # Is KB consisten with formula? Careful with negation,
            self.revision(formula)

        else:
            self.add_formula(formula)

    def revision(self, p):
        """Does resolution with all the subsets of the KB and p, when finding one subset with empty clause:
           -Add that subset to remainders,
           -Choose the best one
           -Set KB to it + p

           Pass p as original formula pls! (not negated)
           """

        remainders = []
        subsets = powerset(self.KB)  # All subsets of KB: [ {{1,2,3}, {1,2}]}, {{1,2,3}}, {{1,2}} ]

        for i in subsets:
            if not resolution(set(i), negate(p)):
                # Check if new info p is consistent with that (pseudo)remainder
                if not resolution(set(i), p):
                    remainders.append(i)  # Its a remainder

        # Find the maximal inclusive remainder
        maxinclusive = []
        if len(remainders) > 0:
            maxinclusive = remainders[0]

        for remainder in remainders:
            if len(remainder[0]) > len(maxinclusive):
                maxinclusive = remainder

        self.KB = set(maxinclusive)
        self.add_formula(p)
        return remainders

    def printkb(self):
        print("KB = {", end="")

        for frozset in self.KB:
            i = 0
            print("{", end="")
            natoms = len(frozset)
            for atom in frozset:
                i = i + 1
                print(atom, end="")
                if i < natoms:
                    print(",", end="")

            print("}", end=" ")
        print("}")


def resolution(belief, alpha):
    """Checks whether the new formula is logically entailed by the KB resolution(KB,not(p)):
        if resolution gives empty clause (TRUE), p is consistent and expansion is done,
        otherwise, Revision is done

        -True if empty clause with alpha
        -False if the resolved are subset of belief
        -Resolved clauses if
        """

    clauses = belief.copy()

    clauses.add(frozenset(alpha))

    new = set()
    resolvents = set()

    while 1:
        list_clauses = list(clauses)

        for i in range(len(list_clauses)):
            for j in range(i + 1, len(list_clauses)):
                resolved = resolve(list_clauses[i], list_clauses[j])
                if len(resolved) == 0:
                    return True

                resolvents.add(frozenset(resolved))
                new = new | resolvents

        if new.issubset(clauses):
            return False

        clauses = clauses | new


def resolve(a, b):

    x1 = set(a.copy())
    y1 = set(b.copy())
    sol = set([])

    for i in range(len(x1)):
        element = x1.pop()
        as1 = set([])
        as1.update([-1 * element])
        # print("as1 = " + str(as1))
        # print(as1.issubset(y1))

        if as1.issubset(y1):
            y1.discard(as1.pop())
            # print("y1 after discarding" + str(y1))

        else:
            sol.update([element])

    sol.update(y1)
    return sol


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def negate(formula):
    """Negates a clause in CNF, so it will be converted from disjuntions to conjuctions """
    negated = set()
    for atom in formula:
        negated.add(atom * -1)

    return frozenset(negated)
