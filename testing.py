text = "apple" #string
number = 10 #integer
decimal = 10.5 #float
has = True #boolean
coordinates = (10.0, 20.0) #tuple
names = ["Elvis", "Bob", "Egil"] #list
unique = {1, 2, 3, 4, 4, 5} #set
user = {"name": "Elvis", "age": 24, "is_admin": True} #dictionary


#type constructor.

number = "21"
print(10 + int(number)) #convert string to integer










# Note: How the text-to-speech app was made
# The app uses Tkinter, which is included with Python, to create its desktop
# window, text box, voice menu, speed slider, and Speak and Stop buttons.
# It uses the pyttsx3 package as its speech engine. The engine reads the
# available voices from the computer, so the app does not send text to an
# online speech service.
# When Speak is clicked, the app reads the text box, applies the selected
# voice and speed, and asks pyttsx3 to speak. Stop cancels speech. Tkinter's
# event loop is also used to keep the speech engine responsive while the
# window is open. The dependency is listed in requirements.txt.







# name = input("What is your name? ")
# age = int(input("How old are you? "))

# if age >= 18:
#     print("Hello", name)
#     print("You are an adult!")
# else:
#     print("Hello", name)
#     print("You are still under 18!")