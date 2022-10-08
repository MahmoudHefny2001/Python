#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

prompt = "\nTell me something, and I will repeat it back to you or enter 'quit' to end the program: "
#prompt += "\nEnter 'quit' to end the program. "

message = ""
#while message != 'quit':
    #message = input(prompt).lower()
    #if message != 'quit':
        #print(message.title())

go = True
while go :
    message = input(prompt)
    if message.lower() == 'quit':
        go = False
    else:
        print(message)
