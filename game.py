from adventurelib import *
Room.items = Bag()


#Rooms 
starting_beach = Room("""
	You look around and see a gently sloping hill leading up to the edge of the forest covered in godlen coloured sand,
	you can feel the sand between your toes, the forest is just up ahead with massive plam trees towering above some small srubs,
	you see that after the plam trees the forest get small and more thick. You heard some weird calling that sounds human, """)

Path = Room("""
	You start walking down the path, with trees towdering over you, you stand on a tiwg, is snaps giving you am fright, then you see movement farther down the path, you see a bush that looks great for hiding in.""")

Bush = Room("""
	You can just see out of the bush you see some people with cloths around there wasts carrying spears and sheilds, you reasles
	that they are cannibals, """)

cannibal_village = Room(""" You look ahead and see some things resembling houses, you walk forward to look closer,
	you see that the house are made with stick stuck together with dried mud then plasered with leaves in some areas,
	you look up there are heaps of these houses, with looks like a massive farther away,
	while you are looking around you see another path""")

Cannibal_bosses_house = Room(""" You start walking towards the large house to see if you can find anything, something comes out of the big hut, it is a very strong looking cannibals, 
	it starts running towards you """)

second_path = Room(""" 
	You see another path that looks similar to the one you came through the beach. """)

Third_beach = Room("""
	Through the trees you glimpse something blue, you brust out of the trees to find a beach slowly sloping down, with the sea about 100 meters away,
	 to spot something farther down the beach, its a jetty with a boat at the end of it, you start running.""")

Forest = Room("""
	You have decided that it would be safer to go throught the forest, you have a hard time going throught the forest,
	with all it's vines and branches.""")

Second_beach = Room("""
	You stumble out of the forest on to a sand beach covered in shells, with no idea of which way you have come. >you have something glithing or food or have a storage thing from the cannibals""")

Death_forest = Room("""
	You start wayding throught the forest againg and you sand on something slipery and you fall heaverly and then you feel something bit you it very painful you look doen and see a snake,
	you try and move but you are prazlyed, you died a slow and painful death.""")

#this is my back ground story
print(""" You are Francis Drake.
	You are taking a holiday form being an explorer, you have decied to take a cruise, you are out on the side of the cruise at night looking at the ocean, you heard yelling,
	you turn to the front of the boat and see a very vage shape in front of the boat, you realse is a large rock sticking out of the water, the boat is heading striaght for it, you brace for impact by lying down,
	theres a tremendous bang, the whole boat pitches forwards and you are throwen off the boat, into the ptich black sea. 
  you swim up to the surface and  start treading water, while you have a look around to see where you are, it is very hard to see around, all you see is darkness, something bums into you you look at it is a briefcase, you grab on to it.
  A cloud finishes passing over the moon, and now it is light so you have a look around to see if you can see the boat, you can't, but in the distance you see something else, you start swimming to it, while holding on to the briefcase.
  As you get closer you realise that it's a island, you have another look around to see if you can see the cruise you can't, so you carry on swimming to the island.
  The waves start to pick up, it is now very hard to see the island, you try and swim harder but that only make you more tired, you try one last desperate attempt to make it to the island, you feel your body going numb and you eyes slowing closing, you think that this is it, your whole life gone in an second.
  You feel your consciousness stir, you feel something in your eyes, it's sand, you quicky open your eyes and sit up resiling that you are alive, you look  around, you are on the island you saw in the distance, you look down and see the breifcase next to you. """)
print("")
#the commands so people know how to play
print("The commands you can use are go north,south,east and west, grab/take, use and inventory (inv)")
print("")

#connections for Rooms
starting_beach.east = Path 
Path.west = Bush 
Path.north = cannibal_village
cannibal_village.west = Cannibal_bosses_house
cannibal_village.east = second_path
second_path.north = Third_beach
starting_beach.west = Forest
Bush.west = Forest
Forest.west = Second_beach
Forest.north = Death_forest

#define and describe Items

petrol = Item("petrol")
petrol.description = "A yellowly liquid that might be useful for a vehicle"

key = Item("key")
key.descritption = "A sliver key, thats a little bit rusty, might open, unlock or start something"

machete = Item("machete")
machete.descritption = "A long sliver with patch of brown ruch and the handle is slowly crumbing off, might be useful for getting around a forest and defending yourself"



#add items to bags
starting_beach.items.add(machete)
Second_beach.items.add(petrol)
Cannibal_bosses_house.items.add(key)

#define variable
current_room = starting_beach
inventory = Bag()
print(current_room)

#binds
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
	

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")



#binds



def main():
	start()

if __name__ == '__main__':
	main()
