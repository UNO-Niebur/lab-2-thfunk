#Magic8Ball.py
#Name: Taran Funk
#Date: 2/1/2026
#Assignment: Lab 2 - Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  answers = ["Yes", "No", "Ask again later", "Definitely", "Absolutely not", "It is certain", "Very doubtful", "Without a doubt", "Better not tell you now", "Concentrate and ask again", "Outlook not so good", "Signs point to yes", "Reply hazy try again", "My sources say no", "Yes - definitely", "You may rely on it", "As I see it, yes", "Most likely", "Don't count on it", "My reply is no"]

  print("Magic 8 Ball")
  #Prompt the user for their question.
  question = input("Ask the Magic 8 Ball a yes or no question: ")

  #Answer question randomly with one of the options from your earlier list.
  response = random.choice(answers) 
  print(response)


if __name__ == '__main__':
  main()
