import csv

inpath = "Input/grades.csv"
outpath = "Output/output16.txt"

llist = []

try:
    with open(inpath) as f:
        dic = list(csv.DictReader(f))
            
except FileNotFoundError:
    print("Xatolik: fayl topilmadi")
    exit()
else:
    for i in dic:
        if int(i['grade']) == 5:
            llist.append(i['name'])

with open(outpath, "w") as f:
    f.write(f"5 baho olganlar soni: {len(llist)}")
