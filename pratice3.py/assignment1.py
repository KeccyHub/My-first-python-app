print("WELCOME TO OUR BUS TERMINAL.")
print("Hope your day has been lovely. Yes: lovely(😁), no: bad(😡), and meh: not quite lovely(😕)")
reply = str(input(" ")).lower()
if reply == "yes":
    print("Awesome!")
elif reply == "no":
    print("Don't worry, we've got you covered in this blissful ride")
else:
    print("You're about to take the ride of your life!")
print('''The following are our bus stops. 
Notice: we do not stop anywhere else that is not designated in the options below''')
print("1. Iyana Ipaja - 500\n2. Isheri Christ Embassy - 700\n3. Igando Phase 2 - 900\n4. First Gate - 300\n5. Ikotun - 800\nPick your Option")
stops={"Iyana Ipaja":500, "Isheri Christ Embassy":700, "Igando Phase 2":900, "First Gate":300} 
stops["Ikotun"]=800
stop_reply = str(input(">> ")).lower()
if stop_reply == "Iyana Ipaja" or 1:
    no_of_seats = int(input("Number of seats: "))
    totl = no_of_seats * stops["Iyana Ipaja"]
    print(totl)
elif stop_reply == "Isheri_christ_embassy" or 2:
    no_of_seats = int(input("Number of seats: "))
    total = no_of_seats * stops["Isheri_christ_embassy"]
    print(total)
elif stop_reply == "Igando_phase_2" or 3:
    no_of_seats = int(input("Number of seats: "))
    ttal = no_of_seats * stops["Igando_phase_2"]
    print(ttal)
elif stop_reply == "first gate" or 4:
    no_of_seats = int(input("Number of seats: "))
    totalp = no_of_seats * stops["First_gate"]
    print(totalp)
elif stop_reply=="Ikotun" or 5:
    no_of_seats = int(input("Number of seats: "))
    tt = no_of_seats * stops["Ikotun"]
else:
    print("Inavlid Response")
print("How would you like to pay?")
print("a. Cash")
print("b. Bank transfer")
response = str(input("")).lower()
if response == "a" or "cash":
    print("Do you have the exact amount? NOTE: We do not have petty cash ")
    print("Choose yes or no")
    choose = str(input(" ")).lower()
    if choose == "yes":
        print("You may proceed")
        print("✔")
    elif choose == "no":
        print("Choose another payment option")
        print("proceed with bank transfer? Yes or no")
        again = str(input(" "))
        if again == "yes": 
            print("Proceed with payment")
        elif again == "no":
            print("HAVE A WONDERFUL DAY, COME AGAIN NEXT TIME.")
        else:
            print("Invalid Option")
    else:
        print("Invalid Option❌")
elif response == "b" or "Bank transfer":
    print("You may Proceed")
    print("✔")
else:
    print("Invalid Option❌")

print("HAVE A WONDERFUL RIDE")

print("KECCY'S TRANSIT, THE CHOICE YOU'LL NEVER REGRET🎇🎇")
