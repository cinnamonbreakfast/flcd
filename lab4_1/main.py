
def printMenu():
    print("1: Display the states")
    print("2: Display the alphabet")
    print("3: Display the transitions")
    print("4: Display the final state")
    print("\n0: Exit")

if __name__ == "__main__":
    file = open('FA.in', 'r')

    states = []
    alphabet = []
    transitions = {} # [string, string] : string
    finals = []
    initial = []

    reading = "none"

    line = file.readline()


    def classify(probe):
        if mode == "#states":
            states.append(probe)
        elif mode == "#initial":
            initial.append(probe)
        elif mode == "#alpha":
            alphabet.append(probe)
        elif mode == "#trans":
            values = probe.split(", ")
            transitions.update({values[2]: [values[0], values[1]]})
        elif mode == "#final":
            tokens = probe.split(", ")
            finals.extend(tokens)

    while line:
        if line.strip() == "#states":
            mode = "#states"
        elif line.strip() == "#initial":
            mode = "#initial"
        elif line.strip() == "#alpha":
            mode = "#alpha"
        elif line.strip() == "#trans":
            mode = "#trans"
        elif line.strip() == "#final":
            mode = "#final"
        else:
            classify(line.strip())

        line = file.readline()

    while True:
        printMenu()

        opt = input("> ")
        if opt == "0":
            break
        elif opt == "1":
            print("States: ", states, "\n")
        elif opt == "2":
            print("Alphabet: ", alphabet, "\n")
        elif opt == "3":
            print("Transitions: ", transitions, "\n")
        elif opt == "4":
            print("Finals: ", finals, "\n")
        else:
            print("Invalid option")
