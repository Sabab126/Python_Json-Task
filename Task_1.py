import json


#read file task1
pos_0_file=open('jsonfile/pos_0.png.json','r')
posFileJson =pos_0_file.read()
pos_json_dict=json.loads(posFileJson)


#parse'
list=pos_json_dict["objects"]
print(list)
#list.append(pos10010_json_dict["objects"])
print(list[0].get("id"))
print(list[1].get("id"))

for i in range(len(list)):
    print("address of i ==",i,"is .....")
    print("classId",list[i].get("classId"))
    print("geometryType",list[i].get("geometryType"))
