d = {"tree": "wood", "flower": "petal", "earth": "water", 101: [4, 6, 8]}

# TODO: INSERT CODE HERE TO REPLACE "wood" WITH "leaves"
d["tree"] = "leaves"

# TODO: INSERT CODE HERE TO ADD THE PAIR "monty": "python"
d["monty"] = "python"

# TODO: INSERT CODE HERE TO FIRST CHECK IF "earth" IS A KEY,
# AND IF IT IS THEN PRINT THE VALUE IT MAPS TO
if "earth" in d:
    print(d["earth"])

# TODO: INSERT CODE HERE TO PRINT A LIST/GENERATOR OF ALL THE PAIRS IN d
print(d.items())

print(d) # check all your work
