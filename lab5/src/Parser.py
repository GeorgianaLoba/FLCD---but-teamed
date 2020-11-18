class Parser:
    def __init__(self):
        self.non_terminals = []
        self.terminals = []
        self.start_symbol = ""
        self.productions = {}

    def split_line(self, line):
        return line.strip().split(' ')

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            # first 3 lines are fixed sized
            self.non_terminals = self.split_line(f.readline())
            self.terminals = self.split_line(f.readline())
            self.start_symbol = self.split_line(f.readline())[0]
            for line in f:
                all = line.split('-') # [ [], [] ]
                key = all[0].strip()
                values = all[1].split('|')
                self.productions[key] = []
                for val in values:
                    #TODO validate
                    self.productions[key].append(val.strip())

    def validate_start_symbol(self):
        if self.start_symbol not in self.non_terminals:
            raise Exception('Invalid start symbol: ' + str(self.start_symbol) + ' not found in not-terminals list.')

    def validate_productions(self):
        for key, vals in self.productions.items():
            if key not in self.non_terminals:
                raise Exception('Invalid production: '+ str(key) + ' not found in not-terminals list.')
            for elem in vals:
                for char in elem:
                    if 97 <= ord(char) <= 122 and char not in self.terminals:
                        raise Exception('Invalid production: ' + char + ' not found in terminals list.')
                    elif 65 <= ord(char) <= 90 and char not in self.non_terminals:
                        raise Exception('Invalid production: ' + char + ' not found in non_terminals list.')

    def get_productions_of_non_terminal(self, non_terminal):
        if non_terminal in self.non_terminals:
            return self.productions[non_terminal]
        else:
            raise Exception('Invalid non-terminal: ' + non_terminal + ' not found in not-terminals list.')

    def __str__(self) -> str:
        stringg = ""
        stringg += "Non-terminals: " + str(self.non_terminals) + "\n"
        stringg += "Terminals: " + str(self.terminals) + "\n"
        stringg += "Start symbol: " + str(self.start_symbol) + "\n"
        for key in self.productions.keys():
            stringg += str(key) + "->" + str(self.productions[key]) + "\n"
        return stringg

