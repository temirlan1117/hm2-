class Hello:
    def __init__(self, str):
        self.str = str
class tema(Hello):
    def __init__(self, str):
        super().__init__(str)
        self.str = str

    def text(self):
        return self.str