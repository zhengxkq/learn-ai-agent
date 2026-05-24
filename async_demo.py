import time

def make_tea():
    print("开始烧水...")
    time.sleep(2)
    print("水开了，泡茶完成")

def make_toast():
    print("开始烤面包...")
    time.sleep(2)
    print("面包考好了")

start = time.time()
make_tea()
make_toast()

print(f"总耗时：{time.time() - start:.1f} 秒")