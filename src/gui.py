import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from methods import euler, improved_euler
import matplotlib.pyplot as plt

#Para visualizar la ventana con la grafica y cuadriculas
def plot_graph(xs, ys, method_name):
    plt.figure(figsize=(6, 4))
    plt.plot(xs, ys, label=method_name)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(method_name)
    plt.legend()
    plt.grid(True)
    plt.show()

#Para hacer calculitos en la calculadora grafica
def calculate(func, entry_x0, entry_y0, entry_h, entry_n, entry_function):
    try:
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        h = float(entry_h.get())
        n = int(entry_n.get())
        func_eval = lambda x, y: eval(entry_function.get())

        if func == "Euler":
            xs, ys = euler(func_eval, x0, y0, h, n)
        else:
            xs, ys = improved_euler(func_eval, x0, y0, h, n)

        plot_graph(xs, ys, func)
    except Exception as e:
        messagebox.showerror("Error", str(e))

#mostrar una ventana aparte con info extra
def open_info_window():
    info_window = tk.Toplevel()
    info_window.title("Diferencias entre Euler y Euler Mejorado")
    
    info_text = tk.Text(info_window, wrap='word', font=('Arial', 12), height=10, width=50)
    info_text.pack(padx=10, pady=10)
    
    info_text.insert(tk.END, "El método de Euler es un algoritmo simple para la resolución numérica de ecuaciones diferenciales ordinarias (EDO) con un valor inicial dado. "
                             "Sin embargo, tiende a acumular errores a medida que avanza en el intervalo de tiempo especificado. "
                             "El método de Euler mejorado, también conocido como método de Euler-Cauchy, es una mejora del método de Euler que reduce estos errores acumulativos "
                             "al tomar en cuenta la pendiente promedio en lugar de la pendiente en el punto inicial solamente.\n\n"
                             "En resumen, el método de Euler mejorado es más preciso que el método de Euler estándar, "
                             "pero también requiere más cálculos por iteración.")

#mostrar la ventana principal
def show_gui():
    root = tk.Tk()
    root.title("Método de Euler y Método de Euler mejorado")

    style = ttk.Style()
    style.configure('TFrame', background='#f0f0f0')
    style.configure('TButton', background='#007bff', foreground='black')
    style.map('TButton', background=[('active', '#0056b3')])

    main_frame = ttk.Frame(root)
    main_frame.grid(row=0, column=0, padx=40, pady=20)

    func_frame = ttk.Frame(main_frame)
    func_frame.grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(func_frame, text="Seleccionar Método:", font=('Arial', 12), padx=10, pady=5).grid(row=0, column=0)
    method_var = tk.StringVar()
    method_var.set("Euler")
    ttk.Radiobutton(func_frame, text="Euler", variable=method_var, value="Euler").grid(row=0, column=1, padx=5)
    ttk.Radiobutton(func_frame, text="Euler Mejorado", variable=method_var, value="Improved Euler").grid(row=0, column=2, padx=5)

    input_frame = ttk.Frame(main_frame)
    input_frame.grid(row=1, column=0, padx=10, pady=10)

    tk.Label(input_frame, text="x0:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky='e')
    entry_x0 = ttk.Entry(input_frame, font=('Arial', 12))
    entry_x0.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="y0:", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky='e')
    entry_y0 = ttk.Entry(input_frame, font=('Arial', 12))
    entry_y0.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="h:", font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5, sticky='e')
    entry_h = ttk.Entry(input_frame, font=('Arial', 12))
    entry_h.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="n:", font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5, sticky='e')
    entry_n = ttk.Entry(input_frame, font=('Arial', 12))
    entry_n.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="f(x,y):", font=('Arial', 12)).grid(row=4, column=0, padx=5, pady=5, sticky='e')
    entry_function = ttk.Entry(input_frame, font=('Arial', 12))
    entry_function.grid(row=4, column=1, padx=5, pady=5)

    calculate_button = ttk.Button(main_frame, text="Calcular", command=lambda: calculate(method_var.get(), entry_x0, entry_y0, entry_h, entry_n, entry_function))
    calculate_button.grid(row=2, column=0, columnspan=1, pady=10)

   

    # Glosario
    glossary_frame = ttk.Frame(main_frame)
    glossary_frame.grid(row=1, column=1, padx=80, pady=20, sticky='n')

    tk.Label(glossary_frame, text="Glosario:", font=('Arial', 12, 'underline')).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    tk.Label(glossary_frame, text="x0: Punto inicial en x", font=('Arial', 11, 'italic')).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    tk.Label(glossary_frame, text="y0: Punto inicial en y", font=('Arial', 11, 'italic')).grid(row=3, column=0, padx=10, pady=10, sticky='w')
    tk.Label(glossary_frame, text="h: Tamaño del paso", font=('Arial', 11, 'italic')).grid(row=5, column=0, padx=10, pady=10, sticky='w')
    tk.Label(glossary_frame, text="n: Número de iteraciones", font=('Arial', 11, 'italic')).grid(row=7, column=0, padx=10, pady=10, sticky='w')
    tk.Label(glossary_frame, text="f(x,y): Función diferencial", font=('Arial', 11, 'italic')).grid(row=9, column=0, padx=10, pady=10, sticky='w')

    info_button = ttk.Button(main_frame, text="Ver Diferencias", command=open_info_window)
    info_button.grid(row=2, column=1, columnspan=2, pady=10)

    root.mainloop()
