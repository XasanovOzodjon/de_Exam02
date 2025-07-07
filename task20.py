import math
def main():
    llist = []
    students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
    ]
    
    for i in students:
        llist.append(i['name'])
    print(min(llist))

if __name__ == "__main__":
    main()
