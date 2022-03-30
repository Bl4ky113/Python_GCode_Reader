
import serial as s

class GlobalValues ():
    def __init__ (self):
        self.serial_port = s.Serial()
        self.g_code = []
        self.g_code_path = None
        self.isPrinting = False
        self.isStreaming = False

    def config_serial_port (self, port_name=None):
        self.serial_port.port = port_name
        self.serial_port.baudrate = 9600

        print(self.serial_port.get_settings())

global global_values
global_values = GlobalValues()
