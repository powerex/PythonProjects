from sample02.sample0201.script14 import Worker

sue = Worker('Sue Jones', 60000)
bob = Worker('Bob Smith', 50000)

print(bob.last_name())
print(sue.last_name())

sue.give_raise(.1)
print(sue.pay)

