import sys

def main():
    fridge = sys.argv[1][1:len(sys.argv[1])-1]
    fridge = fridge.split(',')
    ingredients = sys.argv[2][1:len(sys.argv[1])-1]
    ingredients = ingredients.split(',')
    print(validateRecipe(fridge, ingredients))


def validateRecipe(fridge, ingredients):
    check = 0
    for i in ingredients:
        if i in fridge:
            check += 1
            continue
    if check == len(ingredients) :
        return True
    else :
        return False
    
if __name__ == "__main__" :
    main()