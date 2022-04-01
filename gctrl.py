
from settings import *
from menus import MainMenu

if __name__ == "__main__":
    main_menu = MainMenu()

    global_values.upload_serial_info = main_menu.upload_serial_info
    global_values.upload_cnc_axis = main_menu.upload_cnc_axis
    global_values.upload_cnc_home = main_menu.upload_cnc_home

    main_menu.init_menu()

