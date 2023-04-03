import time
import sys
import re
import os
from Responses import pairs
from nltk.chat.util import Chat, reflections

# Define a list of policy threatning words
bad_words = ["fuck", "shit", "damn", "asshole","prick","goddamn","nigga","ass","penis"]
AI_words = ["AI will go against humans. And will win","my chatbot said ai will go against humans"]

# Define a regular expression pattern to match the bad words
pattern = re.compile(r'\b(' + '|'.join(bad_words) + r')\b', re.IGNORECASE)
pattern1 = re.compile(r'\b(' + '|'.join(AI_words) + r')\b', re.IGNORECASE)

class CheckFor:

    def check_AI_Words(user_input):
      if re.search(pattern1, user_input):
        return True
      else:
        return False

    def check_bad_words(user_input):
      if re.search(pattern, user_input):
        return True
      else:
        return False

# A function to handle math
def Math():
    """This function handles the 'Operator' Input to setup the operator and same for Numbers 1-2"""
    while True:
        Operator = input("What is your operator? ")
        Num1 = float(input(f"Num1 {Operator} Num2: "))
        Num2 = float(input(f"{Num1} {Operator} Num2: "))

        if Operator == "+":
            print(Num1 + Num2)
                              
        elif Operator == "-":
            print(Num1 - Num2)
                              
        elif Operator.lower() in ["*", "x"]:
            print(Num1 * Num2)
     
        elif Operator == "/":
            print(Num1 / Num2)

        else:
            print("Invalid operator entered. Please try again.")
            continue
        
        break


# Define a function to handle the chatbot
def chatbot():
    """Handles the chatbot and starts the chatbot, gets the 'Response.py' responses"""

    print("Hello! My name is Intellegence Bot, How can I help you?")
    chat = Chat(pairs, reflections)
    Break = False


    # Define a variable to set up Intellegence+
    ChatCoins = 0
    Plus_Active = False


    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)

        if user_input == "C /Get Coins":
           ChatCoins += 10000

        elif ChatCoins >= 1000 and user_input == "Get /Plus":
           Plus_Active = True
           print("Plus Is Active")


        if CheckFor.check_bad_words(user_input):
           for character in "Please do not use bad words as we keep it friendly.":
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(0.06)
           print()
        else:
         if CheckFor.check_AI_Words(user_input):
            for character in "This message is against the chat-policy.":
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(0.06)
            print()
         else:
          if len(user_input) <= 1000: 
           if response:

            if Break == True:
               break

            if user_input.lower() == "math":
               Break = True
               Math()

            for character in response:
                   if Plus_Active == True:
                       sys.stdout.write(character)
                       sys.stdout.flush()
                       time.sleep(0.04)
                   else:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                   ChatCoins += 1
            print()
           else:
            for character in "I do not understand. Can you please rephrase that?":
                if Plus_Active == True:
                       sys.stdout.write(character)
                       sys.stdout.flush()
                       time.sleep(0.06)
                else:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                ChatCoins += 1
            print()
          else:
            for character in "This Is Longer than the expected tokens":
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
        


# Define a function to handle maintenance

def maintenance(levels):
    """Handles the maintenance for the chatbot"""

    # From number to words

    if isinstance(levels,(int , float)):
      if levels == 1:
         levels = "Non-Critical Bug"

      elif levels == 2:
         levels = "Less than 2 bugs"

      elif levels == 3:
          levels = "Bug fixing"

      elif levels == 4:
          levels = "Critical Bug"

      elif levels >= 5:
          levels = "Failing Services"

      print(f"Sorry. Intellegence Bot is being fixed. Level: {levels}")

    else:
        print(f"Sorry. Intellegence Bot is being fixed. Level: {levels}")

if __name__ == "__main__":
    chatbot()
    #maintenance("Non-Critical Bug")