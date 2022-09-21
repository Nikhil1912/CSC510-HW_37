class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess


class ProcessCsv:
    def csv(self, filename, funct):
        seperator = None

        # TODO
