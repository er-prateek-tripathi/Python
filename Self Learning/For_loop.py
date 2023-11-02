# for loop : a statement that will execute its
# block of code until the provided number of
# iterations are met.
import time

# while loop = unlimited iterations
# for loop = limited iterations, until
# range is met

for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):
    # range (start, end, step)
    print(i)

for i in "Prateek and Pragya":
    print(i)

for seconds in range(10, 0, -1):  # countdown for 10 to 0
    print(seconds)
    time.sleep(1)  # 1 second of pause is taken
print("Happy Sunday")


