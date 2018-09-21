class Treasure:
    def __init__(self, name = "", description = "", base_value = 50, quantity = 1):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.base_value = base_value
    
    def __str__(self):
        return self.name

class TreasureBox:
    def __init__(self):
        self.treasures = [
            Treasure(
                name = "Norn Stone",
                description = "A cold hard diamond with a high value.",
                base_value = 1000
            ),
            Treasure(
                name = "Opal Eye",
                description = "The stone glistens and glares back at you.",
                base_value = 400
            ),
            Treasure(
                name = "Black Sapphire",
                description = "The darkest stone in the world of wizardry.",                
                base_value = 350
                
            )
        ]