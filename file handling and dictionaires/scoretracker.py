def read_scores():
    try:
        with open ("scores.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No scores found. The file does not exist.")
def load_scores():
    try:
        with open ("scores.txt","r") as file:
            scores = {}
            for line in file:
                name,score = line.strip().split(":")
                scores[name] = int(score)
            return scores
    except FileNotFoundError:
        return {}
def update_score():
    scores = load_scores()
    name = input("Enter your name: ").lower()
    score = int(input("Enter your score: "))
    
    scores[name] = score  # update or add

    with open("scores.txt", "w") as file:
        for student, s in scores.items():
            file.write(student + ":" + str(s) + "\n")

    print("Updated scores:")
    for student, s in scores.items():
        print(student + ":" + str(s))
while True:
    action = input("Would you like to (R)ead the scores or (A)dd/update a score(R/A): ")
    if action.lower() == "r":
        read_scores()
    elif action.lower() == "a":
        update_score()
    else:
        print("Invalid input. Please enter R or A.")
        continue
 


    