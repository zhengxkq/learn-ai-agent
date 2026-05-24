
nums = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]
positives = [x for x in nums if x > 2]

print("doubled:", doubled)
print("positives:", positives)


user = {"name": "haydon", "age": 30}
print("name", user["name"])
print("email:", user.get("email", "N/A"))

val = None
if val is None:
    print("val 是空")

name = "haydon"
age = user["age"]

print(f"Hello {name}, age {age}");

x = 10
label = "big" if x > 5 else "small"

print(f"x={x}, label={label}");


    
