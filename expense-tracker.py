import os
import argparse
import pandas as pd
import datetime
import calendar

CSV_FILE = "expenses.csv"

def create_csv_if_not_exists():
    csv_file = CSV_FILE
    if not os.path.exists(csv_file):
        headers = ['id', 'when', 'category', 'description', 'amount']
        df = pd.DataFrame(columns=headers)
        df.to_csv(csv_file, index=False)

def add_expense(args):
    csv_file = CSV_FILE
    today = datetime.date.today()
    
    # read csv
    df = pd.read_csv(csv_file)

    # add new data
    new_data = pd.DataFrame({
        'id': [len(df) + 1],
        'when': [today.strftime("%Y-%m-%d")],
        'category': [args.category],
        'description': [args.description],
        'amount': [args.amount]        
    })
    df = pd.concat([df, new_data], ignore_index=True)

    # write to csv
    df.to_csv(csv_file, index=False)

    # print
    print(f"Expense added successfully ( ID: {new_data.iloc[0]['id']} )")

def delete_expense(id):
    csv_file = CSV_FILE     

    # read csv
    df = pd.read_csv(csv_file)

    # get index
    try:
        index_value = df[df['id'] == id].index.values[0]
    except IndexError:
        print("ID not found")
        return
    
    # delete row
    df = df.drop(index_value)
    
    # write to csv
    df.to_csv(csv_file, index=False)

    # print
    print("Expense deleted")

def list_expense():
    csv_file = CSV_FILE     

    # read csv
    df = pd.read_csv(csv_file)
    
    # set display options to show all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
    # print all contents of the dataframe
    print(df)

def sum_expense():
    csv_file = CSV_FILE     

    # read csv
    df = pd.read_csv(csv_file)
    
    # calculate the sum of the 'amount' column
    total_amount = df['amount'].sum()
    
    # print the total amount
    print(f"Total amount of expenses: ${total_amount:.2f}")

def sum_expense_for_month(month):
    csv_file = CSV_FILE     

    # read csv
    df = pd.read_csv(csv_file)
    
    # convert 'when' column to datetime
    df['when'] = pd.to_datetime(df['when'])
    
    # filter by month
    df_filtered = df[df['when'].dt.month == month]
    
    # calculate the sum of the 'amount' column for the filtered month
    total_amount = df_filtered['amount'].sum()
    
    import os
import argparse
import pandas as pd
import datetime
import calendar

CSV_FILE = "expenses.csv"

def sum_expense_for_month(month):
    csv_file = CSV_FILE     

    # read csv
    df = pd.read_csv(csv_file)
    
    # convert 'when' column to datetime
    df['when'] = pd.to_datetime(df['when'])
    
    # filter by month
    df_filtered = df[df['when'].dt.month == month]
    
    # calculate the sum of the 'amount' column for the filtered month
    total_amount = df_filtered['amount'].sum()
    
    # convert month number to month name
    month_name = calendar.month_name[month]
    
    # print the total amount for the month
    print(f"Total amount of expenses for {month_name}: ${total_amount:.2f}")

def main():   
    # creates csv if not exist
    create_csv_if_not_exists()

    # Initialize the parser
    parser = argparse.ArgumentParser(description="A script to manage expenses")
    
    # Add commands (subparsers for each action)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', "-d", type=str, help='The description of the expense.')
    add_parser.add_argument('--amount', "-a", type=float, help=f'The amount, in dollars, of the expense.', default=0.0)
    add_parser.add_argument('--category', "-c", type=str, help=f'The catagory of the expense', default="general")

    # Delete command
    add_parser = subparsers.add_parser('delete', help='Delete expenses')
    add_parser.add_argument('id', type=int, help='The id of the expense.')

    # List command
    add_parser = subparsers.add_parser('list', help='List expenses')

    # Add command
    add_parser = subparsers.add_parser('sum', help='Summary of expenses')
    add_parser.add_argument('--month', "-m", type=int, help=f'Summary of expenses for a month. Use double digit months, i.e. 03 for March')

    # Parse the arguments
    args = parser.parse_args()

    # Argument call
    if args.command == "add":
        add_expense(args)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expense()
    elif args.command == "sum":
        if(args.month):
            sum_expense_for_month(args.month)
        else:
            sum_expense()
    else:
        print("This option is not recognized.")

    

if __name__ == "__main__":
    main()