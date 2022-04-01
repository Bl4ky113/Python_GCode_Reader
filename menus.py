
from tk_classes import *
from settings import *
import serial.tools.list_ports as list_serial_ports

def close_menu (callout_function, menu_to_close):
    callout_function()

    menu_to_close.root.destroy()


def start_serial_menu ():
    serial_menu = SetSerialMenu()
    serial_menu.change_function("select_serial_port_btn", "btn", 
            lambda: close_menu(
                lambda: global_values.config_serial_port(serial_menu.port_list.get_selected_value()),
                serial_menu.base
            )
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
        super().__init__("Create, Test and Use G-Code", (0.9, 0.8), True)

        main_title = Title(self.header.div, "Create, Test and Use G-Code", (1, "both", "left"))
        bl4ky_signature = Bl4ky113(self.header.div, " // Made By Bl4ky113 ", (1, "both", "right"))

        cnc_wrapper = Div(self.main.div, (1, "both", "left"))

        btn_cnc_menus_wrapper = Div(cnc_wrapper.div, (0, "x", "top"))
        btn_show_testing_menu = Button(btn_cnc_menus_wrapper.div, self.show_testing_menu, "CNC Testing", ((0, 0), (0, 5), "left"))
        btn_show_gcode_menu = Button(btn_cnc_menus_wrapper.div, self.show_gcode_menu, "G-Code", ((0, 0), (0, 5), "left"))

        cnc_menus_wrapper = Div(cnc_wrapper.div, (1, "both", "left"))
        cnc_menus_wrapper.add_border()

        self.gcode_file_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "left"))
        label_name_gcode_file = Label(self.gcode_file_wrapper.div, "None", (0, "x", "top"))
        self.gcode_viewer = ListBox(self.gcode_file_wrapper.div, (), (1, "both", "top"))
        btn_run_gcode_file = Button(self.gcode_file_wrapper.div, lambda: print(), "Run File", ((15, 5), (0, 2), "right"))
        btn_load_gcode_file = Button(self.gcode_file_wrapper.div, lambda: print(), "Load File", ((10, 5), (0, 2), "left"))
        self.gcode_file_wrapper.hide_div()

        self.testing_cnc_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "left"))
        axis_btns_wrapper = Div(self.testing_cnc_wrapper.div, (0, "none", "left"))
        btn_add_y = Button(axis_btns_wrapper.div, lambda: print(), "+Y", ((10, 20), (5, 5), "top"))
        btn_sub_x = Button(axis_btns_wrapper.div, lambda: print(), "-X", ((15, 20), (5, 5), "left"))
        btn_add_x = Button(axis_btns_wrapper.div, lambda: print(), "+X", ((10, 20), (5, 5), "right"))
        btn_sub_y = Button(axis_btns_wrapper.div, lambda: print(), "-Y", ((15, 20), (5, 5), "bottom"))
        extra_btns_wrapper = Div(self.testing_cnc_wrapper.div, (0, "none", "right"))
        axis_z_wrapper = Div(extra_btns_wrapper.div, (0, "none", "top"))
        btn_add_z = Button(axis_z_wrapper.div, lambda: print(), "+Z", ((10, 20), (5, 5), "top"))
        btn_sub_z = Button(axis_z_wrapper.div, lambda: print(), "-Z", ((15, 20), (5, 5), "top"))
        home_btn_wrapper = Div(extra_btns_wrapper.div, (0, "none", "top"))
        btn_set_home = Button(home_btn_wrapper.div, lambda: print(), "Set Home", ((0, 0), (5, 5), "top"))
        btn_go_home = Button(home_btn_wrapper.div, lambda: print(), "Go Home", ((5, 0), (5, 5), "top"))

        cnc_info_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "right"))
        cnc_info_wrapper.add_border()
        self.label_current_home = Label(cnc_info_wrapper.div, "Home: X: 0; Y: 0; Z: 0;", (0, "x", "top"))
        cnc_info_canvas = Canvas(cnc_info_wrapper.div, self.base.height * 0.5, self.base.height * 0.5)
        cnc_info_canvas.set_num_axis_divisions(global_values.cnc_info["len_x"], global_values.cnc_info["len_y"], global_values.cnc_info["len_z"])
        axis_position_wrapper = Div(cnc_info_wrapper.div, (1, "x", "bottom"))
        self.label_x_position = Label(axis_position_wrapper.div, "X: 0;", (1, "x", "left"))
        self.label_y_position = Label(axis_position_wrapper.div, "Y: 0;", (1, "x", "left"))
        self.label_z_position = Label(axis_position_wrapper.div, "Z: 0;", (1, "x", "left"))

        serial_info_wrapper = Div(self.main.div, (1, "both", "right"))
        serial_info_wrapper.add_border()
        serial_info_title = Label(serial_info_wrapper.div, "Serial Info", (0, "x", "top"))
        serial_info_list = ListBox(serial_info_wrapper.div, (), (1, "both", "top"))
        self.set_serial_port_btn = Button(serial_info_wrapper.div, start_serial_menu, "Set Serial Port", ((0, 0), (10, 5), "bottom"))

    def show_gcode_menu (self):
        try:
            self.gcode_file_wrapper.div.pack_info()
            return
        except:
            self.gcode_file_wrapper.div.pack(
                expand=1,
                fill="both",
                side="left"
            )
            self.testing_cnc_wrapper.hide_div()

    def show_testing_menu (self):
        try:
            self.testing_cnc_wrapper.div.pack_info()
            return
        except:
            self.testing_cnc_wrapper.div.pack(
                expand=1,
                fill="both",
                side="left"
            )
            self.gcode_file_wrapper.hide_div()

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

