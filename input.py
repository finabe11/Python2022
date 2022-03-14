#6.3 Exercises
#1
"""
print("hello")
input ("Push any key and then press enter: \n ")
print("")
#2
input("Type your name and the push enter: \n")
print("")
#3
input("Type your age and the push enter: \n")
print("")
#4
user_name = input("Type your name and the push enter: \n")
print("")
#5
user_age = input("Type your age and the push enter: \n")
print("")
#6
favourite_movie = input("Type your favourite movie and the push enter: \n")
print("")
#7
name_a_book = input("Type the name of a book and the push enter: \n")
print("")
#8
name_a_adjective = input("Type an adjective and the push enter: \n")
print("")
#9
name_a_noun = input("Type a noun and the push enter: \n")
print("")
#10
name_a_verb = input("Type an verb and the push enter: \n")
print("")
#11
print (f"Welcome, {user_name}, you are {user_age} years old \n")
print(f"Your favourite movie is {favourite_movie} \n")
print(f"Random book name: {name_a_book} \n")
print(f"Random adjective: {name_a_adjective} \n")
print(f"Random noun: {name_a_noun} \n")
print(f"Random verb: {name_a_verb} \n")
print(f"Your favourite movie and book are {favourite_movie} and {name_a_book} \n")
print(f"Random adjective, noun and verb: {name_a_adjective}, {name_a_noun} and {name_a_verb} \n")
#12
user_age = int(input("How old are you? \n"))
#13
print (f"You will be {user_age + 10} in ten years")
print("")
#14
print(f"You were born in the year {2021 - user_age} ")
print("")
#15
user_apples = int(input("How many apples do you have? \n"))
#16
user_friends = int(input("How many friends do you have? \n"))
#17
print(f"If you share your apples with you friends they will get {user_apples / user_friends} apples each")
print("")
print(f"If you share your apples with you friends evenly there will be {user_apples % user_friends} apples left over")
print("")
#18
user_pizza = int(input("How many pizza's do you want? \n"))
#19
user_people = int(input("How many people are you feeding? \n"))
#20
print(f"If you share your pizza's with you friends they will get {user_pizza * 8 // user_people} slices each")
print("")
print(f"If you share your pizza's with you friends evenly there will be {user_pizza % user_people} slices left over")
print("")
#21
user_money = int(input("How many dollars do you have?\n"))
#22
TV_cost = int(input ("How much money does a TV cost?\n"))
#23
print(f"You have {user_money - TV_cost} dollars after you buy a TV ")
print("")
#24
print(f"There is a 20% off sale on TV's and the Tv will cost {0.8 * TV_cost} if you wait for the sale.")
print("")
#25
user_bitcoin = int(input("How many Bitcoin do you have? \n"))
#26
bitcoin_price = 57334.53
#27
print(f"Your cryto portfolio is worth {user_bitcoin * bitcoin_price} dollars")
print("")
#28
user_wage = int(input("How much money do you earn in a week? \n"))
#29
tax_rate = float(input("What is the tax rate as a decimal? \n"))
#30
print(f"You take home {(1 - tax_rate) * user_wage} dollars ever week.")
print("")
"""
#31
book_name = input("Name a book? \n")
print("")
#32
print(book_name.upper())
print(book_name.lower())
print(book_name.title())
print("")
#33
number = int(input("Pick a number \n"))
print("")
#34
print(book_name * number )
print("")