car = {"brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
print(car['brand'])
print(car)
x = car.keys()
print(x)
#เพิ่มค่าในdic
car["color"] ="white"
print(car)
#แก้ค่าในdic
car["color"] ="red"
print(car)
#การupdate dic
car.update({"light": "blue"})
print(car)
#ลบค่าในdic
car.pop("light")
print(car)
del car["color"]
print(car)
#เพิ่มค่าในdicแบบ list
car.update({"part": ["body","wheel","light"]})
print(car)
#เพิ่มค่าdic แบบ Nested dic
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child3'])
#นายณรงค์ฤทธิ์ ว่องไว เลขที่34 ชั้น ม.6/14