#Average salraies
canada_average= 64000
us_average= 56516
uk_average= 35423
cambodia_average= 5649856

#function for conversion
def convertSalary(salary, country):
    if country == 'canada':
        converted_salary = salary * 1.55029411765
    elif country == 'usa':
        converted_salary = salary * 1.18
    elif country == 'uk':
        converted_salary = salary * 0.91
    elif country == 'cambodia':
        converted_salary = salary * 4847.38
    else:
        return 'Invalid country'

    return round(converted_salary, 2)

salary = int(input('Enter your salary in Euros per annum: '))
country = input('Enter the country you want to migrate to: ')

converted_salary = convertSalary(salary, country)

#function for comparison
def status(country,converted_salary):
    if country=='canada':
        if int(converted_salary) > canada_average:
            print ('You are rich in canada with annual income of', converted_salary)
        elif int(converted_salary) < canada_average:
            print ('You are poor in canada with annual income of', converted_salary)
    if country=='usa':
        if int(converted_salary) > us_average:
            print ('You are rich in USA with annual income of', converted_salary)
        elif int(converted_salary) < us_average:
            print ('You are poor in USA with annual income of', converted_salary)
    if country=='uk':
        if int(converted_salary) > uk_average:
            print ('You are rich in UK with annual income of', converted_salary)
        elif int(converted_salary) < uk_average:
            print ('You are poor in UK with annual income of', converted_salary)
    if country=='cambodia':
        if int(converted_salary) > cambodia_average:
            print ('You are rich in Cambodia with annual income of', converted_salary)
        elif int(converted_salary) < cambodia_average:
            print ('You are poor in Cambodia with annual income of', converted_salary)

status(country, converted_salary)
        
    
