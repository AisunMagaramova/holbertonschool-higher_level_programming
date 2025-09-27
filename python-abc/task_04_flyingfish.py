#!/usr/bin/env python3
# Fish sinifi
class Fish:
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")


# Bird sinifi
class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")


# FlyingFish sinifi - Fish və Bird siniflərindən irsiyyət alır
class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")
    
    def fly(self):
        print("The flying fish is soaring!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Test hissəsi - FlyingFish obyektini yaradırıq və metodları çağırırıq
if __name__ == "__main__":
    flying_fish = FlyingFish()  # FlyingFish obyektini yaradırıq
    flying_fish.swim()          # swim() metodunu ça_
