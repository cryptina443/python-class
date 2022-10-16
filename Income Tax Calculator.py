
tax_flat_rate=0.20
stnd_deduct=10000


gross_income=float(input('Enter your gross income to the nearest penny: '))
num_dep=int(input('Enter the number of dependents: '))

dep_deduct= num_dep * 3000

income_tax = (gross_income - stnd_deduct - dep_deduct) * tax_flat_rate 

print(f'The income tax is ${income_tax}')