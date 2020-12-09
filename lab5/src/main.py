from src.Descendand import Descendad
from src.Parser import Parser
from src.ParserOutput import ParserOutput


def display():
    print('HEllO')
    print('Press 1 for displaying the entire grammar')
    print('Press 2 for displaying the non-terminals')
    print('Press 3 for displaying the terminals')
    print('Press 4 for displaying start symbol')
    print('Press 5 for displaying for ALL productions')
    print('Press 6 for displaying for specific production')

    print('Press 0 for exit')


def readPif(Filename):
    sequence=[]
    with open(Filename, 'r') as f:

        # first 3 lines are fixed sized
        for line in f:
            all = line.split('on')  # [ [], [] ]
            key = all[0].strip()
            sequence.append(key)
    return sequence

def main():
    parser = Parser()
    # parser.read_file('grammar.in')
    # try:
    #     parser.validate_start_symbol()
    #     parser.validate_productions()
    # except Exception as ex:
    #     print(ex)
    #     return
    # while True:
    #     display()
    #     try:
    #         inp = int(input())
    #     except Exception:
    #         print('Insert valid number please')
    #     if inp == 0:
    #         break
    #     if inp == 1:
    #         print(parser)
    #     if inp == 2:
    #         print(parser.non_terminals)
    #     if inp == 3:
    #         print(parser.terminals)
    #     if inp == 4:
    #         print(parser.start_symbol)
    #     if inp == 5:
    #         for key in parser.productions.keys():
    #              print(str(key) + "->" + str(parser.productions[key]))
    #     if inp == 6:
    #         nn = input()
    #         try:
    #             print(parser.get_productions_of_non_terminal(nn))
    #         except Exception as ex:
    #             print(ex)

    descendad= Descendad(parser)
    seq = readPif('PIF.out')
    print(seq)

    work_stack = descendad.run(seq)
    print(work_stack)
    if work_stack is not None:
        parserOutput = ParserOutput(descendad)
        parserOutput.start(work_stack)




if __name__ == '__main__':
    main()
