inpath = "Input/numbers.txt"
outpath = "Output/output09.txt"

def main():
    max_num = 0
    try:
        with open(inpath) as f:
            file = f.read()
            try:
                numbers = list(map(int, file.split()))
            except ValueError:
                print("Xatolik, Faylda str mavjud!")
                return
            else:
                max_num = max(numbers)
    
    except FileNotFoundError:
        print("fayl topilmadi")
        return
        
    with open(outpath,"w") as f:
        f.write(f"Eng katta son: {max_num}")
        

if __name__ == "__main__":
    main()