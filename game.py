from adventurelib import *
Room.items = Bag()


#Rooms 
starting_beach = Room("""
	You look around and see a gently sloping hill leading up to the edge of the forest covered in golden coloured sand.
	You can feel the sand between your toes. The forest is just up ahead with massive plam trees towering above some small shrubs.
	You see that after the palm trees the forest get small and more thick. You heard some weird calling that sounds human. You look around and see something sticking up in the ground, it looks like a weapon of some sort.""")

Path = Room("""
	You start walking down the path, with trees towering over you. You stand on a twig, it snaps giving you a fright. Then you see movement farther down the path. You see a bush that looks great for hiding in.""")

Bush = Room("""
	You can just see out of the bush. You see some people with clothes around their waists carrying spears and shields. You realise
	that they are cannibals. """)

cannibal_village = Room(""" You look ahead and see some things resembling houses. You walk forward to look closer.
	You see that the house are made with sticks stuck together with dried mud then plastered with leaves in some areas.
	You look up, there are a lot more similar houses further ahead. There's another house, but it's massive and further away than the rest. While you are looking around you see another path.""")

Cannibal_bosses_house = Room(""" You start walking towards the large house to see if you can find anything. Something comes out of the big hut. It is a very strong looking cannibal.
	It starts running towards you. It has something shinny tied aroung its neck.""")

second_path = Room(""" 
	You see another path that looks similar to the one you came through from the beach. """)

Third_beach = Room("""
	Through the trees you glimpse something blue. You burst out of the trees to find a another beach slowly sloping down, with the sea about 100 meters away.
	You spot something farther down the beach. It's a jetty with a boat at the end of it. You start running.""")

Forest = Room("""
	You have decided that it would be safer to go throught the forest. You have a hard time cutting throught the forest,
	with all it's vines and branches.""")

Second_beach = Room("""
	You stumble out of the forest on to a sandy beach covered in shells, with no idea of which way you have come. You look down the beach and see a small hut, mabye made by another traveler. You walk towards it and see inside that there  is a can of some sort. """)

Death_forest = Room("""
	You start wading through the forest again and you stand on something slippery. You fall heavily and then you feel something bite you. It's very painful. You look down and see a snake.
	You try and move but you are paralysed. You die a slow and painful death.""")

#this is my back ground story
print(""" You are Francis Drake.
	You are taking a holiday from being an explorer. You have decided to take a cruise. You are out on the side of the cruise at night looking at the ocean. You hear yelling.
	You turn to the front of the boat and see a very vague shape in front of the boat. You realise it is a large rock sticking out of the water. The boat is heading striaght for it. You brace for impact by lying down.
	There's a tremendous bang. The whole boat pitches forwards and you are thrown off the boat into the pitch black sea. 
  You swim up to the surface and start treading water while you have a look around to see where you are. It is very hard to see around, all you see is darkness. Something bumps into you. You look at it. It's a briefcase. You grab onto it.
  A cloud finishes passing over the moon. Now it's lighter so you have a look around to see if you can see the boat. You can't, but in the distance you see something else. You start swimming to it, while holding onto the briefcase.
  As you get closer you realise that it's a island. You have another look around to see if you can see the cruise ship. You can't, so you carry on swimming to the island.
  The waves start to pick up. It is now very hard to see the island. You try and swim harder but that only makes you more tired. You try one last desperate attempt to make it to the island. You feel your body going numb and your eyes slowly closing. You think that this is it, your whole life gone in a second.
  You feel your consciousness stir. You feel something in your eyes, it's sand. You quicky open your eyes and sit up realising that you are alive. You look around. You are on the island you saw in the distance. You look down and see the briefcase next to you.""")

#the commands so people know how to play
print("The commands you can use are look around (look), go north,south,east and west, grab/take, use and inventory (inv). You type the command in and then press enter")

#connections for Rooms
current_room = starting_beach
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

#define Items 
Item.description = ""   #This adds a blank description to each item 

petrol = Item("petrol")
petrol.description = "A yellowy liquid that might be useful for a vehicle"

key = Item("key")
key.descritption = "A silver key, that's a little bit rusty, might open, unlock or start something"

machete = Item("machete")
machete.descritption = "A long silver with patches of brown rust, the handle is slowly crumbling off, might be useful for getting around a forest and defending yourself"

briefcase = Item("briefcase")
briefcase.descritption = "A briefcase full of money, might be useful if you get off the island"


#add items to bags
starting_beach.items.add(briefcase)
starting_beach.items.add(machete)
Second_beach.items.add(petrol)
Cannibal_bosses_house.items.add(key)

#define variable
current_room = starting_beach
inventory = Bag()
print(current_room)
enter = False
boss = True 


#binds

@when("go DIRECTION")
def travel(direction):
  global current_room
  global enter

  if current_room == starting_beach and inventory.find("machete") == None:
  	print("You need something to cut into the forest")
  	return
  if current_room == starting_beach and inventory.find("machete") and enter == False:
  	print("You use the machete to slash a path through the forest")
  	enter = True 
  	return



 
  if direction in current_room.exits():
    current_room = current_room.exit(direction)
    print(f"You go {direction}.")
    print(current_room)
    print(current_room.exits())
    if current_room == Death_forest:
    	quit()


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





@when("kill boss")
@when("fight boss")
def fight_boss():
	if inventory.find("machete") and current_room == Cannibal_bosses_house:
		print("print your fight ........ Boss drops item")




def main():
	start()

if __name__ == '__main__':
	main()
