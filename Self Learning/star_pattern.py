
# nested loops = The inner loop will finish all
# of its iterations before finishing one iteration
# of the outer loop.

row = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(row):
    for j in range(columns):
        print(symbol, end=" ")
    print()