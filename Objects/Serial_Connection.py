from os import write

import serial
import time


class SerialConnection:
    """
    A class to manage serial communication through a specified port, supporting connection, command writing, logging of communication, and closing the connection.

    Attributes:
        port (str): The serial port name to which the connection is established.
        baud_rate (int): The baud rate for the serial communication.
        timeout (int): Timeout value for the connection in seconds.
        ser (serial.Serial or None): The serial connection object.
        feedback (list): Stores commands sent and their associated responses.

    Methods:
        __init__(self, port, baud_rate, timeout):
            Initializes the instance with the specified port, baud rate, and timeout values, and establishes the connection.

        establish_connection(self):
            Establishes a serial connection using the given port, baud rate, and timeout values.
            Handles serial connection errors and unexpected exceptions.

        write_to_serial(self, command):
            Sends a command string to the connected serial port and logs the communication.

        logout(self):
            Closes the serial connection and writes the logged data to a log file.

        log_data(self, command, feedback):
            Logs the command and the corresponding feedback received from the device.

        write_log(self):
            Writes the logged data of commands and feedback to a timestamped log file.
    """
    port = ""
    baud_rate = 0
    timeout = 0
    ser = None
    feedback = []
    def __init__(self, port, baud_rate, timeout):
        """
        :param port: Serial port to which the connection will be established.
        :param baud_rate: Communication speed for the serial connection.
        :param timeout: Maximum time to wait for data on the serial port.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.establish_connection()
    def establish_connection(self):
        """
        Establishes a serial connection using the specified port, baud rate, and timeout settings.
        If the connection is successful, it prints details of the established connection.
        Handles and prints exceptions in case of errors.

        :return: None
        """
        try:
            with serial.Serial(self.port, self.baud_rate, timeout=self.timeout) as self.ser:
                print(f"Connected to {self.ser.name} over {self.ser.portstr} at {self.ser.baudrate} baud.")
                time.sleep(2)
        except serial.SerialException as e:
            print(f"Fehler bei der seriellen Verbindung: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    def write_to_serial(self, command):
        """
        Writes a command to the serial port, appends a carriage return and newline, and logs the data response.

        :param command: The command string to be sent to the serial port.
        :return: None
        """
        self.ser.write(command.encode('utf-8') + b'\r\n')
        time.sleep(1)
        self.log_data(self, command, self.ser.readline().decode('utf-8').rstrip())

    def logout(self):
        """
        Closes the current session and writes a log entry.

        :return: None
        """
        self.ser.close()
        self.write_log()
    def log_data(self, command, feedback):
        """
        :param command: The command string that was executed or processed.
        :param feedback: The feedback or response associated with the executed command.
        :return: None
        """
        self.feedback.append([command, feedback])

    def write_log(self):
        """
        Writes the feedback to a log file with a unique timestamped filename.

        The method iterates through the `feedback` attribute, where each entry is a tuple containing
        a feedback title and corresponding message. It writes each feedback entry to a file with
        the title followed by the feedback content.

        :return: None
        """
        with open(f"log-file-{time.time()}", 'w') as file:
            for feed_back in self.feedback:
                file.writelines(f"{feed_back[0]}:\n {feed_back[1]}")


