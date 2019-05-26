from BeliefRevisionAgent import Agent


if __name__ == "__main__":

    agent = Agent({1, 2, 3}, {1, 2})
    set1 = {1, 3, 2}
    agent.addformula(set1)
    agent.revision({2})
    print(agent.KB)

