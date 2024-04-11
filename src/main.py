from gui import show_gui

def main():
    # recibimos las variables globales desde la funcion show_gui()
    global entry_x0, entry_y0, entry_h, entry_n, entry_function
    entry_x0, entry_y0, entry_h, entry_n, entry_function = show_gui()
    print("Variables creadas:", entry_x0, entry_y0, entry_h, entry_n, entry_function)

if __name__ == "__main__":
    main()
