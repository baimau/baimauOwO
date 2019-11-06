from __future__ import annotations

class Stack:
    def __init__(self, capacity: int):
        self._top = 0
        self._content = [ None for _ in range(capacity) ]
    def pop(self) -> int:
        self._top -= 1

        return self._content[self._top]

    def push(self, i: int) -> None:
        self._content[self._top] = i
        self._top += 1
    @property
    def top(self) -> int:
        return self._top

def count(abc):
    for i in range(2):
        a=abc._content[i]
        b=abc._content[i+1]
        c=a+b
        print()
        print('堆疊第',i+1,'個數字+堆疊第',i+2,'個數字=',c)

def dump(abc):
    print(f"堆疊： [", end="")

    for i in range(abc.top):
        print(f" {abc._content[i]}", end="")

    print(f" ] top = {abc.top}");
    
if __name__ == "__main__":
    abc = Stack(10)
    print()
    dump(abc)
    print()
    print(f"讓我們push一些資料進堆疊。");

    for i in range(3):
        print(f"data pushed: {i}; ", end="");

        abc.push(i)

        dump(abc)

    print()
    dump(abc)
    print()

    print(f"資料推完了，現在把資料pop出來：")

    for i in range(3):
        print(
            f"data popped: {abc.pop()}; ",
            end=""
        )
        dump(abc)
    count(abc)
