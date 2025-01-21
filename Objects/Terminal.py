
from Configuration_Terminal.Objects.Serial_Connection import SerialConnection


class Terminal:
    #if mode is false Script Mode, True used as Terminal
    mode = None
    connection = None
    def __init__(self, mode):
        self.mode = mode
        if mode:
            self.connection = SerialConnection("COM3", 9600, 1)
        else:
            print("Terminal is in Script Mode")
    def write_script(self, commands):
        pass
    def write_Terminal(self, command):
        self.connection.write_to_serial(command)
    def log_out(self):
        if self.mode:
            self.connection.logout()
        else:
            pass
