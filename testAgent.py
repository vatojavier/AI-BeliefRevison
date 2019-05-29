from BeliefRevisionAgent import Agent


def ex1():
    agent = Agent()
    new_info = {1}
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


def ex4():
    agent = Agent({1}, {2}, {1,2}, {-1,2}, {-2,1})
    new_info = {-1}

    agent.printkb()
    print("New info: " + str(new_info), end="\n\n")

    agent.agm_revison(new_info)
    agent.printkb()


def ex1():
    agent = Agent({1}, {-1,2})
    new_info = {1, 2}

    agent.printkb()
    print("New info: " + str(new_info), end="\n\n")

    agent.agm_revison(new_info)
    agent.printkb()


def convert_to_numbers(new_belief, world1):

    clause = set()
    values = world1.values()

    # for char in new_belief:
    #     if char != "v" and char != "V" and char != " ":
    #         value = world1.get(char)
    #         else:
    #             if value is None:
    #                 world1[char] = max(values) + 1
    #
    #             clause.add(world1.get(char))

    # for i in range(len(new_belief)):
    #     if new_belief[i] != "v" and new_belief[i] != "V" and new_belief[i] != " ":
    #         if new_belief[i] == '-':
    #             char = new_belief[i + 1]
    #             if is_new_char(char, world):
    #                 world[char] = max(values) + 1
    #                 clause.add(world.get(char) * -1)
    #             else:
    #                 clause.add(world.get(char))
    #         else:
    #             if is_new_char(new_belief[i], world):
    #                 world1[new_belief[i]] = max(values) + 1
    #             clause.add(world1.get(new_belief[i]))

    negative = False
    # for i in range(len(new_belief)):
    i = 0
    while i < len(new_belief):

        if new_belief[i] != "v" and new_belief[i] != "V" and new_belief[i] != " ":

            if new_belief[i] == '-':
                i = i+1
                print("I see negative")
                negative = True
                char = new_belief[i]
            else:
                print("I see positive")
                negative = False
                char = new_belief[i]

            if is_new_char(char, world1):
                world1[char] = max(values) + 1
            else:
                pass

            if negative is True:
                print("Value is negative: " + str(world1.get(char) * -1))
                clause.add(world1.get(char) * -1)
            else:
                print("Value is positive: " + str(world1.get(char)))
                clause.add(world1.get(char))

        i = i + 1


    print(world)
    print(clause)
    return clause

def is_new_char(char, dict):
    value = dict.get(char)

    if value is None:
        return True

    return False


if __name__ == "__main__":

    agent = Agent()
    agent.printkb()

    world = {'0': 0}

    while 1:
        new_info = input("Enter new info: ")

        clause_num = convert_to_numbers(new_info, world)
        agent.agm_revison(clause_num)
        agent.printkb()

