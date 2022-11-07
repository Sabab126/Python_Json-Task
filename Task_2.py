import json
#read file

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

# After Merge



myjsonfile=open('jsonfile/mergefile.png.json','r')
merged_file=myjsonfile.read()


merged_file=merged_file.replace("Vehicle","car")
merged_file=merged_file.replace("License Plate","number")


#print(merged_file)
#dict_json=json.loads(merged_file)






file4 = open('jsonfile/new replaced word.json', 'a')
file4.write(json.dumps(merged_file))

print(type(merged_file))
print(len(merged_file))


print(merged_file)


#list=dict_json['objects']
#print("newwww classTitle 1 ", list[0].get("classTitle"))
#print("newwww classTitle 2 ", list[1].get("classTitle"))


#print("replaced word is ",dict_json.get("classTitle"))
#print("replaced word is ",dict_json.get("classTitle"))
#print(type(dict_json))







#print(list[2])












