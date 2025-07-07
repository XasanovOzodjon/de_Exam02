def add(a, b):
    """
    Ikkta sonni qushuvchi fungingsiya.

    Parametrlar:
    a (int yoki float) — birinchi son
    b (int yoki float) — ikkinchi son

    Return:
    a + b natijasi
    """
    return a + b

def subtract(a, b):
    """
    Ikkta sonni ayiruvchi fungingsiya

    Parametrlar:
    a (int yoki float) — birinchi son
    b (int yoki float) — ikkinchi son

    Return:
    a - b natijasi
    """
    return a - b

def multiply(a, b):
    """
    Ikkta sonni kupaytiruvchi fungingsiya.

    Parametrlar:
    a (int yoki float) — birinchi son
    b (int yoki float) — ikkinchi son

    Return:
    a * b natijasi
    """
    return a * b

def divide(a, b):
    """
    Ikkta sonni bo'luvchi fungingsiya

    Parametrlar:
    a (int yoki float) — birinchi son (bo‘linuvchi)
    b (int yoki float) — ikkinchi son (bo‘luvchi)

    Return:
    a / b natijasi
    """
    return a / b




def main() -> None:
    try:
        amallar = ['*', '/', '+', '-']
        number1 = int(input("1-son: "))
        amal = input("Amal: ")
        number2 = int(input("2-son: "))
        
        if amal not in amallar:
            raise(Exception("Error"))
        if amal == "/" and number2 == 0:
            raise(Exception(ZeroDivisionError))
        
    except ValueError:
        print("Siz son kiritmadingiz")
        
    except Exception:
        print("Siz amalni xato kiritingiz")
        
    except ZeroDivisionError:
        print("Sonni 0 ga bo'lib bulmaydi")
    
    else:
        result = 0
        
        if amal == "+":
            result = add(number1, number2)
        elif amal == "-":
            result = subtract(number1, number2)
        elif amal == "*":
            result = multiply(number1, number2)
        elif amal == "/":
            result = divide(number1, number2)
            
        print(f"result: {result}")
    



if __name__ == "__main__":
    main()