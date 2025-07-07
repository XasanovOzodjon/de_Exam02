inpath = "Input/numbers.txt"
outpath = "Output/output10.txt"

def main():
    try:
        with open(inpath) as f:
            file = f.read()
            try:
                numbers = list(map(int, file.split()))
            except ValueError:
                print("Xatolik, Faylda str mavjud!")
                return
            else:
                numbers.sort()
    
    except FileNotFoundError:
        print("fayl topilmadi")
        return
        
    with open(outpath,"w") as f:
        for i in numbers:
            f.write(f"{i}\n")
        

if __name__ == "__main__":
    main()