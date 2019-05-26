# Resolution
# if phi is consistent with B
# check is B entails !phi then it is consistent.


def resolve(a, b):
    x1 = set(a.copy())
    y1 = set(b.copy())
    sol = set([])

    for i in range(len(x1)):
        element = x1.pop()
        as1 = set([])
        as1.update([-1*element])
        #print("as1 = " + str(as1))
        #print(as1.issubset(y1))

        if as1.issubset(y1):
            y1.discard(as1.pop())
            #print("y1 after discarding" + str(y1))

        else:
            sol.update([element])

    sol.update(y1)
    return sol


def resolution(kb1, alpha1):
    kb = set(kb1.copy())
    alpha = set(alpha1.copy())

    consistency = False
    clauses = kb | alpha
    print(clauses)
    new = set([])
    clash1 = set([])
    clash2 = set([])
    cl1 = set([])
    cl2 = set([])
    clauses_copy1 = clauses.copy()
    for i in clauses_copy1:
        cl1.add(i)
        clauses.discard(i)
        if len(cl1) > 1: cl1.pop()
        clauses_copy2 = clauses.copy()

        for j in clauses_copy2:
            cl2.add(j)
            if len(cl2) > 1 : cl2.pop()
            print("resolvent_pair" + str(cl1) + str( cl2))
            resolvent = resolve(cl1, cl2)
            print(resolvent)

            if len(resolvent) == 0:
                clash1 = cl1.copy()
                clash2 = cl2.copy()
                consistency = True
                # Eliminating clause that resulted in empty set

            print("clash1 " + str(clash1))
            print("clash2 " + str(clash2))
            new.update(resolvent)
            print("resolvant update done")

            if len(clash1) >= 1:
                clash_copy1 = int(clash1.pop())
                new.discard(clash_copy1)
                clash1.add(clash_copy1)
                print("#####################")

            if len(clash2) >= 1:
                clash_copy2 = int(clash2.pop())
                new.discard(clash_copy2.pop())
                clash1.add(clash_copy2)
                print("#####################")

            print("new -> " + str(new))

    clauses = clauses | new
    print(clauses)
    if new.issubset(clauses):
        consistency = False
    return consistency


k = {1, 2, 3}
al = {-2, 5, 6}

print(resolution(k, al))

