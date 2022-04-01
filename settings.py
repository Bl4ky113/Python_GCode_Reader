
import serial as s

class GlobalValues ():
    def __init__ (self):
        self.serial_port = s.Serial()
        self.serial_info = self.serial_port.get_settings()
        self.serial_name = None
        self.serial_status = "Closed"
        self.serial_streaming = False
        self.g_code = []
        self.g_code_path = None
        self.axis_info = {
            "x": 0,
            "y": 0,
            "z": 0
        }
        self.home_info = {
            "x": 0,
            "y": 0,
            "z": 0
        }
        self.cnc_info = {
            "len_x": 40,
            "len_y": 40,
            "len_z": 4
        }
        self.cnc_step = 1

    def config_serial_port (self, port_name=None):
        self.serial_port.port = port_name
        self.serial_port.baudrate = 9600
        self.serial_port_name = self.serial_port.name
        self.upload_serial_info()

    def check_change_axis (self, axis, change):
        if (self.axis_info[axis] + change) <= self.cnc_info[f"len_{axis}"] and (self.axis_info[axis] + change) >= 0:
            self.axis_info[axis] += change
            
            self.upload_cnc_axis()
            self.upload_cnc_home()

    def change_home (self):
        self.home_info = self.axis_info.copy()

        self.upload_cnc_axis()
        self.upload_cnc_home()

global global_values
global_values = GlobalValues()
