# function
def tong(a, b):
    return a + b

def greeting(name):
    print(f"Hello {name}")

def change(n):
    n *= 2


def infor(name, job = "grab"):
    print(name, job)

# code để chạy chương trình (do python ko có hàm main nên viết thêm để tường minh)
if __name__ == '__main__':
    #code
    x, y = map(int, input().split())
    print(tong(x, y))

    a = 1000
    change(a)
    print(a) # => pass by value, not pass by reference

    infor('Nam') #default argument: job = "grab"
    infor('Tuan', 'dev') 
    