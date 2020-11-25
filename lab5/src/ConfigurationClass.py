class ConfigurationClass:
    def __init__(self,start):
        self.state = {}
        self.state["q"] = True
        self.state["f"] = False
        self.state["b"] = False
        self.state["e"] = False
        self.index = 1
        self.work_stack = []
        self.input_stack = [start]
