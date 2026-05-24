def add(a: int, b: int) -> int:
    return a + b;

print(add(1, 2))
print(add(10, 20))



def greet(name: str, age: int | None = None) -> str:
    if age is None:
        return f"Hello {name}"
    return f"Hello {name}, age {age}"

print(greet("haydon"))
print(greet("haydon", 30))

def process(items: list[str]) -> dict[str, int]:
    return {item: len(item)  for item in items}

print(process(["apple", "banana", "cherry"]))