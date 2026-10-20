class Developer:

    def __init__(self, tools):
        self.tools = tools


    def __len__(self):
        return len(self.tools)

    def __getitem__(self, index):
        return self.tools[index]