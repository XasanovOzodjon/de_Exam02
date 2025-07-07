def main():
    llist = []
    students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
    
    items = list(students.values())
    average_score = sum(items) / len(items)
    
    
    for key, value in students.items():
        if value > average_score:
            llist.append(key)
    
    
    print(f"O‘rtacha baho: {average_score}")
    print(f"{average_score} dan yuqorilar: {', '.join(llist)}")
    
    

if __name__ == "__main__":
    main()