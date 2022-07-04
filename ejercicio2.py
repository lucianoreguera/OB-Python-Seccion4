initial_number = int(input("Introduce el número inicial: "))
end_number = int(input("Introduce el numero final: "))
odd_numbers = []

for i in range(initial_number, end_number + 1):
    if i % 2 != 0:
        odd_numbers.append(i)

print("Números impares entre " + str(initial_number) + " y " + str(end_number))
print(odd_numbers)