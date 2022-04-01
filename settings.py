
import serial as s

class GlobalValues ():
    def __init__ (self):
        self.serial_port = s.Serial()
        self.serial_info = self.serial_port.get_settings()
        self.g_code = []
        self.g_code_path = None
        self.isPrinting = False
        self.isStreaming = False
        self.axis_info = {
            "x": 0,
            "y": 0,
            "z": 0,
            "home": {"x": 0, "y": 0, "z": 0}
        }
        self.cnc_info = {
            "len_x": 40,
            "len_y": 40,
            "len_z": 1
        }

    def config_serial_port (self, port_name=None):
        self.serial_port.port = port_name
        self.serial_port.baudrate = 9600

global global_values
global_values = GlobalValues()
