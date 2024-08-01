from datetime import datetime

date_format="%d-%m-%Y"
CATEGORIES={"I":"Income","E":"Expense"}

def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        validdate=datetime.strptime(date_str,date_format)
        return validdate.strftime(date_format)
    except ValueError:
        print("ENTER VALIDE DATE (dd-mm-yyyy)")
        return get_date(prompt,allow_default)

def get_amount():
    try:
        amount=float(input("ENTER THE AMOUNT= "))
        if amount <=0:
            raise ValueError("THE AMOUNT CANT BE NON ZERO OR ZERO")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    try:
        category=input("ENTER Category like 'I' For Income ,'E' For Expense ")
        if category in CATEGORIES:
            return CATEGORIES[category]
        
        print("Enter valid category")
        return get_category()
    except:
        pass

def get_desc():
    return input("ENTER DESCRIPTION (optional) ")
