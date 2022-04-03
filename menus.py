
from tk_classes import *
from settings import *
import serial.tools.list_ports as list_serial_ports

def create_sub_menu (SubMenuClass):
    new_sub_menu = SubMenuClass()

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

    def close_menu (self, callout_function):
        callout_function()

        self.base.root.destroy()

class MainMenu (Menu):
    def __init__ (self):
        super().__init__("Create, Test and Use G-Code", (0.9, 0.8), True)

        main_title = Title(self.header.div, "Create, Test and Use G-Code", (1, "both", "left"))
        bl4ky_signature = Bl4ky113(self.header.div, " // Made By Bl4ky113 ", (1, "both", "right"))

        cnc_wrapper = Div(self.main.div, (1, "both", "left"))

        btn_cnc_menus_wrapper = Div(cnc_wrapper.div, (0, "x", "top"))
        btn_show_testing_menu = Button(btn_cnc_menus_wrapper.div, lambda: self.show_menu("testing_cnc_wrapper", "gcode_file_wrapper", "left"), "CNC Testing", ((0, 0), (0, 5), "left"))
        btn_show_gcode_menu = Button(btn_cnc_menus_wrapper.div, lambda: self.show_menu("gcode_file_wrapper", "testing_cnc_wrapper", "left"), "G-Code", ((0, 0), (0, 5), "left"))

        cnc_menus_wrapper = Div(cnc_wrapper.div, (1, "both", "left"))
        cnc_menus_wrapper.add_border()

        self.gcode_file_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "left"))
        self.label_name_gcode_file = Label(self.gcode_file_wrapper.div, "None", (0, "x", "top"))
        self.list_gcode_viewer = ListBox(self.gcode_file_wrapper.div, (), (1, "both", "top"))
        btn_run_gcode_file = Button(self.gcode_file_wrapper.div, lambda: print(), "Run File", ((15, 5), (0, 2), "right"))
        btn_load_gcode_file = Button(self.gcode_file_wrapper.div, global_values.open_gcode_file, "Load File", ((10, 5), (0, 2), "left"))
        self.gcode_file_wrapper.hide_div()

        self.testing_cnc_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "left"))
        axis_btns_wrapper = Div(self.testing_cnc_wrapper.div, (0, "none", "left"))
        btn_add_y = Button(axis_btns_wrapper.div, lambda: global_values.check_change_axis("y", (global_values.cnc_step) * 1), "+Y", ((10, 20), (5, 5), "top"))
        btn_sub_x = Button(axis_btns_wrapper.div, lambda: global_values.check_change_axis("x", (global_values.cnc_step) * -1), "-X", ((15, 20), (5, 5), "left"))
        btn_add_x = Button(axis_btns_wrapper.div, lambda: global_values.check_change_axis("x", (global_values.cnc_step) * 1), "+X", ((10, 20), (5, 5), "right"))
        btn_sub_y = Button(axis_btns_wrapper.div, lambda: global_values.check_change_axis("y", (global_values.cnc_step) * -1), "-Y", ((15, 20), (5, 5), "bottom"))
        self.base.root.bind("<KeyPress-k>", lambda event: global_values.check_change_axis("y", (global_values.cnc_step) * 1))
        self.base.root.bind("<KeyPress-h>", lambda event: global_values.check_change_axis("x", (global_values.cnc_step) * -1))
        self.base.root.bind("<KeyPress-l>", lambda event: global_values.check_change_axis("x", (global_values.cnc_step) * 1))
        self.base.root.bind("<KeyPress-j>", lambda event: global_values.check_change_axis("y", (global_values.cnc_step) * -1))
        extra_btns_wrapper = Div(self.testing_cnc_wrapper.div, (0, "none", "right"))
        axis_z_wrapper = Div(extra_btns_wrapper.div, (0, "none", "top"))
        btn_add_z = Button(axis_z_wrapper.div, lambda: global_values.check_change_axis("z", (global_values.cnc_step) * 1), "+Z", ((10, 20), (5, 5), "top"))
        btn_sub_z = Button(axis_z_wrapper.div, lambda: global_values.check_change_axis("z", (global_values.cnc_step) * -1), "-Z", ((15, 20), (5, 5), "top"))
        self.base.root.bind("<KeyPress-K>", lambda event: global_values.check_change_axis("z", (global_values.cnc_step) * 1))
        self.base.root.bind("<KeyPress-J>", lambda event: global_values.check_change_axis("z", (global_values.cnc_step) * -1))
        home_btn_wrapper = Div(extra_btns_wrapper.div, (0, "none", "top"))
        btn_set_home = Button(home_btn_wrapper.div, lambda: global_values.change_home(), "Set Home", ((0, 0), (5, 5), "top"))
        btn_go_home = Button(home_btn_wrapper.div, lambda: print(), "Go Home", ((5, 0), (5, 5), "top"))

        cnc_info_wrapper = Div(cnc_menus_wrapper.div, (1, "both", "right"))
        cnc_info_wrapper.add_border()
        self.label_current_home = Label(cnc_info_wrapper.div, "Home: X: 0; Y: 0; Z: 0;", (0, "x", "top"))
        self.canvas_cnc_info = Canvas(cnc_info_wrapper.div, self.base.height * 0.5, self.base.height * 0.5)
        self.canvas_cnc_info.set_num_axis_divisions(global_values.cnc_info["len_x"], global_values.cnc_info["len_y"], global_values.cnc_info["len_z"])
        axis_position_wrapper = Div(cnc_info_wrapper.div, (1, "x", "bottom"))
        self.label_x_position = Label(axis_position_wrapper.div, "X: 0;", (1, "x", "left"))
        self.label_y_position = Label(axis_position_wrapper.div, "Y: 0;", (1, "x", "left"))
        self.label_z_position = Label(axis_position_wrapper.div, "Z: 0;", (1, "x", "left"))

        wrapper_serial = Div(self.main.div, (1, "both", "right"))

        wrapper_btns_serial_menus = Div(wrapper_serial.div, (0, "x", "top"))
        btn_show_info_menu = Button(wrapper_btns_serial_menus.div, lambda: self.show_menu("wrapper_serial_info", "wrapper_serial_output", "right"), "Serial Info", ((0, 0), (0, 5), "left"))
        btn_show_output_menu = Button(wrapper_btns_serial_menus.div, lambda: self.show_menu("wrapper_serial_output", "wrapper_serial_info", "right"), "Serial Ouput", ((0, 0), (0, 5), "left"))

        wrapper_serial_menus = Div(wrapper_serial.div, (1, "both", "right"))
        wrapper_serial_menus.add_border()

        self.wrapper_serial_info = Div(wrapper_serial_menus.div, (1, "both", "right"))
        self.label_serial_name = Label(self.wrapper_serial_info.div, "Name: None", (0, "x", "top"))
        self.label_serial_status = Label(self.wrapper_serial_info.div, "Status: Closed", (0, "x", "top"))
        self.label_serial_stream = Label(self.wrapper_serial_info.div, "Streaming: False", (0, "x", "top"))
        self.list_serial_info = ListBox(self.wrapper_serial_info.div, (), (1, "both", "top"))
        set_serial_port_btn = Button(self.wrapper_serial_info.div, lambda: create_sub_menu(SetSerialMenu), "Set Serial Port", ((0, 0), (10, 5), "bottom"))

        self.wrapper_serial_output = Div(wrapper_serial_menus.div, (1, "both", "right"))
        self.list_serial_output = ListBox(self.wrapper_serial_output.div, (), (1, "both", "top"))
        btn_clear_serial_output = Button(self.wrapper_serial_output.div, self.clear_serial_output, "Clear Output", ((10, 0), (0, 5), "right"))
        self.wrapper_serial_output.hide_div()

    def show_menu (self, menu_to_show, menu_to_hide, side="left"): 
        if menu_to_show == "wrapper_serial_output":
            self.base.root.after(500, global_values.get_serial_output)

        menu_to_show = getattr(self, menu_to_show)
        menu_to_hide = getattr(self, menu_to_hide)
        try:
            menu_to_show.div.pack_info()
            return
        except:
            menu_to_show.div.pack(
                expand=1,
                fill="both",
                side=side
            )
            menu_to_hide.hide_div()

    def upload_serial_info (self):
        self.label_serial_name.change_content(f"Name: {global_values.serial_name}")
        self.label_serial_status.change_content(f"Status: {global_values.serial_status}")
        self.label_serial_stream.change_content(f"Streaming: {global_values.serial_streaming}")

        serial_info = []
        for key, value in global_values.serial_info.items():
            serial_info.append(f"{key}: {value}")

        self.list_serial_info.add_values(serial_info)

    def upload_serial_output (self):
        self.list_serial_output.insert_value(global_values.serial_output[-1])
        self.base.root.after(500, global_values.get_serial_output)

    def clear_serial_output (self):
        global_values.clear_serial_output()

        self.list_serial_output.add_values([])

    def upload_cnc_axis (self):
        self.label_x_position.change_content(f"X: {global_values.axis_info['x']}")
        self.label_y_position.change_content(f"Y: {global_values.axis_info['y']}")
        self.label_z_position.change_content(f"Z: {global_values.axis_info['z']}")

        self.canvas_cnc_info.change_axis_position("current", (global_values.axis_info["x"], global_values.axis_info["y"]))
        self.canvas_cnc_info.change_z_position("current", global_values.axis_info["z"])

    def upload_cnc_home (self):
        self.label_current_home.change_content(f"Home: X: {global_values.home_info['x']}; Y: {global_values.home_info['y']}; Z: {global_values.home_info['z']};")

        self.canvas_cnc_info.change_axis_position("home", (global_values.home_info["x"], global_values.home_info["y"]))
        self.canvas_cnc_info.change_z_position("home", global_values.home_info["z"])

    def upload_gcode_info (self):
        self.label_name_gcode_file.change_content(global_values.g_code_path)
        self.list_gcode_viewer.add_values(global_values.g_code)

    def init_menu (self):
        self.base.root.mainloop()

class SetSerialMenu (Menu):
    def __init__ (self):
        super().__init__(" Select the Serial Port ", (0.4, 0.6))

        ports = self.get_active_ports()

        main_title = Title(self.header.div, "Select the Serial Port", (0, "x", "top"))
        self.port_list = ListBox(self.main.div, ports, (1, "both", "top"))
        self.select_serial_port_btn = Button(
            self.footer.div,
            lambda: self.close_menu(
                lambda: global_values.config_serial_port(self.port_list.get_selected_value())
            ), 
            "Use Selected Port", 
            ((10, 5), (20, 10), "right")
        )

    def get_active_ports (self) -> tuple:
        active_ports = list_serial_ports.comports()
        list_ports = []

        for port in active_ports:
            list_ports.append(port.device)
    
        return tuple(list_ports)

