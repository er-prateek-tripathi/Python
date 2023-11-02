# logical operators ( and, or, not) =
# used to check two or more conditional
# statements are true
# not will flip true to false and false to true

temp = int(input("What is the temperature outside?: "))

if 0 <= temp <= 30:  # temp >= 0 and temp <= 30
    print("Temperature is good today!!")
    print("You can go outside.")
elif temp < 0 or temp > 30:
    print("Temperature is bad today!!")
    print("Stay inside.")
