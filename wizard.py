# The wizard's castle
# By Andrew and Jonathan
from treasure import Treasure
# Gameplay Constants
# MAP constants
MAP_MONSTER_DENSITY = 0.3
MAP_TREASURE_DENSITY = 0.05
# TREASURE_LIST = (, , )
TREASURE_LIST = (
    Treasure('Norn Stone'),
    Treasure('Opal Eye'),
    Treasure('Black Sapphire')
)

for treasure in TREASURE_LIST:
    print(treasure.name)

# map_size = 0
# while (int(map_size) > 11 or int(map_size) < 5):
#     map_size = input ('Choose a dungeon size (5 to 10): ')
# print ('You have chosen map size: ' + map_size)
# gender = None
# gender_list = ['M', 'F', 'm', 'f']
# while (gender not
#     in gender_list):
#     gender = input ('Do you want to be male "M" or female "F"? ')
#     if (gender not in gender_list):
#         print ('Please choose "M" or "F"!')

# race = None
# race_list = ['Human', 'Elf', 'Werewolf']
# def convert_lower (stringy): return stringy.lower()[0]
# race_list_lower = list(map(convert_lower, race_list))
# print (race_list_lower)
# while (race.lower() not in race_list.):

