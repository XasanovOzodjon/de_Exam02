import json

inpath = "Input/students.json"
outpath = "Output/output13.json"

list = []
dic = {"long_names": []}

try:
    with open(inpath) as f:
        text = f.read()
        students = json.loads(text)
except FileNotFoundError:
    print("Xatolik: fayl topilmadi")
    exit()
else:
    for i in students:
        if len(i["name"]) > 5:
            list.append(i["name"])

    list.sort()
    dic.update({"long_names": list})
    

with open(outpath, "w") as f:
    json.dump(dic, f, indent=4)
