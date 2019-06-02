class Stack:
    def __init__(self):
        self.list = []

    def empty(self):
        if self.list == []:
            print("Стек пустий")  # Перевіряє чи стек пустий

    def plus(self, item):
        self.list.append(item)

    def pop(self):    #Вертає останній елемент  і видаляє зі стеку

        print("Видаляемо: ", self.list.pop())

    def peek(self):
        return self.list[len(self.list) - 1]

    def size(self):
        if self.list == []:
            pass
        else:
            print("Стек має довжину ", len(self.list))

    def show(self):
        if self.list == []:
            pass
        else:
            print ("Отримали такий стек: ",self.list)


s = Stack()
st = []
n = int(input("Введіть кількість елементів: "))

print("Введіть елементи:")
for i in range(n):
    el = int(input())
    st.append(el)
for i in st:
    s.plus(i)
s.show()
s.pop()
s.size()
s.pop()
s.pop()
s.size()
s.show()
s.empty()

