questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "What is the national bird of India?", "Pigeon", "Peacock", "Sparrow",
    "Crow", "None", 2
  ],
  [
    "When did India became independant?", "1947", "1951", "1800",
    "1972", "None", 1
  ],
  [
    "Which is the largest continent?", "Africa", "North America", "Asia",
    "Europe", "None", 3
  ],
  [
    "WWhat is the capital of Australia?", "Sydney", "Melbourne", "Canberra",
    "Brisbane", "None", 3
  ],
  [
    "Which planet is known as the Red Planet?", "Mars", "Earth", "Jupiter",
    "Neptune", "None", 1
  ],
  [
    "Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso",
    "Michelangelo", "None", 2
  ],
  [
    "In which year did World War II end?", "1945", "1918", "1975",
    "1955", "None", 1
  ],
  [
    "What is the chemical symbol for gold?", "Ag", "Go", "Au",
    "Gl", "None", 3
  ],
  [
    " Which famous scientist developed the theory of general relativity?", " Isaac Newton", "Albert Einstein", "Marie Curie",
    "Nikola Tesla", "None", 2
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"\n\n", question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")