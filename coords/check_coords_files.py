import yaml

with open('coords.yml', 'r', encoding="utf8") as file:
    row_coords = yaml.safe_load(file)

class Coords:
    pass

coords = Coords()

# coords.menu.lives.title = coords['menu']['lives']['title']
coords.menu = row_coords['menu']['lives']['title']
# coords.menu.lives.title = coords['menu']
# fff = coords['menu']
# print(fff)
# print(coords.menu.lives.title)
print(coords.menu)
print(type(coords.menu))