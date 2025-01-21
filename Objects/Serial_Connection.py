class SerialConnection:
    port = ""
    baud_rate = 0
    timeout = 0
    def __init__(self, port: str = "", baud_rate: int = 9600, timeout: int = 0):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
    def establish_connection(self):
        