from adventurelib import *

@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You bush your long flowings locks
		with the gold hairbush that you have 
		selected from in the red basket. """)

space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently 
	to your left, its airlock open and waiting. """)


spaceship = Room("""
	The bridge of the spaceship is shiny and white,
	with thousands of small, red, blinking lights. """)

current_room = space 

print(current_room)

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
@when("enter")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here")
	
	else:
		current_room = spaceship
		print("""
		You heave yourself into the spaceship and 
		slam your hand on the button close to the door.
		""")
		print(current_room)



def main():
	start()

if __name__ == '__main__':
	main()