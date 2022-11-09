colour_to_code = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff",
                  "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "	#ffbf00", "amethyst": "#9966cc",
                  "apricot": "#fbceb1", "aqua": "#00ffff", "army green": "#4b5320"}
print(colour_to_code)

colour = input("Enter colour: ").lower()
while colour != "":
    print(f"The colour {colour} is {colour_to_code[colour]}")  # could have used get() instead of []
    colour = input("Enter colour: ").lower()
