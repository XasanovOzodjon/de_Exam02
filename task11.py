import json

inpath = "Input/students.json"
outpath = "Output/output11.json"

dic = {"count": 0}

try:
    with open(inpath) as f:
        text = f.read()
        students = json.loads(text)
        dic["count"] = len(students)
except FileNotFoundError:
    print("Xatolik: fayl topilmadi")
    exit()

with open(outpath, "w") as f:
    json.dump(dic, f, indent=4)
