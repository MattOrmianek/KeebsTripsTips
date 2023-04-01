# Unpacking

inputs = [
    'Agatha',
    'Marta',
    'Luis',
    'Pedro',
    29
]

first, last, *_, age = inputs
print(f"{first}, {last}, is {age}")

# List Comprehension
names = [
    'Bobby C. Brown',
    'Chris Stevens',
    'Jacob G. Smith',
    'John Paul Davis'
]

last_names = [name.split()[-1] for name in names]
print(f'last_names: {last_names}')

# Zip
a = [1,2,3]
b = ['a','b','c']
c = ['&', '%','#']

for n, l, s in zip(a,b,c):
    print(f"{n}-{l}-{s}")

# Map
citizens = [('Steve', 10), ('Mark', 8), ('Chris', 11)]

def tax(citizen):
    name = citizen
    tax = 0.2 * citizen[1]
    return (name, tax)

taxes = list(map(tax, citizens))
print(f"Taxes for citizens: {taxes}")

# Enumerate with start

people = ['Elon', 'Jeff', 'Mark', 'Tsao']

for i, name in enumerate(people, start = 1):
    #print(f"{i+1} - {name}") - changing i+1 to simple i starting on 1
    print(f"{i} - {name}")