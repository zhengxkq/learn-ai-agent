import asyncio
import httpx


async def fetch_ip():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/ip")
        data = response.json()
        print("我的出口IP :", data["origin"])

asyncio.run(fetch_ip())