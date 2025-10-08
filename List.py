# list có thứ tự
# access by index
# có thể lưu object thuộc các kiểu dữ liệu khác nhau

a = [1, 2, 3]
print(type(a))

s = '28tech' # iterable
a = list(s)
print(a)

b = list(range(20))
print(b)

# in ra size cua list
print(len(b))

# duyệt thông qua chỉ số
for i in range(len(a)):
    print(a[i], end=' ')
print()

for i in range(-1, len(a)*(-1) - 1, -1):
    print(a[i], end=' ')
print()

# duyệt bằng for each
for c in a:
    print(c, end=' ')
print()

# thêm 1 phần tử vào cuối
a.append(19)
a.append(1000)
print(a)

# chèn phần tử
a.insert(1, 20)
print(a)

# xóa phần tử cuối cùng
a.pop()
print(a)

a.pop(1)
print(a)

# remove() xóa bằng giá trị, pop() xóa bằng index
# clear() xóa cả mảng

# Nhân bản
c = a * 2
print(c)

# (if 5 in a) tương đương với duyệt mảng O(n)

# hàm count() đếm số lần xuất hiện của 1 phần tử trong list
a = [1,2,3,1,2,1,1]
print(a.count(1))

# hàm index() trả vể chỉ số đầu tiên của 1 phần tử trong list
print(a.index(2))

# reverse() để lật ngược 1 list
# sort() để sắp xếp các phần tử trong list (timsort O(nlogn))
