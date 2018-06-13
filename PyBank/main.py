#Import OS and CSV modules and specify filepath and filename
import os
import csv

csvpath = os.path.join('C:\\','Users','Nii','Homework','PyBank','raw_data','budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    header = next(csvreader) #Skips the first row
    data_list = list(csvreader)
    
    # Create lists to store data in rows
    dates = []
    revenue = []
    revenue_change = []

    
    # Loop through every row
    for row in data_list:
        dates.append(row[0])
        revenue.append(int(row[1]))

        total_months = len(dates)
        total_revenue = sum(revenue)

    for i in range (len(revenue)-1):
        revenue_change.append(revenue[i+1] - revenue[i])
        average_rev_change = round(sum(revenue_change)/len(revenue_change))
        greatest_rev_increase = max(revenue_change)
        greatest_rev_decrease = min(revenue_change)
        greatest_inc_date = str(dates[revenue_change.index(max(revenue_change))+1])
        greatest_dec_date = str(dates[revenue_change.index(min(revenue_change))+1])


    print("Financial Analysis")
    print("........................")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}") 
    print(f"Average Revenue Change: $ {average_rev_change}") 
    print(f"The Greatest Increase in Revenue: {greatest_inc_date} (${greatest_rev_increase})")
    print(f"The Greatest Decrease in Revenue: {greatest_dec_date} (${greatest_rev_decrease})")
    print(".......")

output_path = os.path.join('C:\\','Users','Nii','Homework','PyBank','financial_analysis.txt') 
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis" + "\n")
    output_file.write("-------------------------" + "\n")
    output_file.write("Total Months: " + str(total_months) + "\n")
    output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
    output_file.write("Average Revenue Change: $" + str(average_rev_change) + "\n")
    output_file.write("The Greatest Increase in Revenue: " + str(greatest_inc_date) + " $(" + str(greatest_rev_increase) + ")" + "\n")
    output_file.write("The Greatest Decrease in Revenue: " + str(greatest_dec_date) + " $(" + str(greatest_rev_decrease) + ")" + "\n")
    
    output_file.close


    




        