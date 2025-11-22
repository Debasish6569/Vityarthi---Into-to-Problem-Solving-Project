# Expenditure Manager

## Subject: Introduction to Problem Solving (Project)

This console-based application is designed as a practical project to demonstrate fundamental programming concepts, including file handling, data structure manipulation (dictionaries and lists), and procedural logic for solving a common organizational problem: tracking personal expenditures.

### Programmer Details
* **Name:** Debasish Kumar Sahoo
* **Registration No:** 25BAI10173

---

## Project Overview and Core Functionality

The Expenditure Manager provides a robust, locally-stored solution for recording, viewing, summarizing, and managing financial transactions. Data persistence is managed entirely through a standard text file.

### Key Features

* **Add Expense:** Records transaction details, including amount, category, and description. The current date is automatically assigned.
* **View History:** Displays all recorded expenses in a clear, tabular format for easy review.
* **Delete Expense:** Allows removal of specific records based on their unique list ID.
* **Financial Summary:** Calculates and presents the **Grand Total** expenditure and a detailed **Category Breakdown** for financial analysis.
* **Persistent Storage:** Data is saved to `expenses.txt`, ensuring records remain between sessions.

---

## Technical Implementation Details

### Prerequisites

The application requires **Python 3.x** to run. No external libraries are necessary as it uses standard built-in modules (`os`, `datetime`).

### Installation and Execution

1.  **Save the Code:** Ensure the provided Python source code is saved as `expenditure_manager.py`.
2.  **Run the Script:** Execute the file from the command line interface:

    ```bash
    python expenditure_manager.py
    ```

### Data Handling

The system employs a **text-based database** approach using the `expenses.txt` file.

* **Structure:** Each expense record is stored as a single line in the file.
* **Delimiter:** The pipe character (`|`) is used to separate fields:
    `Date|Category|Amount|Description`
* **Functions:**
    * `get_all_expenses()`: Reads the file and converts each line into a list of Python dictionaries for in-memory processing.
    * `save_expenses_to_file()`: Overwrites the file with the current state of the in-memory expense list (used primarily after a record deletion).
