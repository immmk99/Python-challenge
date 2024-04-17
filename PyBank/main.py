# Import dependencies
import csv
import os


# Read the data and create an object out of the CSV
budget_data = os.path.join("Resources", "budget_data.csv")


# Initialize variables
profit_loss = []
dates = []
change_profit_loss = []


month_count = 0
total_profit_loss = 0


# Read the CSV file
with open(budget_data, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    # Store the csv header
    csv_header = next(csv_reader)

    # Iterate through the csv rows
    for row in csv_reader:

        # Count the number of months
        month_count += 1

        # Store row values in lists
        dates.append(row[0])
        profit_loss.append(int(row[1]))

        # Calculate the total "Profit/Losses"
        total_profit_loss += int(row[1])


# Calculate the change in "Profit/Losses"
for x in range(month_count-1):
    change_profit_loss.append(profit_loss[x+1] - profit_loss[x])
        
# Calculate the average of the changes in "Profit/Losses"
average_changes_profit_loss = round(sum(change_profit_loss) / (month_count-1), 2)

# Find the amount and date of the greatest increase in profits
greatest_increase_profit_loss = max(change_profit_loss)
greatest_increase_date = dates[change_profit_loss.index(greatest_increase_profit_loss)+1]


# Find the amount and date of the greatest decrease in profits
greatest_decrease_profit_loss = min(change_profit_loss)
greatest_decrease_date = dates[change_profit_loss.index(greatest_decrease_profit_loss)+1]

# Output analysis
output_text = (
    f"\nFinancial Analysis\n"
    f"\n----------------------------\n"
    f"\nTotal Months: {month_count}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_changes_profit_loss}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profit_loss})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_profit_loss})\n"
    )

# Print analysis
print(output_text)


# Export text file with the analysis
results_txt = os.path.join("analysis", "results.txt")
with open (results_txt, "w") as txt_file:
    txt_file.write(output_text)



    
