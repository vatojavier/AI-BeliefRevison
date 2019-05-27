from BeliefRevisionAgent import Agent


if __name__ == "__main__":

    agent = Agent({1,2})
    set1 = {-1,-2}
    agent.agmRevison(set1)
    print(agent.KB)

