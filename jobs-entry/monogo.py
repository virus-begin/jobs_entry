from pymongo import MongoClient
from tabulate import tabulate

client = MongoClient('localhost', 27017)
db_name = client.jobs_list
lists = db_name.job_entries
job_details = {
    "company_name": "Acounts Pvt limted",
    "applied_date": "2019-01-12",
    "followup_date": "2019-05-12",
    "role": "Accountant",
    "comment": "applied",
    "languages": "Excel"
}

# resp = lists.insert_one(job_details)
# print(resp)
# if resp.acknowledged:
#     print("Added Job Entry",resp.inserted_id)

print(tabulate([['Joy', 21], ['Sam', 23]], headers=['name', 'age']))
row_arr = []
fetch_data = lists.find()
for x in fetch_data:
    print(x)
    rows = [x["company_name"], x["applied_date"], x["followup_date"], x["role"], x["languages"]]
    # rows = []
    # rows.append(x["company_name"])
    # rows.append(x["applied_date"])
    # rows.append(x["followup_date"])
    # rows.append(x["role"])
    # rows.append(x["languages"])
    row_arr.append(rows)

col_headers = ["ID", "Company", "Applied_date", "Followup_date", "Role", "Language"]
print(tabulate(row_arr, col_headers, tablefmt="grid"))
