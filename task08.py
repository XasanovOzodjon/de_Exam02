inpath = "Input/numbers.txt"
outpath = "Output/output08.txt"

def main():
    summa = 0
    try:
        with open(inpath) as f:
            file = f.read()
            try:
                numbers = list(map(int, file.split()))
            except ValueError:
                print("Xatolik, Faylda str mavjud!")
            else:
                summa = sum(numbers)
    
    except FileNotFoundError:
        print("fayl topilmadi")
        return
        
    with open(outpath,"w") as f:
        f.write(f"Yig'indi: {summa}")
        

if __name__ == "__main__":
    main()