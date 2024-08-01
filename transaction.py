import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_desc

class CSV():
    csv_file="finance_data.csv"
    columns=["date","amount","category","description"]
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

def add():
    CSV.intialize_csv()
    date=get_date("ENTER THE DATE (dd-mm-yy) or enter for today's date ",allow_default=True)
    amount=get_amount()
    category=get_category()
    desc=get_desc()
    CSV.add_entry(date,amount,category,desc)

add()