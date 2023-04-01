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

a = [1,2,3]
b = ['a','b','c']
c = ['&', '%','#']

for n, l, s in zip(a,b,c):
    print(f"{n}-{l}-{s}")