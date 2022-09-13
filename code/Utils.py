class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess
