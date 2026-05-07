'''
Input is
totsal rent
total food ordered
electricity units spend
charge per unit
persons in flat
Output
total amt have to pay
'''

rent = int(input ('Enter flat rent :'))
food = int(input('Enter amout of food ordered = '))
electricity_spend = int(input('enter eletricity total = '))
charge_per_unit = int(input('Charge per unit ?? '))
persons = int(input('enter number of persons = '))

totl_e_bill = charge_per_unit * electricity_spend

output =(food + rent +totl_e_bill)// persons

print("rent need to pay each = ",output)
