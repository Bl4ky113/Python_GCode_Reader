
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

class Title (Text):
    """ Bigger text labels, for titles & important subjects """
    def __init__ (self, tk_father, content, pack_options=(1, "both", "top")):
        super().__init__(tk_father, content, pack_options)

        self.text.configure(
            font=("Liberation Sans", 32, "bold")
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
    def __init__ (self, tk_father, list_options, pack_options=()):
        self.listbox = tk.Listbox(
            tk_father,
            background=background_color,
            foreground=foreground_color,
            font=("Libre Sans", 16, "bold"),
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
        return self.listbox.get(self.listbox.curselection()[0])
