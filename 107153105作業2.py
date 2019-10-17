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

    def empty(self, i: int) -> None:
        self._content[self._top] = ' '
        self._top += 1

    @property
    def top(self) -> int:
        return self._top

def dump(abc):
    print(f"堆疊： [", end="")

    for i in range(abc.top):
        print(f" {abc._content[i]}", end="")

    print(f" ] top = {abc.top}");

def isempty(abc):
    if abc._content[1] == None or abc._content[1]==' ' :
        print(f"堆疊有資料嗎?  no")
    else:
        print(f"堆疊有資料嗎?  yes")

def peep(abc):
        print(f"堆疊的第2個位置內容是: {abc._content[1]}")
    
if __name__ == "__main__":
    abc = Stack(10)
    print()
    dump(abc)
    isempty(abc)
    print()
    print()
    print(f"讓我們push一些資料進堆疊。");

    for i in range(3):
        print(f"data pushed: {i}; ", end="");

        abc.push(i)

        dump(abc)
    print()
    print()
    dump(abc)
    isempty(abc)
    peep(abc)
    print()
    print()

    print(f"資料推完了，現在把資料pop出來：")

    for i in range(3):
        print(
            f"data popped: {abc.pop()}; ",
            end=""
        )
        dump(abc)
    print()
    dump(abc)
    print()
    print()
    print(f"讓我們empty堆疊。");

    for i in range(3):
        print(f"data empty: ; ", end="");

        abc.empty(i)

        dump(abc)
    print()
    dump(abc)
    isempty(abc)
    print()
    print()
