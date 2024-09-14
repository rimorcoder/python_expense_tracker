# Expense Manager

https://roadmap.sh/projects/expense-tracker

This is a simple command-line tool to manage your expenses. It allows you to add, delete, list, and summarize expenses stored in a CSV file.

## Prerequisites

- Python 3.6 or higher
- `pandas` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:

    ```sh
    pip install pandas
    ```

## Usage

The script provides several commands to manage your expenses. Below are the available commands and their usage:

### Add a New Expense

To add a new expense, use the `add` command:

```sh
python expense_manager.py add --description "Lunch" --amount 15.50 --category "Food"
```

### Delete an Expense
To delete an expense by its ID, use the delete command:
```sh
python expense_manager.py delete 1
```
### List All Expenses
To list all expenses, use the list command:
```
python expense_manager.py list
```
### Summarize Expenses
To get a summary of all expenses, use the sum command:
```
python expense_manager.py sum
```
To get a summary of expenses for a specific month, use the sum command with the --month option:
```
python expense_manager.py sum --month 03
```
### Example
Here is an example of how to use the script:

#### Add a new expense:
```
python expense_manager.py add --description "Coffee" --amount 3.50 --category "Beverage"
```

#### List all expenses:
```
python expense_manager.py list
```

#### Delete an expense by ID:
```
python expense_manager.py delete 1
```

#### Get a summary of all expenses:
```
python expense_manager.py sum
```

#### Get a summary of expenses for March:
```
python expense_manager.py sum --month 03
```

### Notes
The expenses are stored in a CSV file named expenses.csv in the same directory as the script.
The script will create the CSV file if it does not exist.