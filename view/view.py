import tkinter as tk


def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def get_matrix():
    entries = []
    for i in range(n):
        row = []
        for j in range(n):
            entry = entry_fields[i][j].get()
            row.append(int(entry))
        entries.append(row)
    display_matrix(entries)


def create_matrix_form():
    global n, entry_fields

    n = int(entry.get())

    entry.destroy()
    submit_button.destroy()
    label.config(text=f"Enter {n}x{n} Matrix:")

    entry_fields = []
    for i in range(n):
        row_fields = []
        for j in range(n):
            field = tk.Entry(root, width=5)
            field.grid(row=i+2, column=j)
            row_fields.append(field)
        entry_fields.append(row_fields)

    display_button = tk.Button(root, text="Display Matrix", command=get_matrix)
    display_button.grid(row=n+3, column=0, columnspan=n, pady=10)


# Создание главного окна
root = tk.Tk()
root.title("Matrix Form")

# Ввод размерности матрицы
label = tk.Label(root, text="Enter the matrix dimension (n):")
label.grid(row=0, column=0, pady=10)
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=1, pady=10)
submit_button = tk.Button(root, text="Submit", command=create_matrix_form)
submit_button.grid(row=0, column=2, pady=10)

# Запуск главного цикла обработки событий
root.mainloop()
