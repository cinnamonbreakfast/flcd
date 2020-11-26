

class FiniteAutomataState:
    def __init__(self, structure):
        self.states = []
        self.alphabet = []
        self.initial = []
        self.finals = []
        self.transitions = {}

        self._file = open(structure, "r")

        self._load()
        # print(self.validate())

    def _load(self):
        reading = "none"

        reading = "none"

        line = self._file.readline()

        def classify(mode, probe):
            if mode == "states":
                spec = probe.split(', ')
                self.states.extend(spec)
            elif mode == "initial":
                spec = probe.split(', ')
                self.initial.extend(spec)
            elif mode == "alpha":
                spec = probe.split(', ')
                self.alphabet.extend(spec)
            elif mode == "trans":
                values = probe.split(", ")

                if (values[0], values[1]) in self.transitions.keys():
                    self.transitions[(values[0], values[1])].append(values[2])
                else:
                    self.transitions[(values[0], values[1])] = [values[2]]
            elif mode == "final":
                tokens = probe.split(", ")
                self.finals.extend(tokens)

        while line:
            if line.strip()[0] == '#':
                reading = line.strip()[1:]
            else:
                classify(reading, line.strip())

            line = self._file.readline()

    def validate(self):
        if self.initial[0] not in self.states:
            return False

        for final in self.finals:
            if final not in self.states:
                return False

        for key in self.transitions.keys():
            state = key[0]
            symbol = key[1]
            if state not in self.states or symbol not in self.alphabet:
                return False
            for dest in self.transitions[key]:
                if dest not in self.states:
                    return False
        return True

    def dfa(self):
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False
        return True

    def accepted(self, sequence):
        if self.dfa():
            crt = self.initial[0]

            for symbol in sequence:
                if (crt, symbol) in self.transitions.keys():
                    crt = self.transitions[(crt, symbol)][0]
                else:
                    return False
            return crt in self.finals
        return False