def main():
    dic = {}
    words = list(input("Kirish: ").split())
    
    for i in words:
        dic.update({i : words.count(i)})
    
    print(dic)


if __name__ == "__main__":
    main()