# Name: Angel Mendez
# Student ID 823650395
# Section: 18254
# Assignment: Module 4 Assignment EX1

cities_list = []
seattle_dict = {
    'name': 'Seattle',
    'pop': 784777,
    'State': 'Washington',
    'teams' : ["Seahawks", "Mariners", "Kraken", "Sounders FC", "Storm", "Reign FC", "Seawolves", "Torrent"] 
}
SF_dict = {
    'name': 'San Francisco',
    'pop': 826079,
    'State': 'California',
    'teams' : ["Giants", "Golden State Warriors", "49ers"] 
}
Miami_dict = {
    'name': 'Miami',
    'pop': 489812,
    'State': 'Florida',
    'teams' : ["Dolphins", "Heat", "Marlins", "Panthers", "Inter Miami CF"]     
}
cities_list.append(seattle_dict)
cities_list.append(SF_dict)
cities_list.append(Miami_dict)
favorite = input("What is your favorite team? ")
for cities in cities_list:
        for teams in cities['teams']:
                if favorite == teams:
                       print(f"If you like the {teams} you should move to {cities['name']}")