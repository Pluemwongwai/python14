#คำสั่งหาพื้นที่สี่เหลี่ยม
def square(width,height):
    return width*height
ans1 = square(5,5)
#คำสั่งหาพื้นที่สามเหลี่ยม
def triangle(base,height):
    return 1/2*base*height
ans2 = triangle(6,5)
#คำสั่งหาพื้นที่วงกลม
def circle(radius):
    return 3.14*(radius*radius)
ans3 = circle(7)
print(ans1)
print(ans2)      
print(ans3)
#ณรงค์ฤทธิ์ ว่องไว ม.6/14 เลขที่ 34