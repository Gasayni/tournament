num = int(input("Enter a number: "))

if num < 3:
    print('The number is less than 3')
elif num >= 3 and num < 6:
    print('The number is greater than or equal to 3 and less than 6')
elif 6 <= num < 12:
    print('The number is greater than or equal to 6 and less than 12')
else:
    print('The number is greater than 12')
    