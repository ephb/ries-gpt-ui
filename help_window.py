from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
import os
import json

# Ctrl-h function in MainWindow opens a HelpWindow
# Toplevel specifies that this is a subclass of another tkinter window
class HelpWindow(Toplevel): 
    def __init__(self, parent, attributes=None):
        super().__init__(parent)
        self.title("HelpWindow")
        self.parent = parent
        self.resizable(False, False)
        self.cur_file_index = 0
        self.cur_char_index = ""

        self.attr = attributes

        # 
        if self.attr:
            self.geometry(self.attr["position"])
        else: # redundant with default attribute settings in MainWindow
            self.geometry("+100+100")    


        # different ways to close
        self.bind("<Control-h>", self.on_close) # toggle window
        self.bind("<Escape>", self.on_close)
        self.protocol("WM_DELETE_WINDOW", self.on_close) 

    # parent MainWindow cleanup:
    # remove highlights
    # store current window position and search string
    def on_close(self, event=None):
        self.parent.thread_box.tag_remove("highlight", "1.0", END)
        self.parent.help_window = None
        self.parent.help_window_attributes["position"] = self.geometry()
        super().destroy()                                                           