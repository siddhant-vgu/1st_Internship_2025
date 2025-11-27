import google.generativeai as genai

key = "AIzaSyCKbLmhn_jMaRP84A924nG8NRJKkw32nYc"


genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("You:")
    if user.lower() == "exit":
        print("Bye Bye")
        break
    response = model.generate_content(user)
    print("Bot: ",response.text)
