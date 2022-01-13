#Q01
#total zero
print('**r**WELCOME****')
while True:
    starting_number = 0
    enter_number = int(input("Enter the ending number:\n"))
    while starting_number <= enter_number:
        for num in range(starting_number,enter_number + 1,+1):
            print(num)
            if num == enter_number:
                print("Goodbye!")
        break
    repeat_count = input("Would you like to start over? Enter Y to start over or N to exit: ")
    if repeat_count.upper() != 'Y':
        print("Goodbye!")
        break
print()




