
import tkinter as tk
from tkinter import ttk

background_color = "#333333"
foreground_color = "#e9e9e9"

def color_changer (base_color, added_color, mode="+"):
    """ Takes a hexadecimal color and adds other hexadecimal color. Returning the result as a string """
    
    operator = 1
    
    if mode == "-":
        operator = -1

    new_color = f"#{hex(int(base_color[1:], 16) + (int(added_color, 16) * operator))[2:]}"

    return new_color

class Base ():
    """ Creates the bases of Tkinter GUI """
    def __init__ (self, title, percentage_width, percentage_height, tk_root=False):
        if tk_root:
            self.root = tk.Tk(className=title)
        else:
            self.root = tk.Toplevel()
            self.root.wm_title(title)

        self.__calculate_size(percentage_width, percentage_height)
        self.__style()

    def __calculate_size (self, size_width=0.5, size_height=0.5):
        """ Get size of the screen, calculate and set the size of the base element """

        # Get Screen's Size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate Base's Size
        base_width = int(screen_width * size_width)
        base_height = int(screen_height * size_height)
        self.width = base_width
        self.height = base_height

        # Calculate Base's
        align_x = int( (screen_width - base_width) / 2)
        align_y = int( (screen_height - base_height) / 2)

        # Set Base's Size 
        self.root.geometry(f"{base_width}x{base_height}+{align_x}+{align_y}")

    def __style (self):
        """ Styles the Base """
        self.root.configure(
                bg=background_color,
                padx=20,
                pady=20
        )

    def tk_loop (self):
        """ Initialize the main window, base, loop """
        self.root.mainloop()

class Div ():
    """ Create a Wrapper or Divisons, CSS and HTML like """
    def __init__ (self, tk_father, pack_options=(0, "both", "top")):
        self.div = tk.Frame(
            tk_father,
            bg=background_color
        )

        self.div.pack(
            expand=pack_options[0],
            fill=pack_options[1],
            side=pack_options[2]
        )

    def add_border (self):
        border_color = color_changer(background_color, "444444")

        self.div.configure(
            highlightbackground=border_color,
            highlightthickness=2,
            padx=5,
            pady=5
        )

    def hide_div (self):
        self.div.pack_forget()

class Text ():
    """ Create a Label with Text """
    def __init__ (self, tk_father, content, pack_options=(0, "both", "top")):
        self.text = ttk.Label(
            tk_father,
            padding=(20, 5),
            font=("Liberation Sans", 18),
            foreground=foreground_color,
            background=background_color,
            text=content,
            anchor="center"
        )
        
        self.text.pack(
            expand=pack_options[0],
            fill=pack_options[1],
            side=pack_options[2]
        )

    def change_font_color (self, new_color):
        """ Changes the color of the font """
        self.text.configure(
            foreground=new_color
        )

    def change_content (self, new_text):
        self.text.configure(
            text=new_text
        )

class Title (Text):
    """ Bigger text labels, for titles & important subjects """
    def __init__ (self, tk_father, content, pack_options=(1, "both", "top")):
        super().__init__(tk_father, content, pack_options)

        self.text.configure(
            font=("Liberation Sans", 32, "bold")
        )

class SubTitle (Text):
    """ Bigger Text, but not that much bigger than a title """
    def __init__ (self, tk_father, content, pack_options=(1, "both", "top")):
        super().__init__(tk_father, content, pack_options)

        self.text.configure(
            font=("Liberation Sans", 24, "bold")
        )

class Bl4ky113 (Text):
    """ Made by who? """
    def __init__ (self, tk_father, content, pack_options=(1, "both", "top")):
        super().__init__(tk_father, content, pack_options)

        font_color = color_changer(foreground_color, "656565", "-")

        self.change_font_color(font_color)
        self.text.configure(
            font=("Liberation Mono", 18, "bold")
        )

class Label (Text):
    """ Text Labels for Information """
    def __init__ (self, tk_father, content, pack_options=(1, "both", "top")):
        super().__init__(tk_father, content, pack_options)

        font_color = color_changer(foreground_color, "222222", "-")

        self.change_font_color(font_color)
        self.text.configure(
            borderwidth=2,
            font=("Liberation Mono", 15, "bold"),
            anchor="w"
        )

class Button ():
    """ Creates a Button Input """
    def __init__ (self, tk_father, onclick_function, content, pack_options=((5, 5), (5, 5), "top")):
        bg_normal = color_changer(background_color, "111111")
        bg_hover = color_changer(background_color, "222222")

        self.btn = tk.Button(
            tk_father,
            font=("Libre Sans", 16, "bold"),
            text=content,
            command=onclick_function,
            background=bg_normal,
            foreground=foreground_color,
            activebackground=bg_hover,
            activeforeground=foreground_color,
            border=0
        )
        self.btn.pack(
            ipadx=pack_options[0][0],
            ipady=pack_options[0][1],
            padx=pack_options[1][0],
            pady=pack_options[1][1],
            side=pack_options[2]
        )

class ListBox ():
    """ Creates a ListBox Input """
    def __init__ (self, tk_father, list_options, pack_options=(1, "both", "top")):
        self.listbox = tk.Listbox(
            tk_father,
            background=background_color,
            foreground=foreground_color,
            font=("Libre Mono", 14, "bold"),
            highlightcolor=foreground_color,
            border=0
        )

        index_options = 0
        for option in list_options:
            self.listbox.insert(index_options, option)
            index_options += 1
        
        self.listbox.pack(
            ipadx=25,
            ipady=5,
            expand=pack_options[0],
            fill=pack_options[1],
            side=pack_options[2]
        )

    def get_selected_value (self):
        try:
            selected_value = self.listbox.get(self.listbox.curselection()[0])
            return selected_value
        except IndexError:
            return None

    def add_values (self, values_list):
        self.listbox.delete(0, "end")

        index_value = 0
        for value in values_list:
            self.listbox.insert(index_value, value)
            index_value += 1

class Canvas ():
    """ Creates a Canvas Element, for drawing the CNC info """
    def __init__ (self, tk_father, width, height, pack_options="top"):
        self.w = width
        self.h = height
        self.home = (0, 0)
        self.current = (0, 0)
        self.z_home = 0
        self.z_current = 0
        self.current_color = "#C80000"
        self.home_color = "#0000C8"
        self.equal_color = "#700070"

        background_canvas = color_changer(background_color, "222222")

        self.canvas = tk.Canvas(
            tk_father,
            background=background_canvas,
            border=0,
            width=self.w,
            height=self.h
        )

        self.canvas.pack(
            side=pack_options,
            padx=10,
            pady=10
        )

        self.__create_axis()

    def __create_axis (self):
        """ Draws and creates an Axis in the Canvas """
        self.canvas.create_line(
            (self.w * 0.04), (self.h * 0.05),
            (self.w - (self.w * 0.2)), (self.h * 0.05),
            fill=foreground_color,
            width=4,
            tag="axis"
        )

        self.canvas.create_line(
            (self.w * 0.05), (self.h * 0.04),
            (self.w * 0.05), (self.h - (self.h * 0.2)),
            fill=foreground_color,
            width=4,
            tag="axis"
        )

        self.canvas.create_line(
            (self.w - (self.w * 0.1)), (self.h * 0.04),
            (self.w - (self.w * 0.1)), (self.h - (self.h * 0.20)),
            fill=foreground_color,
            width=4,
            tag="axis"
        )

        self.len_x_axis = (self.w - (self.w * 0.2)) - (self.w * 0.05)
        self.zero_x_axis = (self.w * 0.05, self.h * 0.05)

        self.len_y_axis = (self.h - (self.h * 0.2)) - (self.h * 0.05)
        self.zero_y_axis = (self.w * 0.05, self.h * 0.05)

        self.len_z_axis = (self.h - (self.h * 0.2)) - (self.h * 0.05)
        self.zero_z_axis = (self.w - (self.w * 0.1), self.h * 0.05)

    def change_axis_position (self, element="home", coords=(0, 0)):
        anti_element = "current"

        if element == "current":
            anti_element = "home"

        color = getattr(self, f"{element}_color")

        self.canvas.delete(element)

        if coords == getattr(self, anti_element):
            self.canvas.delete(anti_element)
            self.__draw_axis_position(self.equal_color, 6, coords, element)
        else:
            self.__draw_axis_position(color, 4, coords, element)

        if element == "current":
            self.current = coords
        elif element == "home":
            self.home = coords

    def __draw_axis_position (self, color, size=1, cnc_coords=(0, 0), tag=""):
        canvas_coords = (
                self.__transform_cnc_value_to_canvas(cnc_coords[0], "x", 0),
                self.__transform_cnc_value_to_canvas(cnc_coords[1], "y", 1)
        )
        
        self.canvas.create_oval(
            canvas_coords[0] - size, canvas_coords[1] - size,
            canvas_coords[0] + size, canvas_coords[1] + size,
            fill=color,
            tags=tag
        )

    def change_z_position (self, element="home", coord=0):
        anti_element = "current"

        if element == "current":
            anti_element = "home"

        color = getattr(self, f"{element}_color")

        self.canvas.delete(f"z_{element}")

        if coord == getattr(self, f"z_{anti_element}"):
            self.canvas.delete(f"z_{anti_element}")
            self.__draw_z_position(self.equal_color, 6, coord, f"z_{element}")
        else:
            self.__draw_z_position(color, 4, coord, f"z_{element}")

        if element == "current":
            self.z_current = coord
        elif element == "home":
            self.z_home = coord

    def __draw_z_position (self, color, size=1, cnc_coord=0, tag=""):
        canvas_coord = self.__transform_cnc_value_to_canvas(cnc_coord, "z", 1)

        self.canvas.create_oval(
            self.zero_z_axis[0] - size, canvas_coord - size,
            self.zero_z_axis[0] + size, canvas_coord + size,
            fill=color,
            tags=tag
        )

    def __transform_cnc_value_to_canvas (self, value=0, axis="x", direction_axis=0):
        div_axis = getattr(self, f"div_{axis}")
        len_axis = getattr(self, f"zero_{axis}_axis")[direction_axis]

        canvas_value = (value * div_axis) + len_axis

        return canvas_value

    def set_num_axis_divisions (self, x_division, y_division, z_division):
        self.div_x = self.len_x_axis / x_division
        self.div_y = self.len_y_axis / y_division
        self.div_z = self.len_z_axis / z_division

        self.change_axis_position("home", self.home)
        self.change_axis_position("current", self.current)
        self.change_z_position("home", self.z_home)
        self.change_z_position("current", self.z_current)

        self.canvas.create_oval(
            (self.w * 0.05) - 4, (self.h - (self.h * 0.15)) - 4,
            (self.w * 0.05) + 4, (self.h - (self.h * 0.15)) + 4,
            fill=self.current_color,
            tags="axis"
        )
        self.canvas.create_text(
            (self.w * 0.08), (self.h - (self.h * 0.15)),
            font=("Libre Mono", int(self.h * 0.03), "bold"),
            justify="left",
            anchor="w",
            text="Current Position",
            fill=foreground_color,
            tag="axis"
        )

        self.canvas.create_oval(
            (self.w * 0.05) - 4, (self.h - (self.h * 0.10)) - 4,
            (self.w * 0.05) + 4, (self.h - (self.h * 0.10)) + 4,
            fill=self.home_color,
            tags="axis"
        )
        self.canvas.create_text(
            (self.w * 0.08), (self.h - (self.h * 0.10)),
            font=("Libre Mono", int(self.h * 0.03), "bold"),
            justify="left",
            anchor="w",
            text="Home Position",
            fill=foreground_color,
            tag="axis"
        )

        self.canvas.create_oval(
            (self.w * 0.05) - 6, (self.h - (self.h * 0.05)) - 6,
            (self.w * 0.05) + 6, (self.h - (self.h * 0.05)) + 6,
            fill=self.equal_color,
            tags="axis"
        )
        self.canvas.create_text(
            (self.w * 0.08), (self.h - (self.h * 0.05)),
            font=("Libre Mono", int(self.h * 0.03), "bold"),
            justify="left",
            anchor="w",
            text="Home and Current Position Merged",
            fill=foreground_color,
            tag="axis"
        )
