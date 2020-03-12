d={'michael':95,"john":100}
print(d["michael"])
d["john"]=80
if "tracy" in d:
    print("tracy")
print(d.get("tracy",-1))

d.pop("michaed")#刪除
print(d)
e={}#空