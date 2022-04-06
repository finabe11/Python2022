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

cannibals_village = Room(""" You look ahead and see some things resembling houses, you walk forward to look closer,
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
	You are taking a holiday form being an explorer, you have decied to take a cruise, the cruise""")

#connections for Rooms
current_room = starting_beach



def main():
	start()

if __name__ == '__main__':
	main()
