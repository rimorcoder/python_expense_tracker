import os
import argparse
import pandas as pd
import datetime

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

    # # List command
    # add_parser = subparsers.add_parser('list', help='List expenses')

    # # Add command
    # add_parser = subparsers.add_parser('summary', help='Summary of expenses')
    # add_parser.add_argument('--description', "-d", type=str, help='The description of the expense.')


    # Parse the arguments
    args = parser.parse_args()

    # Argument call
    match args.command:
        case "add":
            add_expense(args)
        case "delete":
            delete_expense(args.id)
        case _:
            print("This option is not recognized.")

    

if __name__ == "__main__":
    main()