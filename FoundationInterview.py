#DATE: September 9, 2018. DESCRIPTION: My work for the "Computer Conversations" project. A program that responds using various user
#inputs, set against the backdrop of an interview for a shadowy government agency. SOURCES: All code is my own, only help that I got
#was from Berk Gokmen, Class of 2021, who showed me how to properly use the int() function.

print("FOUNDATION INTERVIEW by Lucas Eggers. DATE: September 9, 2018. DESCRIPTION: My work for the Computer Conversations project. A program that responds using various user inputs, set against the backdrop of an interview for a shadowy government agency. SOURCES: All code is my own, only help that I got was from Berk Gokmen, Class of 2021, who showed me how to properly use the //int() function.")

print("INTERVIEW LOG SCP CLASS3PERSONNEL 807-2 TRANSCRIPT BEGIN: ")


print("... right. Well, thank you for coming in today.")

responseFeeling = input("How are you feeling? ")

print("Good, good.")

responseName = input("Alright. Before we get to the true interview questions, I just have to confirm your identity. Name? ")

print("It's a pleasure to meet you, "+responseName+".")

responseField = input("Field of study? ")

print("Right, you must be here for the "+responseField+" and Anomalous Object Research Assisstant position.")

responseSecurity = input("...and what's the answer to your security question? ")

print("This won't influence your application's success, but I personally think "+responseSecurity+" is a cruel name for a dog.")

responseYears = int(input("Okay. For how many years now have you been interacting with anomalous or powered objects in your daily line of work? (Integer) "))

if responseYears < 6:
	print("Fresh blood, eh? Well, we can always use some new faces around the facility.")
else:
	print("It's good to know SOMEONE around here has some experience.")

responseWeakness = input("What would you say is your greatest weakness? ")

responseTaser = input("Huh. Really. "+responseWeakness+"? Mine is tasers. Those things hurt. Have you ever been tased? ")

print("I see.")

print("Listen. Everything seems to be in order. I'll talk to the higher-ups and see what I can do. Thank you for coming in.")

print("/ / / You feel a cold, damp cloth rise up from below and cover your face. Your vision slips away from you as all your muscles numb at once. / / /")