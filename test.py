import json
#read file


myjsonfile=open('jsonfile/mergefile.png.json','r')
merged_file=myjsonfile.read()


merged_file=merged_file.replace("Vehicle","car")
merged_file=merged_file.replace("License Plate","number")
#print(merged_file)
dict_json=json.loads(merged_file)






#dict_json=json.load(merged_file)


file4 = open('jsonfile/new replaced word.json', 'a')
file4.write(json.dumps(dict_json))

print(type(merged_file))
print(len(merged_file))


print(merged_file)
list=dict_json['objects']
print("newwww classTitle 1 ", list[0].get("classTitle"))
print("newwww classTitle 2 ", list[1].get("classTitle"))


#print("replaced word is ",dict_json.get("classTitle"))
#print("replaced word is ",dict_json.get("classTitle"))
#print(type(dict_json))







#print(list[2])












