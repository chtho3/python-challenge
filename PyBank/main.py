# Import Modules
import csv
import os
import numpy as np

# Open and Access CSV file
pybank_path = "Resources/budget_data.csv"

with open(pybank_path, newline="") as csvfile:
    pybank_csv = csv.reader(csvfile,delimiter=",")

    # Pop-off the header and save it

    pybank_header = next(pybank_csv)
  #  print(pybank_header)


# Count the total number of months in the dataset

    total_months = 0

    for line in pybank_csv:
        total_months = total_months + 1
   # print(str(total_months) + " months")

# Calculate the net total "Profit/Losses" over the dataset

# I was stuck on this for a while with my code trying to start
# where the total_months function left off, at the bottom of my
# dataset. I ended up re-reading the csv file to reset that,
# but I'm sure there's a much better way to do so.

with open(pybank_path, newline="") as csvfile:
    pybank_csv = csv.DictReader(csvfile,delimiter=',')
    total_profit = 0
    total_profit += sum([int(line['Profit/Losses']) for line in pybank_csv])
   # print(total_profit)
    # print(total_months) # double-check to make sure the variable still exists
    

# Calculate the mean Profit/Loss [diff btwn each month and avg those]
with open(pybank_path, newline="") as csvfile:
    pybank_csv = csv.DictReader(csvfile,delimiter=',')
    line_value = 0
    profit_list = []
    for line in pybank_csv:
         line_diff = int(line['Profit/Losses']) - line_value
         profit_list.append(line_diff)
         line_value = int(line['Profit/Losses'])
         #print(line_diff) #double-check
    profit_list.pop(0)
    avg_profit_long = np.mean(profit_list)
    avg_profit = np.round(avg_profit_long, 2)
    # print(profit_list) # double-check
   # print(np.round(avg_profit,2))


# Find the greatest increase in profits
    #print(np.max(profit_list))
    max_profit = np.max(profit_list)
    gain_index = profit_list.index(max_profit) + 1
    # print(gain_index) #double-check
with open(pybank_path, newline="") as csvfile:
    pybank_csv = csv.DictReader(csvfile,delimiter=',')
    for num, line in enumerate(pybank_csv):
        if num == gain_index:
            gain_month = line['Date']
    #print(gain_month)

# Find the greatest decrease in losses
   # print(np.min(profit_list))
    max_loss = np.min(profit_list)
    loss_index = profit_list.index(max_loss) + 1
with open(pybank_path, newline="") as csvfile:
    pybank_csv = csv.DictReader(csvfile,delimiter=',')
    for num, line in enumerate(pybank_csv):
        if num == loss_index:
            loss_month = line['Date']
    #print(loss_month)

# Final Financial Analysis Print-out
print('Financial Analysis')
print('-------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_profit))
print('Average Change: $' + str(avg_profit))
print(f'Greatest Increase in Profits: {gain_month} (${max_profit})')
print(f'Greatest Decrease in Profits: {loss_month} (${max_loss})')

# Export a text file of that Print-out
with open("output.txt", "w") as text_file:
    text_file.write('Financial Analysis \n')
    text_file.write('------------------------- \n')
    text_file.write('Total Months: ' + str(total_months) + '\n')
    text_file.write('Total: $' + str(total_profit) + '\n')
    text_file.write('Average Change: $' + str(avg_profit) + '\n')
    text_file.write(f'Greatest Increase in Profits: {gain_month} (${max_profit}) \n')
    text_file.write(f'Greatest Decrease in Profits: {loss_month} (${max_loss}) \n')