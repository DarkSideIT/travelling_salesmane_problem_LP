import tkinter as tk
from tkinter import messagebox
import numpy as np

from methods.branchbound import tsp_branch_and_bound
from methods.ant import ant_solver
from methods.dynamic import tsp_dp
from plt import visualize_tsp_solution


def create_matrix(size):
    if matrix_frame.winfo_children():
        for widget in matrix_frame.winfo_children():
            widget.destroy()

    matrix_entries.clear()
    matrix_values = []
    for i in range(size):
        row = []
        values_row = []
        for j in range(size):
            entry = tk.Entry(matrix_frame, width=5)

            if i == j:  # Если на главной диагонали
                entry.insert(tk.END, "0")  # Установка значения в ноль
                entry.config(state="disabled")  # Блокировка редактирования

            entry.grid(row=i, column=j)
            row.append(entry)
            values_row.append(entry)

        matrix_entries.append(row)
        matrix_values.append(values_row)

    validate_matrix_entries()

    # Создание кнопок под матрицей
    button_frame = tk.Frame(matrix_frame)
    button_frame.grid(row=size, column=0, columnspan=size, pady=5)

    def process_function1():
        validate_matrix_entries()
        if error_label.cget("text") == "":
            result_path, result_cost = tsp_branch_and_bound(get_matrix_values(matrix_values))
            result_label.config(
                text=f"Метод ветвей и границ: Кратчайший путь: {result_path}, Цена такого пути: {result_cost}"
            )

    def process_function2():
        validate_matrix_entries()
        if error_label.cget("text") == "":
            result_path, result_cost = ant_solver(get_matrix_values(matrix_values))
            result_label.config(
                text=f"Муравиьный алгоритм: Кратчайший путь: {result_path}, Цена такого пути: {result_cost}"
            )

    def process_function3():
        validate_matrix_entries()
        if error_label.cget("text") == "":
            result_path, result_cost = tsp_dp(get_matrix_values(matrix_values))
            result_label.config(
                text=f"Динамическое программирование: Кратчайший путь: {result_path}, Цена такого пути: {result_cost}"
            )

    def show_result():
        matrix = get_matrix_values(matrix_values)
        if len(matrix) > 0:
            result_path, _ = tsp_branch_and_bound(matrix)
            for i in range(len(result_path)):
                result_path[i] = result_path[i] - 1
            visualize_tsp_solution(matrix, result_path)
        else:
            messagebox.showwarning("Пустая матрица", "Матрица не содержит данных.")

    branch_button = tk.Button(button_frame, text="Метод ветвей и границ", command=lambda: process_function1())
    branch_button.pack(side="left", padx=5)

    ant_button = tk.Button(button_frame, text="Муравьиный алгоритм", command=lambda: process_function2())
    ant_button.pack(side="left", padx=5)

    dp_button = tk.Button(
        button_frame, text="Алгоритм динамического программирования", command=lambda: process_function3()
    )
    dp_button.pack(side="left", padx=5)

    show_result_button = tk.Button(button_frame, text="Показать результат", command=show_result)
    show_result_button.pack(side="left", padx=5)

    return matrix_values


def get_matrix_values(matrix):
    values = []
    for row in matrix:
        row_values = []
        for entry in row:
            value = entry.get()
            if value.strip() == "":
                value = "0"  # Если строка пустая, установим значение в ноль
            row_values.append(float(value))
        values.append(row_values)
    return values


def validate_matrix_entries():
    error_label.config(text="")  # Очищаем предыдущее сообщение об ошибке
    has_error = False  # Флаг, указывающий на наличие ошибки
    for row in matrix_entries:
        for entry in row:
            value = entry.get().strip()
            if value:
                try:
                    float(value)
                    entry.config(fg="black")
                except ValueError:
                    entry.delete(0, tk.END)
                    entry.config(fg="red")
                    has_error = True  # Устанавливаем флаг ошибки
            else:
                entry.config(fg="black")
    if has_error:
        error_label.config(text="Ошибка: Введены неверные значения")



def clear_matrix_entries():
    for row in matrix_entries:
        for entry in row:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    error_label.config(text="")




root = tk.Tk()
root.title("Матрица")

size_var = tk.StringVar(root)
size_var.set("3")

size_label = tk.Label(root, text="Выберите размер матрицы:")
size_label.grid(row=0, column=0, columnspan=2)

size_select = tk.OptionMenu(root, size_var, *list(range(3, 15)), command=create_matrix)
size_select.grid(row=1, column=0, columnspan=2)

matrix_frame = tk.Frame(root)
matrix_frame.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2)

matrix_entries = []

clear_button = tk.Button(root, text="Очистить", command=clear_matrix_entries)
clear_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
