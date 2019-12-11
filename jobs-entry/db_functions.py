import pymongo
from pymongo import MongoClient
from tabulate import tabulate


# client, db_name, lists = ''
# rows_arr = []


def db_connection():
    # global client, db_name, lists
    client = MongoClient('localhost', 27017)
    db_name = client.jobs_list
    lists = db_name.job_entries


def add_entry(company_name, date_apply, date_followup, role, languages):
    client = MongoClient('localhost', 27017)
    db_name = client.jobs_list
    lists = db_name.job_entries
    job_details = {
        "company_name": company_name,
        "applied_date": date_apply,
        "followup_date": date_followup,
        "role": role,
        "comment": "applied job",
        "languages": languages
    }
    resp = lists.insert_one(job_details)
    # print(resp)
    if resp.acknowledged:
        print("Added Job Entry", resp.inserted_id)


def read_entries():
    rows_arr = []
    complete_data = []
    client = MongoClient('localhost', 27017)
    db_name = client.jobs_list
    lists = db_name.job_entries
    fetch_data = lists.find().sort("followup_date")
    for index, entry in enumerate(fetch_data):
        temp = []
        rows = []
        temp = [entry["company_name"], entry["applied_date"], entry["followup_date"], entry["role"],
                entry["languages"],entry["comment"],entry["_id"]]
        complete_data.append(temp)
        rows = [index, entry["company_name"], entry["applied_date"], entry["followup_date"], entry["role"],
                entry["languages"]]
        rows_arr.append(rows)
    col_headers = ["ID", "Company", "Applied_date", "Followup_date", "Role", "Language"]
    print(tabulate(rows_arr, col_headers, tablefmt="grid"))
    return complete_data


if __name__ == "__main__":
    db_connection()

# print(tabulate([['Joy', 21], ['Sam', 23]], headers=['name', 'age']))
# row_arr = []
# fetch_data = lists.find()
# for x in fetch_data:
#     print(x)
#     rows = [x["company_name"], x["applied_date"], x["followup_date"], x["role"], x["languages"]]
#     # rows = []
#     # rows.append(x["company_name"])
#     # rows.append(x["applied_date"])
#     # rows.append(x["followup_date"])
#     # rows.append(x["role"])
#     # rows.append(x["languages"])
#     row_arr.append(rows)

# col_headers = ["ID", "Company", "Applied_date", "Followup_date", "Role", "Language"]
# print(tabulate(row_arr, col_headers, tablefmt="grid"))
