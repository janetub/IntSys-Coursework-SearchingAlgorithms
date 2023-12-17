# main.py
from matrix_window import MatrixWindow

def main():
    size = 3
    input_values = {}
    matrix_window = MatrixWindow(size, input_values)
    matrix_window.handle_events()

if __name__ == "__main__":
    main()