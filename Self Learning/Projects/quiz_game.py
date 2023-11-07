def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Which option? (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!!!")
        return 1
    else:
        print("Wrong!!!")
        return 0


def display_score(correct_guesses, guesses):
    print("----------")
    print("Result: ")
    print("----------")
    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=", ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=", ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your Score is: " + str(score)+"%")


def play_again():
    response = input("Wanna play again? (y/n): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False


questions = {

    "Who created Python?: ": "A",
    "What year was python created?: ": "B",
    "Python was tribute to which comedy group?: ": "C",
    "Is the earth round?: ": "A",

    "What is the capital of France?: ": "A",
    "What is the largest planet in our solar system?: ": "B",
    "What is the chemical symbol for gold?: ": "A",
    "What is the name of the world's tallest mountain?: ": "A",
    "What is the most populous country in the world?: ": "E",

    "Who wrote the novel 'Pride and Prejudice'?: ": "A",
    "Who painted the Mona Lisa?: ": "A",
    "Who composed the opera 'Carmen'?: ": "C",
    "Who invented the lightbulb?: ": "D",
    "Who discovered penicillin?: ": "D",

    "What is the chemical formula for water?: ": "A",
    "What is the process called by which plants convert sunlight into energy?: ": "A",
    "What is the name of the force that keeps us on the ground?: ": "A",
    "What is the name of the largest country in the world by land area?: ": "C",
    "What is the name of the smallest continent?: ": "E",

    "What is the capital of Italy?: ": "A",
    "What is the name of the currency used in Japan?: ": "D",
    "What is the national language of Spain?: ": "A",
    "What is the name of the largest ocean?: ": "A",
    "What is the name of the tallest mountain range in the world?: ": "C",

    "What is the capital of Germany?: ": "A",
    "What is the name of the country that shares a border with both North and South Korea?: ": "B",
    "What is the name of the largest desert in the world?: ": "A",
    "What is the name of the river that flows through Paris?: ": "D",
    "What is the name of the largest country in South America?: ": "C",

}

options = [

    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth"],

    ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
    ["A. Jupiter", "B. Saturn", "C. Earth", "D. Mars"],
    ["A. Au", "B. Ag", "C. Fe", "D. Cu"],
    ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"],
    ["A. China", "B. India", "C. United States", "D. Indonesia", "E. Japan"],

    ["A. Jane Austen", "B. Charlotte Brontë", "C. Emily Brontë", "D. George Eliot"],
    ["A. Leonardo da Vinci", "B. Michelangelo", "C. Raphael", "D. Sandro Botticelli"],
    ["A. Georges Bizet", "B. Giacomo Puccini", "C. Giuseppe Verdi", "D. Richard Wagner"],
    ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Guglielmo Marconi", "D. Nikola Tesla"],
    ["A. Alexander Fleming", "B. Howard Florey", "C. Ernst Chain", "D. All of the above"],

    ["A. H2O", "B. CO2", "C. CH4", "D. N2"],
    ["A. Photosynthesis", "B. Respiration", "C. Transpiration", "D. Germination"],
    ["A. Gravity", "B. Magnetism", "C. Friction", "D. Inertia"],
    ["A. Russia", "B. Canada", "C. China", "D. United States"],
    ["A. Oceania", "B. Asia", "C. Europe", "D. Africa", "E. South America"],

    ["A. Rome", "B. Milan", "C. Naples", "D. Florence"],
    ["A. Japanese yen", "B. Chinese yuan", "C. South Korean won", "D. Indian rupee"],
    ["A. Spanish", "B. Catalan", "C. Basque", "D. Galician"],
    ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean", "E. Southern Ocean"],
    ["A. Andes Mountains", "B. Rocky Mountains", "C. Himalayas", "D. Alps", "E. Ethiopian Highlands"],

    ["A. Berlin", "B. Munich", "C. Cologne", "D. Hamburg"],
    ["A. China", "B. Russia", "C. North Korea", "D. South Korea"],
    ["A. Sahara", "B. Gobi", "C. Arabian", "D. Kalahari"],
    ["A. Seine", "B. Rhone", "C. Loire", "D. Garonne"],
    ["A. Brazil", "B. Argentina", "C. Colombia", "D. Peru", "E. Chile"],

]

new_game()

while play_again():
    new_game()

print("Bye!!")
