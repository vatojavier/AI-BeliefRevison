from BeliefRevisionAgent import Agent


if __name__ == "__main__":

    agent = Agent({1, 2, 3}, {1, 2})
    print(agent.KB)
    agent.revision(2)


