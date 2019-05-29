from BeliefRevisionAgent import Agent


def ex11():
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

    i = 0
    while i < len(new_belief):

        if new_belief[i] != "v" and new_belief[i] != "V" and new_belief[i] != " ":

            if new_belief[i] == '-':
                i = i+1
                negative = True
                char = new_belief[i]
            else:
                negative = False
                char = new_belief[i]

            if is_new_char(char, world1):
                world1[char] = max(values) + 1
            else:
                pass

            if negative is True:
                clause.add(world1.get(char) * -1)
            else:
                clause.add(world1.get(char))

        i = i + 1

    return clause


def is_new_char(char, dictionary):
    value = dictionary.get(char)

    if value is None:
        return True

    return False


if __name__ == "__main__":

    agent = Agent()
    agent.printkb()

    while 1:
        new_info = input("\nEnter new info: ")

        clause_num = convert_to_numbers(new_info, agent.language)

        agent.agm_revison(clause_num)

        print("\nUpdated new Belief set:")
        agent.printkb()

