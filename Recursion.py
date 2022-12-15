def is_power_of_two(number):
    print(('NO', 'YES')[bin(number)[2:].count('1') == 1])


number_input = int(input("Enter a number: "))
is_power_of_two(number_input)
