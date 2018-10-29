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
class OrderedList:
    def __init__(self):
        # Ініціалізація пустого списку
        self.head = None

    def isEmpty(self):
        # Перевірка на наявність значень у списку
        return self.head is None

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

    def search(self, item):
        # Цикл проходить по списку або до кінця, або поки значення не стане більшим за шукане, і виводить значення
        # булевої змінної.
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    break
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        # Робить те ж, що і search, а потім маркер позиції поточного елементу переміщається вперед, а на його місце
        # вставляється item.
        current = self.head
        previous = None
        while current is not None:
            if current.getData() > item:
                break
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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