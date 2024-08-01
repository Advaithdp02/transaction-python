import pandas as pd
import csv
from datetime import datetime

class CSV():
    csv_file="finance_data.csv"
    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
            
        except FileNotFoundError:
            df=pd.DataFrame(columns=["data","amount","catgory","description"])
            df.to_csv(cls.csv_file,index=False)
CSV.intialize_csv()

