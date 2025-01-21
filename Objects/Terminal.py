from xmlrpc.client import boolean


class Terminal:
    #if mode is false Script Mode, True used as Terminal
    mode = None
    def __init__(self, mode=boolean(False)):
        self.mode = mode
    def write_script(self, command):
        pass
    def write_Terminal(self, command):
        pass