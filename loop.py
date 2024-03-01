#fruit = ["Apple", True, 23, 23.55]
#print(fruit)
#sequence = ['A', 'B', 'C', 'D']
#for item in sequence: 
   # print("How many seats?")
   # no_of_seats = int(input())
    #enter = int(input(item))
    #print(enter * no_of_seats)

# num = 100
# while num <= 200:
#     print(num) 
#     num += 2

# number = [5, 2, 2, False, 10, 5, 7]

# for happy in number:
#     print(happy * happy) NB: use "break" to stop while loop


# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("Done")

# secret_number = 9
# start_count = 0
# guess_limit = 4
# while start_count < guess_limit:
#     guess = int(input("Guess: "))
#     start_count += 1
#     if guess == secret_number:
#         print("You win!!!")
#         break
# else:
#     print("You Loose!!!")

# print("Pick an option: \n1. Start \n2. Stop \n3. Help")
# Option=str(input(">>")).lower()
# if Option==1 or Option=="start":
#     print("Car Started.....Ready to go!")
# elif Option==2 or Option=="stop":
#     print("Car Stopped")
# elif Option==3 or Option=="help":
#     print("Select from the following options: \n1. Start \n2. Stop")
#     again=str(input("Select an option: ")).lower()
#     if again=="start":
#         print("Car Started.....Ready to go!")
#     elif again=="stop":
#         print("Car Stopped")
#     else:
#         print("I don't understand that....")
# else:
    # print("I don't understand that......")

# or....
command=""
started=False
help=True
stop=True
print("Car Ready.....\n Type: \n1. start \n2. stop \n3. help")
while True:
    command=input(">").lower()
    if command=="help":
        help=True
        started=False
        stop=True
        print("Select from the following options:  Start or Stop")
    elif command=="start":
        if not stop:
            help=False
            started=True
            print("Car has already started!")
        else:
            started=False
            help=False
            stop=False
            print("Car Started....")
    elif command=="stop":
        if stop:
            help=False
            started=False
            print("Car has already stopped!")
        else:
            started=True
            help=False
            stop=False
            print("Car Stopped.")
    else:
        print("I don't  understand this command")
    
  




