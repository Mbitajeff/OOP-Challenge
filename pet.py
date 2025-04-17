class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  
        self.energy = 5  
        self.happiness = 5 
        self.tricks = [] 
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...!")
        print(f"Hunger decreased to {self.hunger}, happiness increased to {self.happiness}")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...!")
        print(f"Energy increased to {self.energy}")
        
    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!!")
            return
            
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing...")
        print(f"Energy decreased to {self.energy}, happiness increased to {self.happiness}, hunger increased to {self.hunger}")
        
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger} {"sad" if self.hunger <= 3 else 'Tired' if self.hunger >= 7 else 'Gutted'}")
        print(f"Energy: {self.energy} {'Happy' if self.energy >= 7 else 'Sleeping' if self.energy <= 3 else 'Crying'}")
        print(f"Happiness: {self.happiness} {'Smiling' if self.happiness >= 7 else 'Bored' if self.happiness <= 3 else 'Surprised'}")
        if hasattr(self, 'tricks') and self.tricks:
            print(f"Tricks: {self.tricks}")
            
    def train(self, trick):
        if self.energy < 3:
            print(f"{self.name} is too tired to learn new tricks!")
            return
            
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 1)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}!")
        
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")