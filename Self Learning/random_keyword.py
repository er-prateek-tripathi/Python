import random

# prints any random number between the given range
x = random.randint(1, 6)
print(x)

# prints any random decimal value
y = random.random()
print(y)

# rock paper scissor game
myList = ['rock', 'paper', 'scissor']
z = random.choice(myList)
print(z)

# shuffling numbers
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"]
random.shuffle(cards)
print(cards)