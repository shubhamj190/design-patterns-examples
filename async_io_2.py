import asyncio
import json
import requests
import time

# creating a normal http_req


def http_req(url: str) -> int:
    resp = requests.get(url)
    return resp.status_code


async def http_req_async(url: str) -> str:
    return await asyncio.to_thread(http_req, url)


async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Counter started")
    for i in range(until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}: Was asleep for {now - last}s")


# async def main():
#     task = asyncio.create_task(counter())
#     status_code = await http_req_async("https://sales.ufaber.com/")
#     print("Got http response")
#     await task


async def main():
    status_code, _ = await asyncio.gather(http_req_async('https://sales.ufaber.com/'), counter())
    print("got all the responses")

if __name__ == "__main__":
    asyncio.run(main())
