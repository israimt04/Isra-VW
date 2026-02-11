people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print(len(people))

people['Lisa'] = 'Green'

people.pop('Jenny')

for name in sorted(people):
    print(name, people[name])