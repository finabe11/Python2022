from adventurelib import *
Room.items = Bag()

'''
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
'''
#Rooms
space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently 
	to your left, its airlock open and waiting. """)

spaceship = Room("""
	The bridge of the spaceship is shiny and white,
	with thousands of small, red, blinking lights. """)

cargo = Room("""
	The cargo room has lots of boxes and suitcases. They stack up 
  high to the ceiling.
	They look like they could topple at any moment. Wait what is 
  that under the stack in the corner.
	Could that be a body?
	""")

docking = Room("""
	The other ships must be huge. There are so many spaces,
	but where are they all.
	""")

hallway = Room("""
	The Hallway is long and dark. It is hard to see the end of 
  it, there might be a faint
	light at the end.
	""")

bridge = Room("""
	There are too many people here. It is so noisy with all the 
  talking but there is something else.
	A high pitched sound which is almost hypnotising.
	""")

quarters = Room("""
	At last a place to rest. But no one is in here. Where has 
  everyone gone.
	And why does it seem like everyone left on a hurry.
	""")

mess_hall = Room("""
	There is food and wine and music. A strange music that I have 
  never heard before. Is this where I can find what I have been 
  looking for.
	""")

escape_pods = Room("""
	This area is guarded and they are armed. It might be possible
	to sneak around without being seen but you might need 
  something to help you.
	""")

#connections 
spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mess_hall
quarters.east = mess_hall
bridge.south = escape_pods
cargo.east = docking

#define Items 
Item.description = ""   #This adds a blank description to each item 

Knife = Item("a dirty knife","dirty knife","knife")
Knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","red keycard","a keycard","keycard","a red card","red card","a card","card")
red_keycard.description = "It's a red keycard. It probably opens a door or a locker."

oxygen = Item("oxygen")
oxygen.description = "It's a colourless gas that you need to live, might be useful if you are running out of it."

torch = Item("torch","light")
torch.description = "An old torch. When you try it you see a faint light. Might be useful if anything happens "

#Add Items to Bags
#define Bags
mess_hall.items.add(red_keycard)
cargo.items.add(Knife)
docking.items.add(torch)
escape_pods.items.add(oxygen)


#Varibles
current_room = space 
inventory = Bag()
print(current_room)


@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
@when("enter")
@when("go in")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here")
	
	else:
		current_room = spaceship
		print(""" You heave yourself into the spaceship and 
		slam your hand on the button close to the door.
		""")
		print(current_room)

@when("go DIRECTION")
def travel(direction):
  global current_room
  if direction in current_room.exits():
    current_room = current_room.exit(direction)
    print(f"You go {direction}.")
    print(current_room)
    print(current_room.exits())

@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0:     #if there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)      #print out each item


@when("take ITEM")
@when("grab ITEM")
@when("pick up ITEM")


@when("get ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")


@when("inventory")
@when("inv")
@when("show inventory")
@when("bag")
@when("what is in my pocket")
@when("what is in my bag")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)
	if 

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")



dtrfrh

def main():
	start()

if __name__ == '__main__':
	main()