# Define some pattern-response pairs for the chatbot
pairs = [
    # Easter egg

    ["G -e --update",["EPICO EL MAGICO"]],
    ["GET -exe",["This statement is false."]],
    ["BARREL IS GREAT!|EXE IS WOWS",["Do a barrel roll!"]],
    ["You Have A FIRST WORD?|ARE YOU A REAL CHATBOT BABY -e --update",["My first word is: Hello, world!"]],

    # Intellegence+

    ["Get /Plus",["Getting Plus"]],
    ["C /Get Coins",["Getting Coins"]],

    # Simple chat

    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["what is your name?|who are you?", ["My name is Intellegence Bot.", "You can call me Intellegence Bot."]],
    ["how are you?", ["I'm doing well, thank you!", "I'm good, how about you?"]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
    ["let's do coding|let's code|code",["let's code!","Are you ready?"]],
    ["what's the weather today?",["I do not know as I am just a simple chatbot."]],

    # Facts

    ["do you know about poop|what is poop|poop",["""Poop, also known as feces, is the 
solid or semisolid matter that is eliminated from the body during the process of defecation. 
It is made up of waste materials from the digestive system, including undigested food, 
bacteria, and other substances. The color, texture, and odor of poop can vary based on a 
variety of factors, such as diet, hydration levels, and health conditions. While poop may not 
be a pleasant topic for everyone, it is a normal and important part of the body's waste 
elimination process."""]],

    ["will ai go against humans|ai will go against humans?|is ai gonna go against humans?",["No, AI will not go against humans.","""Artificial intelligence is not meant to be a replacement for humans, but rather a tool to 
    assist and enhance our capabilities. The development of AI is aimed at making our lives 
    easier and more efficient, not to compete with or undermine human intelligence. The goal is 
    to create a symbiotic relationship between humans and AI, where we can work together to 
    achieve common goals and tackle complex problems.""","""No, AI will never replace humans or go against humans as they were made to help
    humans."""]],

    ["content policy|policy|chatbot policy|chat policy",["The policy for chatting here is in this link: "]],

    ["what is your current version|version|--version",["My current version is 1.0.0"]],

    ["html|website language",["""HTML or: Hypertext Markup Language is a programming language that was made in 1993. 
    HTML is the structure of very single website."""]],

    ["php",["""PHP is a general-purpose scripting language geared toward web development. 
    It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995. 
    The PHP reference implementation is now produced by The PHP Group. Typing Discipline: Dynamic, Weak, Gradual"""]],

    # Coding

    ["Make a simple html script|Make a simple html|simple html",["""Okay! this is a simple html script named Website: 
        <!DOCTYPE html>
        <html lang="en">
        <head>
           <meta charset="UTF-8">
           <meta http-equiv="X-UA-Compatible" content="IE=edge">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <title>Website</title>
        </head>
        <body>
           <h1>Hello world</h1>
        </body>
        </html>""","""Okay! this is a simple html script named First website: 
        <!DOCTYPE html>
        <html lang="en">
        <head>
           <meta charset="UTF-8">
           <meta http-equiv="X-UA-Compatible" content="IE=edge">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <title>First website</title>
        </head>
        <body>
           <link rel="stylesheet" href="style.css">
           <h1 class="Test">Hello world</h1>
        </body>
        </html>
        
        CSS:
        
        h1.Test{
            color: white;
        } """]],

    ["make a simple python script|simple python|can you make a simple python script?",["""Okay! This is a simple python script that will print Numbers based on a function parameter.
    
    def Number(Number):
        
        # Checking if it is a number
        
        if isinstance(Number,(int,float)):
            print(Number)
            
        else:
            print("Not a number!")""","""Okay! This script will change numbers to words.
            
            # Make a function that will check if it is a number

            def Function_Name(word):
                
                if isinstance(word,(int,float)):
                    if word == 1:
                        word = "Hi" 
                        
                    # Continue Code Here ""","""This python script will make a calculator:
                    
                    def Calculator(Operator,N,N1):
                        
                        if Operator == "+":
                             print(N+N1)
                              
                        elif Operator == "-":
                             print(N-N1)
                              
                        elif (Operator.lower() == "*" or "x"):
                             print(N*N1)
     
                        elif Operator == "/":
                             print(N/N1), This will make a calculator.""","""Here is a python script that will check if it is binary or not

                             def is_binary(number):
                                binary_digits = set("01")
                                for digit in str(number):
                                   if digit not in binary_digits:
                                        print("This is not binary")
                                        return
                                print("This is binary")

                                is_binary(10001101010101)""","""This will print hello world:
                                    
                                    print("hello world")"""]],

    ["make a simple chatbot|simple python chatbot",["""Okay! this simple python script will make a simple chatbot.
            from nltk.chat.util import Chat, reflections
            
            # Responses for the bot
            
            responses = [
              ["Hi",["Hello!","Hello There"]],
            ]
            
            # A function to handle chatbot
            
            def ChatBot():
                
                print("Hi! My Name Is ChatBot-1")
                CHAT = Chat(responses, reflections)
                
                while True:
                    InputToRespond = input("")
                    Bot_Response = CHAT.respond(InputToRespond)
                    
                    print(Bot_Response)
                    
            ChatBot(), This scipt uses the 'nltk' library for the chatbot functions. It will pick a random response from the pairs and prints
            it out.""","""A simple chatbot in python
            from nltk.chat.util import Chat, reflections
            
            # Responses for the bot
            
            responses = [
              ["Hi",["Hello!","Hello There"]],
            ]
            
            # A function to handle chatbot
            
            def ChatBot():
                
                print("Hi! My Name Is ChatBot")
                CHAT = Chat(responses, reflections)
                
                while True:
                    InputToRespond = input("")
                    Bot_Response = CHAT.respond(InputToRespond)
                    
                    if response:
                       for character in response:
                           sys.stdout.write(character)
                           sys.stdout.flush()
                           time.sleep(0.04)
                       print()""","""Alright.
            from nltk.chat.util import Chat, reflections
            
            # Responses for the bot
            
            responses = [
              ["Hi",["Hello!","Hello There"]],
              ["1+1",["1+1 = 2"]],
            ]
            
            # A function to handle chatbot
            
            def ChatBot():
                
                print("Hi! My Name Is First Chat Bot")
                CHAT = Chat(responses, reflections)
                
                while True:
                    InputToRespond = input("")
                    Bot_Response = CHAT.respond(InputToRespond)
                    
                    print(Bot_Response)"""]],

    ["python random numbers",["""Okay! this is a simple python script that will print out 10 random numbers:
    import random
    
    Loopcount = 0
    MaxLoop = 10

    while Loopcount < MaxLoop:
        N = random.choice(range(10000))
        
        print(N)
        Loopcount += 1. This uses the 'random' library to get a random number, You can see it in action on line 5. """]],
]