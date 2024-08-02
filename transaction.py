import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_desc

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


def main():
    while True:
        print("\n1.ADD A TRANSACTION\n2.View Transaction from a date range\n 3.exit \n".upper())
        ch=int(input("Enter your choice; "))
        if ch==1:
            add()
        elif ch==2:
            start_date=get_date("Enter the start date (dd-mm-yyyy)")
            end_date=get_date("Enter the end date (dd-mm-yyyy)")
            df=CSV.get_transaction(start_date,end_date)
        elif ch==3:
            print("Exiting...")
            exit()
        else:
            print("Invalid opttion")
    
if __name__=="__main__":
    main()