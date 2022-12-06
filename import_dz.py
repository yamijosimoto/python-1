import csv
import json
from csv import DictReader

with open("users.json", "r") as j:
    users = json.loads(j.read())

with open("books.csv", newline="") as c:
    reader = DictReader(c)
    rows = list(reader)

with open("result.json", "w") as file:
    s = json.dumps(users, indent=4)
    v = json.dumps(rows, indent=4)
    file.write(s + v)

# import csv
#
# with open("books.csv", "r") as f:
#     reader = csv.reader(f)
#
#     with open("new.csv", "w") as f:
#         writer = csv.writer(f)
#
#         for line in reader:
#             writer.writerow(line)

# import json
#
# def write(data, "result.json"):
#     data = json.dumps(data)
#     data = json.loads(str(data))
#
#     with open("result.json", "w", encoding="utf-8") as file:
#         json.dump(data, file, indent = 4)
#
# data = {
#     "users": [1]
# }