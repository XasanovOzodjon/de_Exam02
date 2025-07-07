def main():
    full_name = list(input("Familiya Ism Sharifingizni kiriting: ").title().split())
    if len(full_name) == 3:
        print(f"{full_name[1]} {full_name[2]}, {full_name[0]}")
    else:
        print("Familiya Ism Sharifingizni xato kiritingiz!")



if __name__ == "__main__":
    main()