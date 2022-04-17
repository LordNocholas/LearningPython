import random 

class Character:
    # class variable
    characterCount = 0

    # constructor method
    def __init__(self, name):
        self.name = name
        self.items = ["sword"]
        Character.characterCount += 1

    def nameDisplay(self):
        print("Welcome {}".format(self.name))

    def inventoryUpdate(self, item):
        print("You found a {}".format(item))
        self.items.append(item)

    def itemsDisplay(self):
        print("Your current items are: ")
        for i in self.items:
            print(i)

c1 = Character("Sheldor")
print("Number of characters created is {}".format(Character.characterCount))
c1.nameDisplay()
c1.inventoryUpdate("Shield")
c1.itemsDisplay()

c2 = Character("LordNocholas")
c2.nameDisplay()
c2.itemsDisplay()


        
