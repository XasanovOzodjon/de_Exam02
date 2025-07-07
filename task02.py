menu = """
-----------Menu----------
1 - Pul qo'yish(deposit)
2 - Pul chiqarish(withdraw)
3 - Balansni ko'rish
4 - Dasturdan chiqish(exit)
"""

def deposit(balance, amount):
    """Bu hisobingizga depazit quyish uchun fungsiya

    Args:
        balance (float): Sizning bank hisobingiz
        amount (float): Qancha pul kiritmoqchiligingiz

    Returns:
        Float: Yangilangan hisobingiz
    """
    return balance + amount

def withdraw(balance, amount):
    """Bu hisobingizdan pul chiqaruvchi fungsiya

    Args:
        balance (float): Sizning bank hisobingiz
        amount (float): Qancha pul chiqarmoqchi bulgan summa

    Returns:
        Float: Yangilangan hisobingiz
    """
    
    if balance < amount:
        print("Xisobingizda mablag' yetarli emas")
        return balance
    else:
        return balance - amount

def check_balance(balance):
    """Hisobingizda qancha mablag bor tekshiruvchi fungsiya

    Args:
        balance (float): Hisob raqamingiz
    """
    print(f"balance: {balance} so'm")




def main() -> None:
    balance = 0
    while True:
        print(menu)
        choise = input(">>>")

        if choise == "1":
            try:
                amount = float(input("Qancha pul kiritayapsiz: "))
                
                if amount < 0:
                    raise(Exception("Xato"))
                balance = deposit(balance, amount)
                
            except:
                print("Sonni xato kiritingiz")
    
        
        elif choise == "2":
            try:
                amount = float(input("Qancha pul chiqarmoqchisiz: "))
                
                if amount < 0:
                    raise(Exception("Xato"))
                balance = withdraw(balance, amount)
                
            except:
                print("Sonni xato kiritingiz")
                
        elif choise == "3":
            check_balance(balance)
        
        elif choise == "4":
            break
        else:
            print("Xato amal kiritingiz")





if __name__ == "__main__":
    main()