# 제대로 동작하는 예제

class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')


obj1 = MyClass('obj1')
obj2 = MyClass('obj2')

obj1 = None  # obj1에 대한 참조를 제거하여 도달 불가능하게 만듦

# 출력:
# obj1 객체가 제거되었습니다.


# 메모리 누수가 발생하는 예제

class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')


def create_objects():
    obj1 = MyClass('obj1')
    obj2 = MyClass('obj2')
    obj1.other = obj2  # obj1이 obj2를 참조하도록 함
    obj2.other = obj1  # obj2가 obj1을 참조하도록 함


create_objects()
# 출력