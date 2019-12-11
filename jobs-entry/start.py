import datetime
from db_functions import *


def read_data():
    print("read_data")
    res = read_entries()


def update_data():
    print("update_data")
    result = read_entries()
    update_entry = int(input("Enter ID for updating row. "))
    # print(result, update_entry)
    quote = """1. Company_name"   2. "Followup_date"   3. "Role"   4. "Language   5. Comment.
    select option to update content. """
    input(quote)


def delete_entry():
    print("delete_entry")


def followup_data():
    print("followup_data")


def add_data():
    print("\n Please mention following data: ")
    company_name = input("Company Name: ")
    applied_date = input("If applied today leave it blank, else mention Date (YYYY-MM-DD)")
    if applied_date == "":
        applied_date = str(datetime.date.today())
    # print(applied_date)
    followup_date = input("mention the date for follow up (YYYY-MM-DD)")
    role = input("Mention role name")
    languages = input("Mention if any specific languages in job")

    try:
        date_apply = datetime.datetime.strptime(applied_date, '%Y-%m-%d')
        date_followup = datetime.datetime.strptime(followup_date, '%Y-%m-%d')
        if date_apply and date_followup:
            print("its fine", date_apply, date_followup)
    except ValueError:
        print("Please enter a proper date")

    add_entry(company_name, date_apply, date_followup, role, languages)


def start_message(flag=0):
    if flag == 0:
        followup_data()
    message = """Hello Jonny! what you want to do?
    1. Add new entry
    2. List Table
    3. Update existing entry
    4. Delete entry
    5. Exit"""
    print(message)
    selection = input("Select Option: ")
    if int(selection) == 5:
        exit(0)
    elif int(selection) == 1:
        add_data()
    elif int(selection) == 2:
        read_data()
    elif int(selection) == 3:
        update_data()
    elif int(selection) == 4:
        delete_entry()
    start_message(1)


if __name__ == "__main__":
    start_message()
