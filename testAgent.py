from BeliefRevisionAgent import Agent


def ex1():
    agent = Agent({3}, {1, 2})
    new_info = {-3}
    agent.printkb()
    print("New info: " + str(new_info), end="\n\n")

    agent.agm_revison(new_info)
    agent.printkb()


def ex2():
    agent = Agent({1, 2})
    new_info = {-1}

    agent.printkb()
    print("New info: " + str(new_info), end="\n\n")

    agent.agm_revison(new_info)
    agent.printkb()


def ex3():
    agent = Agent({1}, {2}, {-1, 2})
    new_info = {-2}

    agent.printkb()
    print("New info: " + str(new_info), end="\n\n")

    agent.agm_revison(new_info)
    agent.printkb()


if __name__ == "__main__":

    ex3()

