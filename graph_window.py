
from collections import deque
import tkinter as tk
from tkinter import ttk
import math
from search_algorithms import SearchAlgorithm, BFS

class GraphWindow:
    def __init__(self, size, input_values):
        self.size = size
        self.input_values = input_values # adjacency matrix
        self.create_window()

    def create_window(self):
        
        # Forming window
        root = tk.Tk()
        root.title("Interactive Graph")
        root.geometry("800x600")

        # Frame for top panel
        top_panel = ttk.Frame(root)
        top_panel.pack(side="top", fill="x")

        # Frame for animation control frame
        control_frame = ttk.Frame(top_panel)
        control_frame.pack(side="left")

        # Frame for algorithm selection frame
        search_options_frame = ttk.Frame(top_panel)
        search_options_frame.pack(side="left")

        # Dropdown for algorithm selection
        self.algo_var = tk.StringVar()
        algo_dropdown = ttk.OptionMenu(search_options_frame, self.algo_var, "BFS", "BFS", "DFS", "A*", "Hill Climbing", "Beam", "Branch and Bound")
        algo_dropdown.pack(side="left")

        # Entry for start node
        self.start_node_entry = ttk.Entry(search_options_frame, width=10)
        self.start_node_entry.pack(side="left")
        self.start_node_entry.bind("<KeyRelease>", self.update_start_node)

        # Entry for end node
        self.end_node_entry = ttk.Entry(search_options_frame, width=10)
        self.end_node_entry.pack(side="left")
        self.end_node_entry.bind("<KeyRelease>", self.update_end_node)

        # Button to start the search
        start_button = ttk.Button(search_options_frame, text="Start Search", command=self.start_search)
        start_button.pack(side="left")

        # Frame for canvas
        canvas_frame = ttk.Frame(root)
        canvas_frame.pack(side="top", fill="both", expand=True)

        # Visualizing Graph
        circle_positions = [(400 + 200 * math.cos(2 * math.pi * i / self.size), 300 + 200 * math.sin(2 * math.pi * i / self.size)) for i in range(self.size)]

        canvas = tk.Canvas(canvas_frame, width=600, height=600, bg='white')
        canvas.pack(fill="both", expand=True)

        node_ids = [canvas.create_oval(pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20, fill="blue") for pos in circle_positions]

        text_ids = [canvas.create_text(pos[0], pos[1], text=str(i), font=("Arial", 16)) for i, pos in enumerate(circle_positions)]

        edge_ids = []
        for i in range(self.size):
            for j in range(self.size):
                if self.input_values.get((i, j), False):
                    pos1 = canvas.coords(node_ids[i])
                    pos2 = canvas.coords(node_ids[j])
                    edge_id = canvas.create_line((pos1[0]+pos1[2])/2, (pos1[1]+pos1[3])/2, (pos2[0]+pos2[2])/2, (pos2[1]+pos2[3])/2)
                    # Create edge weight (text) and store its id
                    edge_text_id = canvas.create_text(((pos1[0]+pos1[2])/2 + (pos2[0]+pos2[2])/2) / 2, ((pos1[1]+pos1[3])/2 + (pos2[1]+pos2[3])/2) / 2, text=str(self.input_values.get((i, j), '')), font=("Arial", 16))
                    edge_ids.append((edge_id, edge_text_id, i, j))  # Store the edge weight id with the edge id

        

        # def traverse_graph_step(step=0):
        #     animation_speed = tk.DoubleVar(value=speed_slider.get())
        #     if animation_running.get() and 0 <= step < len(self.traversal_order):
        #         item = self.traversal_order[step]
        #         if isinstance(item, int) and 0 <= item < len(node_ids):
        #             highlight_node(node_ids[item], "green")
        #         elif isinstance(item, tuple) and len(item) == 2:
        #             i, j = item
        #             if 0 <= i < len(node_ids) and 0 <= j < len(node_ids):
        #                 highlight_edge(item, "green")
        #         root.after(int(1000 / animation_speed.get()), traverse_graph_step, step + 1)  # Schedule the next step
        #     else:
        #         # All steps are done or animation is paused, reset highlights
        #         root.after(0, reset_highlights)

        # def traverse_graph():
        #     traverse_graph_step()

        # Make them instance variables
        self.animation_running = tk.BooleanVar(value=False)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.edge_ids = []

        # Create a mini window for the counting parameters
        self.count_window = tk.Toplevel()
        self.count_window.title("Counting Parameters")
        self.count_display = tk.Text(self.count_window, width=30, height=10)
        self.count_display.pack()
        
    def highlight_edge(self, edge, color="red"):
        """Change the color of an edge."""
        if not self.animation_running.get():
            return
        # Find the edge ID in the edge_ids list
        edge_id = next((id for id, _, node1, node2 in self.edge_ids if (node1, node2) == edge), None)
        if edge_id is not None:
            self.canvas.itemconfig(edge_id, fill=color)
            self.root.update()  # Update the window

    def reset_highlights(self):
        self.animation_running.set(False)
        for node_id in self.node_ids:
            self.canvas.itemconfig(node_id, fill="blue")
        for edge_id, _, _, _ in self.edge_ids:
            self.canvas.itemconfig(edge_id, fill="black")
        self.speed_slider.set(1.0)

    def on_click(self, event):
        # Check if a node is clicked
        for node_id in self.node_ids:
            node_pos = self.canvas.coords(node_id)
            if node_pos[0] <= event.x <= node_pos[2] and node_pos[1] <= event.y <= node_pos[3]:
                self.selected_node_id = node_id
                self.original_pos = (event.x, event.y)
                break

    def on_drag(self, event):
        # If a node is selected, move it within canvas boundaries
        if self.selected_node_id is not None:
            dx = event.x - self.original_pos[0]
            dy = event.y - self.original_pos[1]
            new_pos = self.canvas.coords(self.selected_node_id)[0] + dx, self.canvas.coords(self.selected_node_id)[1] + dy
            if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] <= self.canvas.winfo_width() and new_pos[1] <= self.canvas.winfo_height():
                self.canvas.move(self.selected_node_id, dx, dy)
                # Move the node number (text) with the node
                text_id = self.text_ids[self.node_ids.index(self.selected_node_id)]
                self.canvas.move(text_id, dx, dy)
                self.original_pos = (event.x, event.y)
                self.update_edges()

    def on_release(self, event):
        # Release the selected node
        self.selected_node_id = None

    def on_resize(self, event):
        # Resize the canvas
        self.canvas.config(width=event.width, height=event.height)

    def on_close(self):
        self.window_closed.set(True)
        self.root.destroy()


        animation_running = tk.BooleanVar(value=False)

        # Speed/Animation Control Buttons
        pause_button = ttk.Button(control_frame, text="Pause", command=lambda: animation_running.set(False))
        pause_button.pack(side="left")

        # play_button = ttk.Button(control_frame, text="Play", command=lambda: [animation_running.set(True), traverse_graph()])
        # play_button.pack(side="left")

        speed_slider = ttk.Scale(control_frame, from_=0.1, to=10.0, value=1.0, orient="horizontal")
        speed_slider.pack(side="left")
        
        reset_button = ttk.Button(control_frame, text="Reset", command=reset_highlights)
        reset_button.pack(side="left")
        
        # Variables to store the selected node and its original position
        selected_node_id = None
        original_pos = None

        # Node interactions
        def update_edges():
            # Update the positions of the edges connected to the moved node
            for edge_id, edge_text_id, node1, node2 in edge_ids:
                pos1 = canvas.coords(node_ids[node1])
                pos2 = canvas.coords(node_ids[node2])
                canvas.coords(edge_id, (pos1[0]+pos1[2])/2, (pos1[1]+pos1[3])/2, (pos2[0]+pos2[2])/2, (pos2[1]+pos2[3])/2)
                # Update the position of the edge weight
                canvas.coords(edge_text_id, ((pos1[0]+pos1[2])/2 + (pos2[0]+pos2[2])/2) / 2, ((pos1[1]+pos1[3])/2 + (pos2[1]+pos2[3])/2) / 2)

        def on_click(event):
            nonlocal selected_node_id, original_pos
            # Check if a node is clicked
            for node_id in node_ids:
                node_pos = canvas.coords(node_id)
                if node_pos[0] <= event.x <= node_pos[2] and node_pos[1] <= event.y <= node_pos[3]:
                    selected_node_id = node_id
                    original_pos = (event.x, event.y)
                    break

        def on_drag(event):
            nonlocal selected_node_id, original_pos
            # If a node is selected, move it within canvas boundaries
            if selected_node_id is not None:
                dx = event.x - original_pos[0]
                dy = event.y - original_pos[1]
                new_pos = canvas.coords(selected_node_id)[0] + dx, canvas.coords(selected_node_id)[1] + dy
                if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] <= canvas.winfo_width() and new_pos[1] <= canvas.winfo_height():
                    canvas.move(selected_node_id, dx, dy)
                    # Move the node number (text) with the node
                    text_id = text_ids[node_ids.index(selected_node_id)]
                    canvas.move(text_id, dx, dy)
                    original_pos = (event.x, event.y)
                    update_edges()

        def on_release(event):
            nonlocal selected_node_id
            # Release the selected node
            selected_node_id = None

        def on_resize(event):
            # Resize the canvas
            canvas.config(width=event.width, height=event.height)

        root.update()

        root.bind("<Configure>", on_resize)
        canvas.bind("<Button-1>", on_click)
        canvas.bind("<B1-Motion>", on_drag)
        canvas.bind("<ButtonRelease-1>", on_release)

        # Create a Tkinter variable to track if the window is closed
        window_closed = tk.BooleanVar(value=False)

        def on_close():
            nonlocal window_closed
            window_closed.set(True)
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_close)

        # Wait for the window to be closed
        root.wait_window()

        return node_ids, edge_ids
    
    def start_search(self):
        # Get the selected algorithm from the dropdown
        algo = self.algo_var.get()
        # Create an instance of the selected algorithm class
        if algo == "BFS":
            search_algo = BFS(self)
        # ... other algorithms ...
        
        # Get the start and end nodes from the entry fields
        try:
            start_node = int(self.start_node_entry.get())
        except ValueError:
            print("Please enter a valid start node.", self.start_node_entry.get())
            return

        try:
            end_node = int(self.end_node_entry.get())
        except ValueError:
            print("Please enter a valid end node.")
            return

        # Start the search
        search_algo.search(start_node, end_node)

    def update_start_node(self, event):
        try:
            self.start_node = int(self.start_node_entry.get())
        except ValueError:
            print("Please enter a valid start node.")

    def update_end_node(self, event):
        try:
            self.end_node = int(self.end_node_entry.get())
        except ValueError:
            print("Please enter a valid end node.")

    def highlight_node(self, node_id, color="red"):
        """Change the color of a node."""
        if not self.animation_running.get():
            return
        self.canvas.itemconfig(node_id, fill=color)
        self.root.update()  # Update the window

    def highlight_edge(self, edge, color="red"):
        """Change the color of an edge."""
        if not self.animation_running.get():
            return
        # Find the edge ID in the edge_ids list
        edge_id = next((id for id, _, node1, node2 in self.edge_ids if (node1, node2) == edge), None)
        if edge_id is not None:
            self.canvas.itemconfig(edge_id, fill=color)
            self.root.update()  # Update the window
    
    def update_count_display(self, count_parameters):
        # Update the text in the mini window with the current values of the counting parameters
        count_text = "\n".join(f"{param}: {value}" for param, value in count_parameters.items())
        self.count_display.delete(1.0, tk.END)  # Clear the current text
        self.count_display.insert(tk.END, count_text)  # Insert the new text