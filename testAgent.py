from BeliefRevisionAgent import Agent


if __name__ == "__main__":

    agent = Agent({1, 2}, {3})
    set1 = {-3}
    agent.agmRevison(set1)
    agent.printkb()

