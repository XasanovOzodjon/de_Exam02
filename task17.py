def main():
    numbers = [
        {'value': -5}, 
        {'value': 10}, 
        {'value': -1}, 
        {'value': 7}
    ]
    
    llist = list(filter(lambda x: x['value'] > 0, numbers))
    print(llist)

if __name__ == "__main__":
    main()
