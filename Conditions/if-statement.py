number = int(input("Enter USSD Code"))

if number == 544:
    print("Welcome to safaricom Services")
    print("Chose one of the choices below")
    print("1;Data deals")
    print("2;Daily deals")
    print("3;Blaze offer")
    print("4;Data Bundles 'No expiry")
    print("5;Okoa Data")
    print("6;Storo data")
    print("7;Data Balance")

    number_2 = int(input("Select an option above"))
if number_2 == 1:
    print("Data deals")
elif number_2 == 2:
    print("Daily deals")
elif number_2 == 3:
    print("Blaze offer")
elif number_2 == 4:
    print("Data Bundles 'No expiry'")
elif number_2 == 5:
    print("Okoa Data")
elif number_2 == 6:
    print("Storo data")
elif number_2 == 7:
    print("Data Balance")
else:
     print("Invalid choice")
