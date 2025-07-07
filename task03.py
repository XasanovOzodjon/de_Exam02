def calculate_tax(salary):
    """Bu fungsiya Siz o'z oyligingizdan qancha davlatga foiz tulashingizni chiqaradi

    Args:
        salary (float): Oyligiz

    Returns:
        Float: Nechpul foiz tulashiz
    """
    if 5000000 < salary:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    """Bu siz davlatga soliq tulab tozza foydangizni hisoblaydi

    Args:
        salary (float): Oyuligingiz

    Returns:
        float: Tozza foydaingz
    """
    return salary - calculate_tax(salary)


def main():
    salary = 6000000
    tax = calculate_tax(salary)
    net = calculate_net_salary(salary)
    print(f"Soliq: {int(tax):_}")
    print(f"Sof maosh: {int(net):_}")



if __name__ == "__main__":
    main()