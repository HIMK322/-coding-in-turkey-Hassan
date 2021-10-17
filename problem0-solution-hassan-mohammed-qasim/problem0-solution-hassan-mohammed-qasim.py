import sys

def whereIsMyFood(fridge, item):
    for i in range(len(fridge)):
        if fridge[i] == item:
            return i
    return -1

def main() :
    fridge = sys.argv[1][1:len(sys.argv[1])-1]
    fridge = fridge.split(',')
    postion = whereIsMyFood( fridge,sys.argv[2])
    print(postion)

if __name__ == "__main__":
    main()
