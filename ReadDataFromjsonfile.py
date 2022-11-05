import json

#read file task1
myjsonfile=open('jsonfile/pos_0.png.json','r')
jsondata =myjsonfile.read()

#parse
print(type(jsondata))
obj=json.loads(jsondata)
#print(str(obj['objects']))
print(type(obj))

list=obj['objects']
#print(list)
print(list[0])
print(list[1])
print(len(list))


for i in range(len(list)):
    print("address of i ==",i,"is .....")
    print("classId",list[i].get("classId"))
    print("geometryType",list[i].get("geometryType"))



###TASK 2

Posjsondata1=Posjsondata2=Posjsondata3=""

file1 = open('jsonfile/pos_0.png.json', 'r')
Posjsondata1 = file1.read()

file2 = open('jsonfile/pos_10010.png.json', 'r')
Posjsondata2 = file2.read()

file3 = open('jsonfile/pos_10492.png.json', 'r')
Posjsondata3 = file3.read()


Posjsondata1+="\n"
Posjsondata1+="\n"
Posjsondata1+=Posjsondata2
Posjsondata1+="\n"
Posjsondata1+="\n"
Posjsondata1+=Posjsondata3


file4 = open('jsonfile/mergefile.png.json', 'a')
file4.write(Posjsondata1)
file4.close()








