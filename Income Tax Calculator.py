#initiating variables that will stay constant
tax_flat_rate=0.20
stnd_deduct=10000

#asking for input from the user
gross_income=float(input('Enter the gross income: '))
num_dep=int(input('Enter the number of dependents: '))

#calculating the deduction based on dependents and storing it
dep_deduct= num_dep * 3000

#calculating income tax based on deductions and laws
income_tax = (gross_income - stnd_deduct - dep_deduct) * tax_flat_rate 

#displaying income tax
print(f'The income tax is ${income_tax}')
