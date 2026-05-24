import asyncio
import time


async def make_tea():
    print("开始烧水")
    await asyncio.sleep(2)
    print("水开了，泡茶完成")

async def make_toast():
    print("开始烤面包")
    await asyncio.sleep(2)
    print("面包烤好了")

async def main():
    start = time.time()
    await asyncio.gather(make_tea(), make_toast())
    print(f"总耗时： {time.time() - start:.1f} 秒")

asyncio.run(main())

# result = make_tea()
# print("直接调用 make_tea()得到：", result)