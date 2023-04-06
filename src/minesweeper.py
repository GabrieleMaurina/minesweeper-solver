import tkinter as tk


DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 20
CELL_SIZE = 20


class Minesweeper:
    def __init__(self):
        self.root = tk.Tk()
        self.create_settings_page()
        self.create_main_page()
        self.show_settings_page()
        self.root.mainloop()

    def create_settings_page(self):
        self.settings_page_frame = tk.Frame(self.root)
        self.integer_only = (
            (self.root.register(lambda v: str.isdigit(v))), '%P')
        self.width_label = tk.Label(self.settings_page_frame, text='Width')
        self.width_label.grid(row=0, column=0)
        self.width_variable = tk.StringVar(self.root, DEFAULT_WIDTH)
        self.width_entry = tk.Entry(
            self.settings_page_frame, width=4, textvariable=self.width_variable, validate='all', validatecommand=self.integer_only)
        self.width_entry.grid(row=0, column=1)
        self.height_label = tk.Label(self.settings_page_frame, text='Height')
        self.height_label.grid(row=1, column=0)
        self.height_variable = tk.StringVar(self.root, DEFAULT_HEIGHT)
        self.height_entry = tk.Entry(
            self.settings_page_frame, width=4, textvariable=self.height_variable, validate='all', validatecommand=self.integer_only)
        self.height_entry.grid(row=1, column=1)
        self.start_button = tk.Button(
            self.settings_page_frame, text='Start', command=self.show_main_page)
        self.start_button.grid(row=2, column=0, columnspan=2)

    def create_main_page(self):
        self.main_page_frame = tk.Frame(self.root)
        self.main_page_frame.grid_columnconfigure(0, weight=0)
        self.main_page_frame.grid_columnconfigure(1, weight=0)
        self.main_page_frame.grid_columnconfigure(2, weight=0)
        self.main_page_frame.grid_columnconfigure(3, weight=1)
        self.back_button = tk.Button(
            self.main_page_frame, text='Back', command=self.show_settings_page)
        self.back_button.grid(row=0, column=0)
        self.next_button = tk.Button(
            self.main_page_frame, text='Next', command=None)
        self.next_button.grid(row=0, column=1)
        self.solve_button = tk.Button(
            self.main_page_frame, text='Solve', command=None)
        self.solve_button.grid(row=0, column=2)
        self.canvas = tk.Canvas(self.main_page_frame,
                                width=CELL_SIZE * self.width(), height=CELL_SIZE * self.height())
        self.canvas.grid(row=1, column=0, columnspan=4)

    def show_settings_page(self):
        self.settings_page_frame.pack()
        self.main_page_frame.pack_forget()

    def show_main_page(self):
        self.main_page_frame.pack()
        self.settings_page_frame.pack_forget()

    def width(self):
        try:
            return int(self.width_variable.get())
        except ValueError:
            return DEFAULT_WIDTH

    def height(self):
        try:
            return int(self.height_variable.get())
        except ValueError:
            return DEFAULT_HEIGHT


def main():
    Minesweeper()


if __name__ == '__main__':
    main()
