import tkinter as tk
from tkinter import ttk
from graph_window import GraphWindow

class MatrixWindow:
    def __init__(self, size, input_values={}):
        self.size = size
        self.input_values = input_values
        self.window = self.create_matrix_window()

    def create_matrix_window(self):
        window = tk.Tk()
        window.geometry('800x600')
        window.title('Adjacency Matrix')

        frame = tk.Frame(window, padx=20, pady=20) 
        frame.pack()

        self.entries = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                entry = tk.Entry(frame, width=5)
                entry.insert(0, str(self.input_values.get((i, j), '0')))
                entry.grid(row=i, column=j)
                row.append(entry)
            self.entries.append(row)

        generate_button = ttk.Button(frame, text='Generate', command=self.generate)
        generate_button.grid(row=self.size, column=0, columnspan=self.size)

        add_node_button = ttk.Button(frame, text='Add Node', command=self.add_node)
        add_node_button.grid(row=self.size+1, column=0, columnspan=self.size)

        window.update()

        return window

    def handle_events(self):
        self.window.mainloop()

    def generate(self):
        self.input_values = {(i, j): int(self.entries[i][j].get()) for i in range(self.size) for j in range(self.size)}
        traversal_order = [0, (0, 1), 1, (1, 2), 2, (2, 3), 3, (3, 4), 4, (4, 0)]
        GraphWindow(self.size, self.input_values)

    def add_node(self):
        self.input_values = {(i, j): int(self.entries[i][j].get()) for i in range(self.size) for j in range(self.size)}
        self.size += 1
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.destroy()
        self.window = self.create_matrix_window()
