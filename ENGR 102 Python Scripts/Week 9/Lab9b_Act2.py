# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 9b Activity 2
# Date:         10/23/2020
#

print('This program will save to a file a list of amortized values for a loan')

# Get name for file
file_name = str(input('Please enter the name of the file that will contain the loan\
                  data: '))

# open named file
loan_data = open(file_name + '.csv', 'w')

# get the amount of the loan ,the number of months over which the load 
# will be repaid, and the annual interest rate (i).
loan_amount = float(input('Please enter the amount of the loan here: '))
Num_months = int(input('Please enter the number of months the loan will be \
                          repaid here: '))
interest_rate = float(input('Please enter the annual interest of the loan as a\
                            decimal here: '))
J = interest_rate/12
# loan_amount = 100000
# Num_months = 60
# interest_rate = 0.025

# find the monthly payment(M)
month_payment = loan_amount * (J/(1-(1 + J)**(-Num_months)))

# loop to find the accured interest and ending balance for each month
begin_balance = loan_amount
acc_interest = 0
begin_balance_list = []
month_interest_list = []
acc_interest_list = []
end_balance_list = []
month_list = []

for month in range(0, Num_months + 1):
    if month == 0:
        month_interest = 0
        end_balance = begin_balance
        begin_balance = 0
    else: 
        month_interest = begin_balance * J
        end_balance = (begin_balance - month_payment) + month_interest
    begin_balance_list.append(begin_balance)
    begin_balance = end_balance
    acc_interest += month_interest
    month_interest_list.append(month_interest)
    acc_interest_list.append(acc_interest)
    end_balance_list.append(end_balance)
    month_list.append(month)

# Create table for the file
header_row = 'Month, Beginning Balance, Monthly Interest, Accured Interest, Final Balance'
header_row = header_row.split(', ')
header_format = '{:^5},{:^15},{:^15},{:^15},{:^15}\n'
header = header_format.format(header_row[0], header_row[1], header_row[2], \
                        header_row[3], header_row[4])
loan_data.write(header)

# Use table to format data
my_format = '{:<5},${:>15.2f},${:>15.2f},${:>15.2f},${:>15.2f}\n'
for i in range(0, Num_months + 1):
    loan_data.write(my_format.format(month_list[i], begin_balance_list[i], month_interest_list[i], \
                                         acc_interest_list[i], \
                                             end_balance_list[i]))

# close file
loan_data.close()
