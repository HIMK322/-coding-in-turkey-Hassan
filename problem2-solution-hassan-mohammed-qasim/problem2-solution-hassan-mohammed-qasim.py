import sys
import json

def main():
    with open(sys.argv[1]) as json_file:
        data = json.load(json_file) 

    fridge = data["fridge"]
    ingredients =data["ingredients"]
    print(validateRecipeWithQuantity(fridge, ingredients))


def validateRecipeWithQuantity(fridge, ingredients) :
    check = 0
    for i in ingredients:
        if i  in fridge.keys():
            if fridge[i] >= ingredients[i]:
                check += 1
    if check == len(ingredients):
        return True
    return False


if __name__ == "__main__":
    main()


