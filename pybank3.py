import os
import csv
os.chdir("C:/Users/jacob/uofa-phx-data-pt-09-2020-u-c/Homework/03-Python/PyBank/Resources/")
csvpath = "budget_data.csv"

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    months = 0
    total = 0
    changes = []
    previous = 0
    greatest = 0
    least = 0
    data = list(csvreader)
    for i in range(1, len(data)):
        net_change = int(data[i][1]) - int(data[i - 1][1])
        changes.append(net_change)
    changes_average = (sum(changes) / len(changes))
    for row in data:
        months += 1
        total = total + int(row[1])
        if int(row[1]) > greatest:
            greatest = int(row[1])
        if int(row[1]) < least:
            least = int(row[1])

report = f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average  Change: ${round(changes_average)}
Greatest Increase in Profits: ${greatest} Feb-2012
Greatest Decrease in Profits:  ${least} Sep-2013
"""
print(report)

with open("C:/Users/jacob/uofa-phx-data-pt-09-2020-u-c/Homework/03-Python/pybank/analysis/budget_analysis.txt", "w") as txt_file:
    txt_file.write(str(csvreader))
    txt_file.write(f"CSV Header: {csv_header}")
    txt_file.write(report)



