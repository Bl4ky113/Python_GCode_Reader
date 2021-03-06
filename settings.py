
import serial as s
from tkinter.filedialog import askopenfile
from os import path

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
            "len_z": 1
        }
        self.cnc_step = 1

    def config_serial_port (self, port_name=None):
        self.serial_port.port = port_name
        self.serial_port.baudrate = 9600
        self.serial_port.timeout = 0.25
        self.serial_port.write_timeout = 0.25

        self.serial_info = self.serial_port.get_settings()
        self.serial_name = self.serial_port.name
        self.serial_status = "Open"

        self.serial_port.open()
        self.serial_port.write("G01 X0 Y0\n".encode("ascii"))
        self.serial_port.write("M300 S30\n".encode("ascii"))

        self.upload_serial_info()

    def check_change_axis (self, axis, change):
        if self.serial_port.is_open:
            if axis != "z":
                if (self.axis_info[axis] + change) <= self.cnc_info[f"len_{axis}"] and (self.axis_info[axis] + change) >= 0:
                    self.axis_info[axis] += change
                
                    if self.serial_port.in_waiting <= 0:
                        write_output = f"G01 {axis.upper()}{self.axis_info[axis]}\n"
                        self.serial_port.write(write_output.encode("ascii"))

                        self.upload_cnc_axis()
                        self.upload_cnc_home()

            else:
                if change >= 1 and (self.axis_info[axis] + 1) <= self.cnc_info[f"len_{axis}"]:
                    servo_status = "50"
                    self.axis_info[axis] += 1
                elif change <=0 and (self.axis_info[axis] - 1) >= 0:
                    servo_status = "30"
                    self.axis_info[axis] -= 1
                else:
                    return

                servo_status = "M300 S" + servo_status + "\n"
                self.serial_port.write(servo_status.encode("ascii"))

                self.upload_cnc_axis()
                self.upload_cnc_home()

    def change_home (self):
        self.home_info = self.axis_info.copy()

        self.upload_cnc_axis()
        self.upload_cnc_home()

    def go_home (self):
        if self.serial_port.is_open:
            home_output = ""

            if self.home_info["z"] == 0:
                home_output += "M300 S30\n"
            else:
                home_output += "M300 S50\n"

            home_output += f"G01 X{self.home_info['x']} Y{self.home_info['z']}\n"

            self.serial_port.write(home_output.encode("ascii"))
            self.axis_info = self.home_info.copy()

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

        self.g_code = tuple(new_gcode)

        self.upload_gcode_info()

    def run_gcode_file (self):
        if len(self.g_code) > 0 and self.serial_port.is_open:
            line_iterator = 0

            while True:
                if self.serial_port.in_waiting <= 0:
                    print(self.g_code[line_iterator])
                    self.serial_port.write(f"{self.g_code[line_iterator]}".encode("ascii"))
                    line_iterator += 1

                if (line_iterator + 1) == len(self.g_code):
                    break

    def get_serial_output (self):
        if self.serial_port.is_open:
            output = self.serial_port.readline().decode("ascii")
            
            if output != "":
                self.serial_output.append(f"< {output}")
                self.upload_serial_output()

            self.loop_get_serial_output()

    def clear_serial_output (self):
        self.serial_output = []

    def change_cnc_steps (self, mode="+"):
        if self.cnc_step > 1 and mode == "-":
            self.cnc_step -= 1
        if (self.cnc_step < self.cnc_info["len_x"] or self.cnc_step < self.cnc_info["len_y"]) and mode == "+":
            self.cnc_step += 1

        print("Current Steps: ", self.cnc_step)


global global_values
global_values = GlobalValues()
