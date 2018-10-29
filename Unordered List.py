# Клас вузла
class Node:
    def __init__(self, initdata, position=0):
        # Ініціалізація значення вузла
        self.data = initdata
        # Ініціалізація наступного значення як None
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        # Перезапис значення вузла
        self.data = newdata

    def setNext(self, newnext):
        # Перезапис наступного значення вузла
        self.next = newnext


# Невпорядкований список.
class UnorderedList:
    def __init__(self):
        # Ініціалізація пустого списку
        self.head = None

    def isEmpty(self):
        # Перевірка на наявність значень у списку
        return self.head is None

    def add(self, item):
        # Ініціалізація вузла
        temp = Node(item)
        # Робить перше значення у списку наступним
        temp.setNext(self.head)
        # Присвоює голові значення item
        self.head = temp

    def size(self):
        # Ініціалізація зовнішьного посилання і каунтера,
        # переміщається по списку поки не дійде кінця,
        # в кінці виводить значення каунтера.
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        # Ініціалізація зовнішнього посилання і булевої змінної.
        # Цикл проходить по списку до кінця і виводить значення булевої змінної.
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        # Ініціалізація двох зовнішніх посилань і булевої змінної.
        # previous на одне значення позаду current.
        # Поки не знайдеться item, переміщати current i previous на значення вперед
        # Коли значення знайдеться: якщо воно перше, перемістити голову на значення вперед, видаляючи таким чином
        # перше значення; якщо десь всередині, перемістити маркер значення на наступне значення, видаляючи таким чином
        # це значення.
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        elif not found:
            return False
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        # Проходить по списку, поки не дійде до кінця. Надає значення item наступному, пустому значенню у списку.
        # Якщо список пустий, надає його голові.
        current = self.head
        if current:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)

    def index(self, item):
        # Проходить по списку, при переході до кожного елементу індекс +1. Якщо item немає, index == None.
        index = 0
        current = self.head
        found = False
        while current is not None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

    def insert(self, index, item):
        # Проходить по списку черв'яком. Якщо елементу позаду немає, item вставляється в голову. Інакше маркер позиції
        # поточного елементу переміщається вперед, а на його місце вставляється item.
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        found = False
        if index > self.size():
            raise IndexError('List Index Out Of Range')
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def pop(self, index=None):
        # Проходить по списку, коли доходить до позиції, повертає її значення і переміщає маркер вперед. Якщо позиції
        # немає, повертає останній елемент.
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.getNext() is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        return current.getData()