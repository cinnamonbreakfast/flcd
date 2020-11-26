class Parser:
    def __init__(self, file_path):
        self.__dot_productions = {'S\'': [['.', 'S']]}
        file_program = self.__load(file_path)
        self.__terminals = file_program[0]
        self.__non_terminals = file_program[1]
        self.__productions = {}
        self.__transactions = file_program[2:]
        self.initial_closure = None

        # init productions
        self.__init_prods()
        self.__init_in_closure()

    def __init_prods(self):
        for e in self.__transactions:
            if e[0] in self.__productions:
                self.__productions[e[0]].append(e[1:])
            else:
                self.__productions[e[0]] = [e[1:]]
    def __init_in_closure(self):
        dot = self.__dot_maker()

        self.initial_closure = {"S'": [dot["S'"][0]]}
        self.closure(self.initial_closure, dot, dot["S'"][0])
    def __dot_maker(self):
        self.__dot_productions = {'S\'': [['.', 'S']]}

        for nt in self.__productions:
            self.__dot_productions[nt] = []
            for path in self.__productions[nt]:
                self.__dot_productions[nt].append(["."] + path)

        return self.__dot_productions
    def __load(self, dir):
        file1 = open(dir, 'r')
        lines = file1.readlines()
        file1.close()
        return [line.replace("\n", "").replace("\t", "").split(" ") for line in lines]

    def __to_human_readable(self, hashmap, message=None, deepness=""):
        if message is not None:
            print(deepness + message)
        for key in hashmap:
            print(f"{deepness}{key} : {hashmap[key]}")

    def closure(self, closure_map, transitions_map, transition_value):
        dot_index = transition_value.index(".")

        if dot_index + 1 == len(transition_value):
            return

        after_dot = transition_value[dot_index + 1]

        if after_dot in self.__non_terminals:
            non_terminal = after_dot

            if non_terminal not in closure_map:
                closure_map[non_terminal] = transitions_map[non_terminal]
            else:
                closure_map[non_terminal] += transitions_map[non_terminal]
            for transition in transitions_map[non_terminal]:
                self.closure(closure_map, transitions_map, transition)

    @staticmethod
    def shiftable(transition):
        dot_index = transition.index(".")

        if len(transition) > dot_index + 1:
            return True
        return False

    @staticmethod
    def shift_dot(transition):
        transition = transition[:]
        dot_index = transition.index(".")

        if not Parser.shiftable(transition):
            raise Exception("Should I shift it back ?")

        if len(transition) > dot_index + 2:
            remainder = transition[dot_index + 2:]
        else:
            remainder = []

        return transition[:dot_index] + [transition[dot_index + 1]] + ["."] + remainder

    def canonical_collection(self):
        self.temp = {}
        self.queue = [{
            "state": self.initial_closure,
            "initial_dotted": self.__dot_productions,
        }]
        self.states = []
        self.state_parents = {}

        while len(self.queue) > 0:
            self.goto_all(**self.queue.pop(0))

        reduced = self.get_reduced()

        for k in reduced:
            red_k = list(reduced[k].keys())

            if red_k[0] != "S'":
                trans = red_k + reduced[k][red_k[0]][0][:-1]
                reduce_index = self.__transactions.index(trans) + 1
                self.temp[k] = {terminal: f"r{reduce_index}" for terminal in self.__terminals}
                self.temp[k]["$"] = f"r{reduce_index}"
            else:
                self.temp[k] = {"$": "accept"}

        del self.state_parents[0]

        for key in self.state_parents:
            parent = self.state_parents[key]

            if parent["parent_index"] in self.temp:
                self.temp[parent["parent_index"]][parent["before_dot"]] = key
            else:
                self.temp[parent["parent_index"]] = {parent["before_dot"]: key}

        table = {f"I{index}": self.temp[index] for index in range(len(self.states))}

        self.__to_human_readable(table, "Table:")

    def goto_all(self, state, initial_dotted, parent=-1, parent_key="-1"):
        if state not in self.states:
            self.states.append(state)
            index = len(self.states) - 1
            self.state_parents[index] = {
                "parent_index": parent,
                "before_dot": parent_key
            }
            {}.items()
            self.__to_human_readable(state, f"state {index}")
            for key in state:
                for transition in state[key]:
                    if self.shiftable(transition):
                        self.goto_one(initial_dotted, key, transition, index)
        else:
            if parent in self.temp:
                self.temp[parent][parent_key] = self.states.index(state)
            else:
                self.temp[parent] = {parent_key: self.states.index(state)}

    def goto_one(self, initial_dotted, key, state, parent=-1):
        shifted_transition = self.shift_dot(state)
        closure_map = {key: [shifted_transition]}
        self.closure(closure_map, initial_dotted, shifted_transition)
        self.queue.append({
            "state": closure_map,
            "initial_dotted": initial_dotted,
            "parent": parent,
            "parent_key": shifted_transition[shifted_transition.index(".") - 1]
        })

    def get_reduced(self):
        self.reduced = {}

        for state in self.states:
            state_key = list(state.keys())[0]

            if len(state) == 1 and len(state[state_key]) and len(state[state_key][0]) and state[state_key][0][-1] == ".":
                self.reduced[self.states.index(state)] = state

        return self.reduced


    def get_terminals(self):
        return self.__terminals
    def get_non_terminals(self):
        return self.__non_terminals
    def get_productions(self):
        return self.__productions
    def get_production(self, non_terminal):
        res = []

        if non_terminal in self.__productions:
            for row in self.__productions[non_terminal]:
                res.append((non_terminal, row))
        else:
            return None

        return res
