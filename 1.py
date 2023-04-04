month=int(input('Enter the month in the numeric form:'))
if month>12 and month<1:
    print('Error: Invalid Month Input')
day=int(input('Enter the day in numeric form:'))
if day>32 and day<1:
    print('Error: Invalid Day Input')
year=int(input('Enter the year as two numerical digits:'))
if year>100 and year<1:
    print('Error: Invalid Year Input')


print('Success: Congratulations! you entered the correct date.')
print('The Date is',month,'/',day,'/',year)