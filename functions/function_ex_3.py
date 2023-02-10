try:
    def agecalc():
        Age_years = int(input("Enter your age in years"))
        month = Age_years * 12
        print(f"You have lived for {month} months")


    agecalc()
except:
    print("not a number")
