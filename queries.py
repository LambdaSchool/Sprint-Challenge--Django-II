from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
print('total characters: ', Character.objects.count())  # a: 302

# How many of each specific subclass?

# Mages
print('mages: ', Mage.objects.count())
# a: 108

# Fighters
print('fighters: ', Fighter.objects.count())
# a: 68

# Clerics
print('clerics: ', Cleric.objects.count())
# a: 75

# Thieves
print('thieves: ', Thief.objects.count())
# a: 51

# Necromancers
print('necromancers: ', Necromancer.objects.count())
# a: 11

# How many total Items?
print('items: ', Item.objects.count())
# a: 174

# How many of the Items are weapons?
print('weapons: ', Item.objects.filter(
    weapon__isnull=False).count())
# a: 37

# How many are not?
print('nonweapon items: ',
      Item.objects.filter(weapon__isnull=True).count())
# a: 137

# On average, how many Items does each Character have?
# mage items avg
mages = list(Mage.objects.all())
mage_total = 0
for mage in mages:
    mage_total += mage.inventory.count()

print('mage avg items count: ', round(
    mage_total / Mage.objects.count()))  # Answer: 4

# fighter items avg
fighters = list(Fighter.objects.all())
fighter_total = 0
for fighter in fighters:
    fighter_total += fighter.inventory.count()

print('fighter avg items count: ', round(
    fighter_total / Fighter.objects.count()))  # Answer: 4

# cleric items avg
clerics = list(Cleric.objects.all())
cleric_total = 0
for cleric in clerics:
    cleric_total += cleric.inventory.count()

print('cleric avg items count: ', round(
    cleric_total / Cleric.objects.count()))  # Answer: 3

# thief items avg
thieves = list(Thief.objects.all())
thief_total = 0
for thief in thieves:
    thief_total += thief.inventory.count()

print('thief avg items count: ', round(
    thief_total / Thief.objects.count()))  # Answer: 3

# necromancer items avg
necromancers = list(Necromancer.objects.all())
necromancer_total = 0
for necromancer in necromancers:
    necromancer_total += necromancer.inventory.count()

print('necromancer avg items count: ', round(
    necromancer_total / Necromancer.objects.count()))  # Answer: 3

# On average, how many Weapons does each character have?
