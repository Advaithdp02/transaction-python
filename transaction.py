import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_desc
import matplotlib.pyplot as plt

class CSV():
    csv_file="finance_data.csv"
    columns=["date","amount","category","description"]
    date_format="%d-%m-%Y"
    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)

        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.csv_file,index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.csv_file,'a',newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("ENTRY ADDED SUCCESSFULLY") 
    @classmethod
    def get_transaction(cls,start_date,end_date):
        df=pd.read_csv(cls.csv_file)
        df["date"]=pd.to_datetime(df["date"],format=CSV.date_format)
        start_date=datetime.strptime(start_date,CSV.date_format)
        end_date=datetime.strptime(end_date,CSV.date_format)

        mask=(df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df=df.loc[mask]

        if filtered_df.empty:
            print("No transaction Found in that date range\n")
        else:
            print(f"The transaction from date {datetime.strftime(start_date,CSV.date_format)} to{datetime.strftime(end_date,CSV.date_format)}")
            print(filtered_df.to_string(index=False,formatters={"date":lambda x:x.strftime(CSV.date_format)}))
            total_income=filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
            total_expense=filtered_df[filtered_df["category"]=="Expense"]["amount"].sum()
            print("\nSummary")
            print(f"total Income ${total_income:.2f}")
            print(f"total Expense ${total_expense:.2f}")
            print(f"Net Savings ${(total_income-total_expense):.2f}")
        return df
    



def add():
    CSV.intialize_csv()
    date=get_date("ENTER THE DATE (dd-mm-yy) or enter for today's date ",allow_default=True)
    amount=get_amount()
    category=get_category()
    desc=get_desc()
    CSV.add_entry(date,amount,category,desc)

def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n1.ADD A TRANSACTION\n2.View Transaction from a date range\n 3.exit \n".upper())
        ch=int(input("Enter your choice: "))
        if ch==1:
            add()
        elif ch==2:
            start_date=get_date("Enter the start date (dd-mm-yyyy): ")
            end_date=get_date("Enter the end date (dd-mm-yyyy): ")
            df=CSV.get_transaction(start_date,end_date)
            print(df)
            if (input("do you want to see the graph (y/n) ").lower()=="y"):
                plot_transactions(df)
            
        elif ch==3:
            print("Exiting...")
            exit()
        else:
            print("Invalid opttion")
    
if __name__=="__main__":
    main()