# no s div by 3  = fizz
# no s div by 5 = bus
# if no s div by both 5 and 3 = fizzbus

for i in range(1,51):
    if i % 5 == 0 and i % 3 == 0:
        print("FIZZBUS")
    elif i % 5 == 0:
        print("BUS")
    elif i % 3 == 0:
        print("FIZZ")
    else:
        print(i)