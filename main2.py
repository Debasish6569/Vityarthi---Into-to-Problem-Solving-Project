import os
from datetime import date

FILE_NAME = "expenses.txt"

def save_expenses_to_file(expenses):
    """Helper function: Overwrites the file with the current list of expenses."""
    try:
        with open(FILE_NAME, "w") as file:
            for item in expenses:
                # Reconstruct the line: Date|Category|Amount|Description
                line = f"{item['date']}|{item['category']}|{item['amount']}|{item['description']}\n"
                file.write(line)
    except IOError as e:
        print(f"Error saving data: {e}")

def get_all_expenses():
    """Reads the file and returns a list of dictionaries."""
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 4:
                expenses.append({
                    "date": parts[0],
                    "category": parts[1],
                    "amount": float(parts[2]),
                    "description": parts[3]
                })
    return expenses

def add_expense():
    """Appends a new expense to the file."""
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
        
        category = input("Enter Category: ").strip().capitalize()
        description = input("Description: ").strip().replace("|", "-")
        today = date.today().strftime("%Y-%m-%d")

        # Append directly to file
        entry = f"{today}|{category}|{amount}|{description}\n"
        with open(FILE_NAME, "a") as file:
            file.write(entry)
        
        print("✅ Expense saved!")

    except ValueError:
        print("❌ Error: Please enter a valid number.")

def view_expenses():
    """Displays expenses in a table."""
    expenses = get_all_expenses()
    print("\n--- Your Expenditure History ---")
    if not expenses:
        print("No records found.")
        return

    print(f"{'ID':<4} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 70)

    # enumerate gives us an index (i) starting from 0, we add 1 for the display ID
    for i, item in enumerate(expenses):
        print(f"{i+1:<4} | {item['date']:<12} | {item['category']:<15} | ${item['amount']:<9.2f} | {item['description']}")
    print("-" * 70)

def delete_expense():
    """Lists expenses and asks user which ID to delete."""
    print("\n--- Delete an Expense ---")
    expenses = get_all_expenses()
    
    if not expenses:
        print("No expenses to delete.")
        return

    # Show the list first so user knows the ID
    view_expenses()

    try:
        choice = int(input("\nEnter the ID of the expense to delete: "))
        
        # Check if the choice is valid (between 1 and the length of the list)
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1) # Remove item from list
            save_expenses_to_file(expenses)    # Rewrite the file
            print(f"✅ Deleted: {removed['description']} (${removed['amount']})")
        else:
            print("❌ Invalid ID. Please check the list and try again.")
            
    except ValueError:
        print("❌ Please enter a valid integer ID.")

def show_summary():
    """Calculates and displays totals."""
    expenses = get_all_expenses()
    if not expenses:
        print("\nNo data to summarize.")
        return

    total_spent = sum(item['amount'] for item in expenses)
    
    category_totals = {}
    for item in expenses:
        cat = item['category']
        category_totals[cat] = category_totals.get(cat, 0) + item['amount']

    print("\n--- Financial Summary ---")
    print(f"💰 Grand Total: ${total_spent:.2f}")
    print("\n--- Breakdown by Category ---")
    for cat, amount in category_totals.items():
        print(f"{cat:<15}: ${amount:.2f}")

def main():
    while True:
        print("\n=== EXPENDITURE MANAGER ===")
        print("1. Add Expense")
        print("2. View History")
        print("3. Delete Expense")  # <-- New Option
        print("4. Show Summary")
        print("5. Exit")
        
        choice = input("Choose (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
