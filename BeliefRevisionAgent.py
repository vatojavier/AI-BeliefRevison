from itertools import chain, combinations


class Agent:
    belief_base = set()
    language = {'0': 0}

    def __init__(self, *arg):

        for disjunction in arg:
            self.add_formula(disjunction)

    def add_formula(self, formula):
        """Basically this is Expansion"""

        formula = frozenset(formula)
        if not formula.issubset(self.belief_base):
            self.belief_base.add(formula)

    def agm_revison(self, formula):
        """Checks whether the new formula is logically entailed by the KB resolution(KB,not(p)):
            if resolution gives empty clause (TRUE), p is consistent and expansion is done,
            otherwise, Revision is done"""

        if resolution(self.belief_base, formula):  # Is KB consisten with formula? Careful with negation,
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
        subsets = powerset(self.belief_base)  # All subsets of KB: [ {{1,2,3}, {1,2}]}, {{1,2,3}}, {{1,2}} ]

        # checking consistency remainders
        for i in subsets:
            if not resolution(set(i), p):
                remainders.append(set(i))

        # Check if a set is subset o the others
        delete_set = []
        for i in remainders:
            for j in remainders:
                if i != j:
                    if i.issubset(j):
                        if i not in delete_set:
                            delete_set.append(i)

        for i in delete_set:
            remainders.remove(i)

        choosen_rem = set()
        #  Find the maximal inclusive remainder
        if len(remainders) > 0:
            choosen_rem = remainders[0]

        for remainder in remainders:
            if len(remainder) >= len(choosen_rem):
                choosen_rem = remainder

        self.belief_base = choosen_rem
        self.add_formula(p)
        return remainders

    def printkb(self):
        print("Belief base:= {", end="")

        for frozset in self.belief_base:
            i = 0
            print("{", end="")
            natoms = len(frozset)
            for literal in frozset:
                i = i + 1
                if literal < 0:
                    print("-" + get_key(literal*-1, self.language), end="")
                else:
                    print(get_key(literal, self.language), end="")

                if i < natoms:
                    print(" V ", end="")

            print("}", end=" ")
        print("}")


def get_key(value, language):

    for key in language:
        if value == language[key]:
            return key


def find_remainder(b, p, remainders):

    if b.issubset(remainders):
        return False

    if not resolution(b, p):
        remainders.append(b)

    for clause in b:
        b2 = b.copy()
        b2.discard(clause)
        if len(b) == 0:
            return False
        find_remainder(b2, p, remainders)


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

        if as1.issubset(y1):
            y1.discard(as1.pop())
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
