from BeliefRevisionAgent import Agent

agent = Agent({1, 2, 3}, {1, 2})

print(agent.KB)
agent.revision()


