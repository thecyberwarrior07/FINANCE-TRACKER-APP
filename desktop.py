import sqlite3
import tkinter as tk 
from tkinter import messagebox


conn= sqlite3.connect("expenses.db")
curser = conn.cursor()

curser.execute('''
CREATE TABLE IF NOT EXISTS expenses(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               NAME text,
               AMOUNT real,
               CATEGORY text
)
''')

conn.commit

expenses = []



def add_expenses():
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    curser.execute(
        "INSERT INTO expenses (name, amount, category) VALUES (?,?,?)",
        (name, amount, category)
    )
    conn.commit()

    expense_list.insert(tk.END,f"{name}  - ₹{amount} {category}")

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

def previous_expense():
    expense_list.delete(0, tk.END)
    curser.execute("SELECT name, amount, category FROM expenses")
   
    rows = curser.fetchall()

    for row in rows :
        expense_list.insert(tk.END,f"{row[0]}  - ₹{row[1]} {row[2]}")


root = tk.Tk()
root.title("FINANCE TRACKER APPLICATION")
root.geometry("400x400")

tk.Label(root, text="NAME OF EXPENSE").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="AMOUNT").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="CATEGORY").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="CREATE ENTRY", command=add_expenses).pack(pady=10)
tk.Button(root, text=" SHOW PREVIOUS DATA", command=previous_expense).pack(pady=10)

expense_list = tk.Listbox(root)
expense_list.pack(fill=tk.BOTH, expand=True)


root.mainloop()
