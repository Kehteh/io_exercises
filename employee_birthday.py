import csv

with open("employee_birthday.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    #            ^^^^^^^^^^^^^^^^^^^^ Iterable
    next(csv_reader) # skip headers (first row)

    for row in csv_reader:       
        if row:
            employee_name = row[0]
            department_name = row[1]
            birthday_month = row[2]
            print(f"Name: {employee_name}")
            print(f"Department: {department_name}")
            print(f"Birth month: {birthday_month}")

with open("employee_birthday.csv") as csv_file:
    csv_dictreader = csv.DictReader(csv_file)
    for row in csv_dictreader:
        if row:
            print(f"Name: {row["name"]}")
            print(f"Department: {row["department"]}")
            print(f"Birth month: {row["birthday_month"]}")