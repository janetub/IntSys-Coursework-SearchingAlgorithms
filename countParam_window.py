import tkinter as tk
from observer import Observer

class MiniWindow(Observer):

    def __init__(self, graph_window):
        # Register itself as an observer of the graph window
        graph_window.add_observer(self)

        # Initialize other attributes
        self.window = None
        self.count_label = None
        self.step_label = None

    def update(self, observable, args):
        # Update itself based on the notification from the graph window
        if args == "start_search":
            # Create a mini window to show the count parameters and the search steps
            self.window = tk.Toplevel(observable.root)
            self.window.title("Search Log")
            self.window.geometry("200x200")

            # Create a label to show the count parameters
            self.count_label = tk.Label(self.window, text="Count Parameters")
            self.count_label.pack()

            # Create a label to show the search steps
            self.step_label = tk.Label(self.window, text="Search Steps")
            self.step_label.pack()

        elif args == "update_search":
            # Update the count parameters and the search steps based on the search algorithm
            search_algorithm = observable.search_algorithm
            self.count_label.config(text=f"Number of nodes visited: {search_algorithm.num_nodes_visited}\nMaximum queue size: {search_algorithm.max_queue_size}")
            self.step_label.config(text=f"Current step: {search_algorithm.path[-1]}")