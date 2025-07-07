import math
def main():
    numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]
    
    llist = list(map(lambda x: x['value'] ** 2, numbers))
    print(llist)

if __name__ == "__main__":
    main()
