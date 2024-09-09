from dataset import responses

#chatbot responses
def chatbotResponse(userInput):
    for key in responses.keys():
        if key in userInput.lower():
            return responses[key]
    return "Sorry, I don't Understand that"

#user Interface
while True:
    userInput = input("You: ")
    if userInput.lower() == "exit":
        break
    print("Chatbot : ", chatbotResponse(userInput))