from recipes import *

print("Welcome to the Team Cookbook!")
print("Loaded recipes:")
for recipe in __all__:
    print("-", recipe)
