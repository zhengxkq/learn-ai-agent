import asyncio
import time
import httpx

async def fetch_delay(client: httpx.AsyncClient, seconds: int):
    response = await client.get(f"https://httpbin.org/delay/{seconds}")
    print(f"  {seconds} 秒的请求返回了,状态码 {response.status_code}")

async def main():
    start = time.time()
    async with httpx.AsyncClient(timeout=10) as client:
            await fetch_delay(client, 1)
            await fetch_delay(client, 2)
            await fetch_delay(client, 3)
    print(f"总耗时: {time.time() - start:.1f} 秒")

asyncio.run(main())