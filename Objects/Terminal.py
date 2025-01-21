from Configuration_Terminal.Objects.Serial_Connection import SerialConnection
from Configuration_Terminal.Objects.Script import write_script


class Terminal:
    """
    Handles operation modes: Script Mode and Terminal Mode.
    """
    script_commands = []
    def __init__(self, mode: bool, port: str):
        """
        Initializes the Terminal based on the mode.
        
        :param mode: If False, script mode is activated. If True, terminal mode is activated.
        :param port: Serial port for the terminal connection.
        """
        self.mode = mode
        self.connection = SerialConnection(port, 9600, 1) if mode else None
        if not mode:
            print("Terminal is in Script Mode")

    def write_commands(self, command: str):
        if self.mode:
            self.write_terminal(command)
        else:
            self.write_script(command)

    def write_script(self, command: str):
        """
        Placeholder for future implementation of script mode commands.
        :param commands: List of commands to execute in script mode.
        """
        self.script_commands.append(command)

    def write_terminal(self, command: str):
        """
        Writes a command to the terminal in Terminal Mode.
        
        :param command: Command to write to the terminal.
        """
        if self.mode and self.connection:
            self.connection.write_to_serial(command)
        else:
            print("Cannot write to terminal in Script Mode.")

    def logout(self):
        """
        Logs out the terminal connection in Terminal Mode.
        """
        if self.mode and self.connection:
            self.connection.logout()
        else:
            write_script(self.script_commands)