from BeliefRevisionAgent import Agent


if __name__ == "__main__":

    agent = Agent({1, 2}, {3})
    agent.printkb()
    set1 = {-3}
    print("New info: " + str(set1) + "\n")
    agent.agmRevison(set1)
    agent.printkb()

