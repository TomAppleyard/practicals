"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

code_to_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(code_to_name)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in code_to_name:
        print(f"{state_code:3} is {code_to_name[state_code]:3}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
