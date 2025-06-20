
# 💰 Expense Tracker (CLI)

A lightweight command-line expense tracker built with Python. Track your daily/monthly expenses, generate summaries, and manage your data using CSV file storage.

---

## 📌 Project Details

- **Project Type**: CLI Utility
- **Tech Stack**: Python, CSV, Colorama

---

## 🎯 Features

- Add, update, delete expenses
- View all expense entries
- Monthly summaries
- Color-coded output using `colorama`
- Error handling (invalid input, missing arguments)
- Clean CLI design

---

## 🖥️ Preview

![Preview](https://github.com/user-attachments/assets/80a15bcd-694c-4e02-9237-427b6397ad74)

---

## ✅ Requirements

- Python 3.x

### 🔧 Install Required Package:

```bash
pip install colorama
```

---

## 🚀 How to Use

Run all commands from your terminal or command prompt:

### 🟢 Add Expense:

```bash
python expense_tracker.py add "Tea" 15
```

### ✏️ Update Expense:

```bash
python expense_tracker.py update 2 "Coffee" 30     # updates both description and amount
python expense_tracker.py update 2 45              # updates only amount
```

### ❌ Delete Expense:

```bash
python expense_tracker.py delete 3
```

### 📄 List All Expenses:

```bash
python expense_tracker.py list
```

### 📆 Monthly Summary:

```bash
python expense_tracker.py summary 6     # For June
```

---

## 📋 Command Table

| Command                          | Description                             |
|----------------------------------|-----------------------------------------|
| `add "desc" amount`              | Adds a new expense                      |
| `update id "desc" amount`        | Updates description & amount            |
| `update id amount`               | Updates only amount                     |
| `delete id`                      | Deletes an expense                      |
| `list`                           | Lists all expenses                      |
| `summary [month]`                | Shows total spent in given month        |

---

## 🧾 Example Output:

```
ID  Date        Description   Amount
-----------------------------------------
1   2025-06-11  Tea           $15.00
2   2025-06-11  Snacks        $30.00
```

```bash
Total expenses for month 6: $45.00
```

---

## 📦 File Structure

```
expense_tracker/
├── expense_tracker.py
├── expense.csv
└── README.md
```

---

## 🧠 Concepts Practiced

- File I/O with CSV
- CLI command parsing with `sys.argv`
- Error handling and validation
- Color-coded output using `colorama`
- Monthly filtering using datetime

---

## ✨ Add-On Suggestions

- Add category field to expenses
- Generate pie/bar chart using matplotlib
- Export report to PDF
- Convert CLI to GUI with Tkinter

---

## 📃 License
This project is open-source and free to use for educational purposes.

---

## Made with ❤️ by Shakyasimha Das.
