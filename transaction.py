import pandas as pd
import csv
from datetime import datetime

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
CSV.intialize_csv()
CSV.add_entry('20-07-2024',200.00,'Income','Salary')

