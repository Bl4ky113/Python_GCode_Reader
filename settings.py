
import serial as s
from tkinter.filedialog import askopenfile
from os import path
from time import sleep

class GlobalValues ():
    def __init__ (self):
        self.serial_port = s.Serial()
        self.serial_info = self.serial_port.get_settings()
        self.serial_name = None
        self.serial_status = "Closed"
        self.serial_streaming = False
        self.serial_output = []
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
        self.serial_port.timeout = 5.0
        self.serial_port.write_timeout = 5.0

        self.serial_info = self.serial_port.get_settings()
        self.serial_name = self.serial_port.name
        self.serial_status = "Open"

        self.serial_port.open()

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

    def open_gcode_file (self):
        new_gcode = []

        file_opener = askopenfile(
            mode="r",
            filetypes=(
                ("G-Code Files", "*.gcode"),
                ("N G-Code Files", "*.ngc"),
                ("Any Files", "*.*")
            )
        )

        with open(file_opener.name, mode="r", encoding="UTF-8") as gcode_file:
            for line in gcode_file:
                new_gcode.append(line)

            self.g_code_path = path.basename(gcode_file.name)

        self.g_code = new_gcode

        self.upload_gcode_info()

    def get_serial_output (self):
        if self.serial_port.is_open:
            if self.serial_port.in_waiting > 0:
                output = self.serial_port.readline().decode("ascii")

                self.serial_output.append(output)

                self.upload_serial_output()

    def clear_serial_output (self):
        self.serial_output = []

global global_values
global_values = GlobalValues()
