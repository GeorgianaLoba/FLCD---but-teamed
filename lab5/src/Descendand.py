from src import Parser
from src.ConfigurationClass import ConfigurationClass


class Descendad:
    def __init__(self, parser):
        self.parser = parser
        self.parser.read_file("grammar.in")
        self.configuration = ConfigurationClass(self.parser.start_symbol)

    def expand(self):
        nonTerminal = self.configuration.input_stack.pop(0)
        self.configuration.work_stack.append(nonTerminal + " 1")
        for i in range(len(self.parser.get_productions_of_non_terminal(nonTerminal)[0]) - 1, -1, -1):
            self.configuration.input_stack.insert(0, self.parser.get_productions_of_non_terminal(nonTerminal)[0][i])

    def advance(self):
        self.configuration.index += 1
        terminal = self.configuration.input_stack.pop(0)
        self.configuration.work_stack.append(terminal)

    def momentary_insucces(self):
        self.configuration.state["q"] = False
        self.configuration.state["b"] = True

    def back(self):
        self.configuration.index -= 1
        terminal = self.configuration.work_stack.pop()
        self.configuration.input_stack.insert(0, terminal)

    def succes(self):
        self.configuration.state["q"] = False
        self.configuration.state["f"] = True

    def another_try(self):
        nonTernminal = self.configuration.work_stack.pop()
        number = nonTernminal.split(' ')[1]
        productions = self.parser.get_productions_of_non_terminal(nonTernminal.split(' ')[0])
        for i in range(len(productions[int(number) - 1])):
            self.configuration.input_stack.pop(0)
        if self.configuration.index == int(number) and len(self.configuration.work_stack)==0:
            self.configuration.state["e"] = True
            self.configuration.state["b"] = False
        elif len(productions) > int(number):
            self.configuration.state["q"] = True
            self.configuration.state["b"] = False
            self.configuration.work_stack.append(nonTernminal.split(' ')[0] + " " + str(int(number) + 1))

            for i in range(len(productions[int(number)])-1, -1, -1):
                self.configuration.input_stack.insert(0, productions[int(number)][i])
        elif len(productions) <= int(number):
            self.configuration.input_stack.insert(0, nonTernminal.split(' ')[0])



    def run(self, sequence):
        running = True
        while (running):
            print('------------------------------------------------------------')
            print(self.configuration.work_stack)
            print(self.configuration.input_stack)
            print('--------------------------------------------------------------')
            if len(self.configuration.input_stack) == 0 and self.configuration.state["q"] == True and self.configuration.index-1 == len(sequence):
                self.succes()
            elif self.configuration.input_stack[0] in self.parser.non_terminals and self.configuration.state["q"] == True:
                self.expand()
            elif self.configuration.state["q"] == True and self.configuration.input_stack[0] in self.parser.terminals:
                if self.configuration.index>len(sequence):
                    self.momentary_insucces()
                else:
                    if sequence[self.configuration.index-1] == self.configuration.input_stack[0]:
                        self.advance()
                    else:
                        self.momentary_insucces()
            elif self.configuration.state["b"] == True:
                if self.configuration.work_stack[-1] in self.parser.terminals:
                    self.back()
                else:
                    self.another_try()

            if self.configuration.state["f"] == True:
                running = False
                print("Succes" + str(self.configuration.input_stack) + " " + str(self.configuration.work_stack))
                return self.configuration.work_stack
            if self.configuration.state["e"] == True:
                running = False
                print("Error. Sequence not accepted")
