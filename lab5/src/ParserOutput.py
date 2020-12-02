from typing import List

from src.Descendand import Descendad


# class ProductionElement:
#     def __init__(self, production, index=0):
#         self.production = production
#         self.index = index

#['S 1', 'a', 'S 2', 'a', 'S 3', 'c', 'b', 'S 3', 'c']
class TableElement:
    def __init__(self, element, pos):
        self.element = element #production elem ('S 1', 0)
        self.parent = None
        self.left = None
        self.right = None
        self.pos = pos

    def __str__(self) -> str:
        return str(self.element)

class ParserOutput:
    def __init__(self, grammar: Descendad):
        self.grammar = grammar
        self.table = {}

    def start(self, work_stack):
        self.table[0] = TableElement(work_stack[0], 0)
        index = 1
        current = self.table[0]
        while index < len(work_stack):
            index = self.parse(current, work_stack, index)
            current = self.getNextParse(current)
        for val in self.table.values():
            print(val)
        # for key in self.table.keys():
        #     print(str(key) + "-> " + str(self.table[key]))

    def getNextParse(self, current):
        for val in self.table.values():
            if val.element != current.element and val not in self.grammar.parser.terminals:
                return val

    # ['S 1', 'a', 'S 2', 'a', 'S 3', 'c', 'b', 'S 3', 'c']
    # 0 nodeS1
    # 1 node(a) parent(0) leftNone right(2)
    # 2 node(S2) parent(0) left(1) right(3)
    # 3 node(b) parent(0) left(2) right(4)
    # 4 node(S3) parent(0)
    # 5 node(a) parent(2)
    def parse(self, node, work_stack, index):
        if node.element not in self.grammar.parser.terminals:
            non_terminal = node.element.split(' ')[0]
            production_nr = int(node.element.split(' ')[1])
            production = self.grammar.parser.get_productions_of_non_terminal(non_terminal)[production_nr-1]
            nodes = []
            left = None
            for el in production:
                current = None
                if el in self.grammar.parser.terminals:
                    current = TableElement(el, index)
                else:
                    current = TableElement(work_stack[index], index)
                self.table[index] = current
                index += 1
                current.parent = node
                current.left = left
                left = current
                nodes.append(current)
            for i in range(len(nodes)-1):
                nodes[i].right = nodes[i+1]
        return index




    # def start(self):
    #     parser = self.grammar.parser
    #     start_symbol = parser.start_symbol
    #     self.head = TableElement(parser.get_productions_of_non_terminal(start_symbol))
