colour_to_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "	#ffbf00", "Amethyst": "#9966cc",
                  "Apricot": "#fbceb1", "Aqua": "#00ffff", "Army Green": "#4b5320"}
print(colour_to_code)

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in colour_to_code:
        print(f"{colour} is {colour_to_code[colour]}")
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
