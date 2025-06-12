import sys,os, csv,json
import datetime
from colorama import init, Fore, Style

init()

arguments = sys.argv
if len(arguments) == 1:
    print(f"""{Fore.YELLOW}Welcome to Expense Tracker CLI 🧾{Style.RESET_ALL}
Usage:
  python expense_tracker.py <command> [arguments]

Available Commands:
  add "description" amount
  update id "description" amount
  delete id
  list
  summary [month_number]

Examples:
  python expense_tracker.py add "Tea" 15
  python expense_tracker.py update 2 "Bus Ticket" 40
  python expense_tracker.py delete 3
  python expense_tracker.py summary 6
""")
    sys.exit()

def get_next_id():
    try:
        with open("expense.csv",'r') as file:
            reader_obj = csv.reader(file)
            next(reader_obj)
            reader_list = list(reader_obj)
            if len(reader_list) <= 0:
                return 1
            else:
                id = int(reader_list[-1][0]) + 1
                return id
    except FileNotFoundError:
        return 1
    except (ValueError, IndexError):
        return 1


def add(description,amount):
    if not description:
        return f"{Fore.RED}Description cannot be empty{Style.RESET_ALL}"
    
    if type(amount) == str:
        amount = float(amount)
    if amount <= 0:
        return f"{Fore.RED}Enter a valid amount{Style.RESET_ALL}"
    
    if not os.path.exists("expense.csv"):   
        with open("expense.csv",'w', newline='') as file:
            writer_obj = csv.writer(file)
            writer_obj.writerow(['id','date','description','amount'])

    id = get_next_id()
    date = datetime.datetime.now().date()
    return add_expense(id,date,description,amount)


def add_expense(id,date,description,amount):
    with open("expense.csv",'a', newline='') as file:
        writer_obj = csv.writer(file)
        writer_obj.writerow([id,date,description,amount])
    return f"{Fore.GREEN}Expense added successfully{Style.RESET_ALL}"

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def update(id, description=None,amount=None):
    if is_number(description):
        description = float(description)
    try:
        rows = []
        if isinstance(description,(int,float)) and amount == None:
            amount = description
            description = None
            
        with open("expense.csv",'r') as file:
            reader_obj = csv.reader(file)
            header = next(reader_obj)
            rows = list(reader_obj)

            found = False
            for row in rows:
                if int(row[0]) == int(id):
                    found = True
                    if description:
                        row[2] = description
                    if amount:
                        row[3] = float(amount)
            
            if not found:
                return f"{Fore.RED}ID not found{Style.RESET_ALL}"

        with open("expense.csv",'w', newline='') as file:
            writer_obj = csv.writer(file)
            writer_obj.writerow(header)
            writer_obj.writerows(rows)

        return f"{Fore.GREEN}Update Successful{Style.RESET_ALL}"

    except FileNotFoundError:
        return f"{Fore.RED}File not found{Style.RESET_ALL}"
    except ValueError:
        return f"{Fore.RED}Invalid ID or amount{Style.RESET_ALL}"
    
def delete(id):
    found = False
    with open("expense.csv",'r') as file:
        read_obj = csv.reader(file)
        header = next(read_obj)
        rows = list(read_obj)
        for i in range(len(rows)):
            if rows[i][0] == id:
                print(rows[i][0])
                found = True
                rows.pop(i)
                for j in range(i,len(rows)):
                    rows[j][0] = str(int(rows[j][0]) - 1)
                break

    if not found:
        return f"{Fore.RED}ID not found{Style.RESET_ALL}"    
    
    with open("expense.csv",'w', newline='') as file:
        writer_obj = csv.writer(file)
        writer_obj.writerow(header)
        writer_obj.writerows(rows)

    return f"{Fore.GREEN}Deleted successfully{Style.RESET_ALL}"

def summary(month=None):
    try:
        total_expense = 0
        month_found = False

        # Month validation (only if month is provided)
        if month is not None:
            month = int(month)
            if month > 12 or month == 0:
                return f"{Fore.RED}Invalid month number{Style.RESET_ALL}"
            # Zero-pad month to match CSV format
            month = f"{month:02d}"

        with open("expense.csv", "r") as file:
            reader_obj = csv.reader(file)
            next(reader_obj)
            rows = list(reader_obj)

            if not month:
                # Calculate total for all months
                for row in rows:
                    total_expense += float(row[3])
                return f"Total expenses: {Fore.YELLOW}${total_expense:.2f}{Style.RESET_ALL}"
            else:
                # Calculate total for specific month
                for row in rows:
                    date = row[1].split('-')
                    month_no = date[1]
                    if month_no == month:
                        month_found = True
                        total_expense += float(row[3])
                
                if not month_found:
                    return f"{Fore.RED}No expenses found for month {month}{Style.RESET_ALL}"
                return f"Total expenses for month {month}: {Fore.YELLOW}${total_expense:.2f}{Style.RESET_ALL}"

    except FileNotFoundError:
        return f"{Fore.RED}File not found{Style.RESET_ALL}"
    except ValueError:
        return f"{Fore.RED}Invalid month format{Style.RESET_ALL}"
    except IndexError:
        return f"{Fore.RED}Invalid date format in file{Style.RESET_ALL}"

def list_expenses():
    try:
        with open("expense.csv", 'r') as file:
            read_obj = csv.reader(file)
            header = next(read_obj)
            rows = list(read_obj)

            if not rows:
                return f"{Fore.YELLOW}No expenses recorded yet{Style.RESET_ALL}"
            
            # Print header with formatting
            print(f"\n{Fore.CYAN}ID  Date        Description  Amount{Style.RESET_ALL}")
            print("-" * 40)  # Separator line
            
            # Print each row with formatting
            for row in rows:
                print(f"{Fore.GREEN}{row[0]:<4}{Style.RESET_ALL}{row[1]:<12}{row[2]:<12}{Fore.YELLOW}${float(row[3]):.2f}{Style.RESET_ALL}")

    except FileNotFoundError:
        return f"{Fore.RED}File not found{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}"

    

commands = {
    "add":add,
    "update":update,
    "delete":delete,
    "summary":summary,
    "list":list_expenses
}

try:
    if len(arguments) == 6:
        response = commands[arguments[1]](arguments[2], arguments[3], arguments[4], arguments[5])
    elif len(arguments) == 5:
        response = commands[arguments[1]](arguments[2], arguments[3], arguments[4])
    elif len(arguments) == 4:
        response = commands[arguments[1]](arguments[2], arguments[3])
    elif len(arguments) == 3:
        response = commands[arguments[1]](arguments[2])
    elif len(arguments) == 2:
        response = commands[arguments[1]]()
    else:
        response = f"{Fore.RED}Invalid number of arguments{Style.RESET_ALL}"

    if response:
        print(response)

except TypeError as te:
    print(f"{Fore.RED}Error: {te}{Style.RESET_ALL}")
except KeyError:
    print(f"{Fore.RED}Invalid command. Use add, update, delete, list, summary{Style.RESET_ALL}")
except Exception as e:
    print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")