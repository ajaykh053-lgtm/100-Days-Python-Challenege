# Find, install and publish Python packages
#  with the Python Package Index
# Website: https://pypi.org/
# Prettytable documentation
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtal", "Charmendor"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.header_style = "cap"
table.align = "l"
print(table)
