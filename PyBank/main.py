import os
import csv

PyBank_csv=os.path.join("Resources","budget_data.csv")

dates=[]
net_profit=0.0
changes=[]
prev_profit=0.0
max_change = 0.0
min_change = 0.0

with open(PyBank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:
        dates.append(row[0])
        net_profit += float(row[1])

        profit = float(row[1])
        change = profit - prev_profit

        changes.append(profit-prev_profit)
        if max_change < profit-prev_profit:
           max_change=profit-prev_profit
           max_date=row[0]

        if min_change > profit-prev_profit:
           min_change=profit-prev_profit
           min_date=row[0]


        prev_profit = float(row[1])

total_months=len(dates)


print(str(total_months))
print(net_profit)
avg_change = sum(changes[1:]) / len(changes[1:])
print(round(avg_change, 2))
print(max_date,max_change)
print(min_date,min_change)
   
output_file=os.path.join("analysis","analysis.txt")
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write("Total Months: " + str(total_months) + "\n")
    datafile.write("Total: " + "$"+str(net_profit) + "\n") 
    datafile.write("Average Change: " +"$"+str(round(avg_change,2)) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(max_date)+" $"+str(max_change) + "\n")
    datafile.write("Greatest Decrease om Profits: " + str(min_date)+" $"+str(min_change) + "\n")   