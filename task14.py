import json

inpath = "Input/students.json"
outpath = "Output/output14.json"

list = []
dic = {"a_names": []}

try:
    with open(inpath) as f:
        text = f.read()
        students = json.loads(text)
except FileNotFoundError:
    print("Xatolik: fayl topilmadi")
    exit()
else:
    for i in students:
        if i["name"].lower().startswith("a"):
            list.append(i["name"])

    list.sort()
    dic.update({"a_names": list})
    

with open(outpath, "w") as f:
    json.dump(dic, f, indent=4)
