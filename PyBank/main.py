# Dependencies
import csv
import os

# Files to Load - Input File
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open and Read the csv
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

#Create Empty Lists to Contain CSV values
    month_count = []
    total_profit = []
    change_profit = []

#Read Through Values and Add Them to Lists
    for row in reader:
        month_count.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit) - 1):
        change_profit.append(total_profit[i+1] - total_profit[i])

#Calculating the Changes in Profit and Month Values
greatest_increase = max(change_profit)
greatest_decrease = min(change_profit)

month_greatest_increase = change_profit.index(max(change_profit)) + 1
month_greatest_decrease = change_profit.index(min(change_profit)) + 1

#Calculating the Average Changes
average_change = round(sum(change_profit)/len(change_profit),2)

#Print Results
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_count[month_greatest_increase]} (${((greatest_increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_greatest_decrease]} (${((greatest_decrease))})")

#Generate Text File and Output
budget_analysis = os.path.join("PyBank", "analysis", "budget_analysis.txt")

with open(budget_analysis, "w") as text_file:
    text_file.write("PyBank Financial Analysis:\n")
    text_file.write(f"Total Months: {len(month_count)}\n")
    text_file.write(f"Total: ${sum(total_profit)}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {month_count[month_greatest_increase]} (${((greatest_increase))})\n")
    text_file.write(f"Greatest Decrease in Profits: {month_count[month_greatest_decrease]} (${((greatest_decrease))})")