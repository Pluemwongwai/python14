#การแสดงค่าในlist
from operator import truediv


fruits = ["apple","banana","cherry","watermelon","blurburry"]
print(fruits[1])
#การเปลี่ยนค่าในlist
fruits[1] = "blackcurrant"
print(fruits[1])
#การเปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:3] = ["kiwi","mango","pineapple"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("orange")
print(fruits)
fruits.insert(1,"orange")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon") 
fruits.pop(1)
print(fruits)
#del fruits
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#นายณรงค์ฤทธิ์ ว่องไว เลขที่34 ชั้น ม.6/14