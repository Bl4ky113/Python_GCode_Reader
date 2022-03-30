
from tk_classes import *
from settings import *
import serial.tools.list_ports as list_serial_ports


def start_serial_menu ():
    serial_menu = SetSerialMenu()
    serial_menu.change_function("select_serial_port_btn", "btn", 
            lambda: global_values.config_serial_port(serial_menu.port_list.get_selected_value())
    )

class Menu ():
    def __init__ (self, base_title, size_percentage=(0.5, 0.5), tk_root=False):
        self.base = Base(base_title, size_percentage[0], size_percentage[1], tk_root)

        self.header = Div(self.base.root, (0, "x", "top"))
        self.main = Div(self.base.root, (1, "both", "top"))
        self.footer = Div(self.base.root, (0, "x", "bottom"))

    def change_function (self, tk_element, tk_type, new_function):
        element_obj = getattr(self, tk_element)
        element = getattr(element_obj, tk_type)

        element.configure(
            command=new_function
        )

class MainMenu (Menu):
    def __init__ (self):
        super().__init__(" Create, Test and Use G-Code ", (0.9, 0.8), True)

        main_title = Title(self.header.div, "Create, Test and Use G-Code", (1, "both", "left"))
        bl4ky_signature = Bl4ky113(self.header.div, " // Made By Bl4ky113 ", (1, "both", "right"))
        
        self.set_serial_port_btn = Button(self.footer.div, start_serial_menu, "Set Serial Port", ((0, 0), (10, 5), "right"))

    def init_menu (self):
        self.base.root.mainloop()

class SetSerialMenu (Menu):
    def __init__ (self):
        super().__init__(" Select the Serial Port ", (0.4, 0.6))

        ports = self.get_active_ports()

        main_title = Title(self.header.div, "Select the Serial Port", (0, "x", "top"))
        self.port_list = ListBox(self.main.div, ports, (1, "both", "top"))
        self.select_serial_port_btn = Button(self.footer.div, lambda: None, "Use Selected Port", ((10, 5), (20, 10), "right"))

    def get_active_ports (self) -> tuple:
        active_ports = list_serial_ports.comports()
        list_ports = []

        for port in active_ports:
            list_ports.append(port.device)
    
        return tuple(list_ports)

