# IntSys-Coursework-SearchingAlgorithms

This repository contains Python scripts for implementing various search algorithms in an interactive graph environment. The project is structured as follows:

## Files

### 1. `countParam_window.py`
This file contains the `MiniWindow` class which inherits from the `Observer` class. The `MiniWindow` class is used to create a mini window that displays the count parameters and the search steps during the execution of a search algorithm.

### 2. `graph_window.py`
This file contains the `GraphWindow` class which is used to create an interactive graph window. The graph window allows the user to select a search algorithm, input the start and end nodes, and visualize the execution of the search algorithm on the graph.

### 3. `main.py`
This is the main entry point of the application. It creates a `MatrixWindow` instance and starts the event loop.

### 4. `matrix_window.py`
This file contains the `MatrixWindow` class which is used to create a window for inputting the adjacency matrix of the graph. The user can add nodes to the graph and generate the graph window from this matrix window.

### 5. `search_algorithms.py`
This file contains various search algorithm classes, including `SearchAlgorithm` and `BFS`. Each search algorithm class has a `search` method that implements the search algorithm.

## Usage
To run the application, execute the `main.py` script. This will open the matrix window where you can input the adjacency matrix of the graph and add nodes to the graph. After inputting the adjacency matrix, click the 'Generate' button to open the graph window. In the graph window, select a search algorithm, input the start and end nodes, and click the 'Start Search' button to start the search.

## Dependencies
The application requires Python 3 and the following Python libraries:
- `tkinter`
- `collections`
- `math`

Please ensure that you have these dependencies installed before running the application.