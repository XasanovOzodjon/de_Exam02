import json

inpath = "Input/students.json"
outpath = "Output/output12.json"

list = []
dic = {"sorted_names": []}

try:
    with open(inpath) as f:
        text = f.read()
        students = json.loads(text)
except FileNotFoundError:
    print("Xatolik: fayl topilmadi")
    exit()
else:
    for i in students:
        list.append(i["name"])

    list.sort()
    dic.update({"sorted_names": list})
    

with open(outpath, "w") as f:
    json.dump(dic, f, indent=4)
