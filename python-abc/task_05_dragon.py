#!/usr/bin/env python3
# SwimMixin Mixin
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# FlyMixin Mixin
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon sinifi SwimMixin və FlyMixin-dən irsiyyət alır
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
