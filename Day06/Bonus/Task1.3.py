def make_custom_sandwich(ingredients):
    if not any(x in ingredients for x in["Ham","Tomato"]):
        print("Error: need ham or tomato!")
        return
    
    if ingredients.count("bread")<2:
        print("Error: A sandwich needs top and bottom bread!")
        return

    for item in ingredients:
        print(item)


make_custom_sandwich(["bread","lettuce","tomato","ham","bread"])
make_custom_sandwich(["bread","lettuce","bread"])