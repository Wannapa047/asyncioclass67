import asyncio
import random

# coroutine สำหรับทำอาหาร
async def cook_rice():
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time)
    print(f"Rice is ready in {cook_time:.2f} seconds")
    return ("rice", cook_time)

async def cook_noodle():
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time)
    print(f"Noodle is ready in {cook_time:.2f} seconds")
    return ("noodle", cook_time)

async def cook_curry():
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time)
    print(f"Curry is ready in {cook_time:.2f} seconds")
    return ("curry", cook_time)

# main coroutine
async def main():
    # สร้าง tasks สำหรับทำอาหารแต่ละชนิด
    tasks = [
        cook_rice(),
        cook_noodle(),
        cook_curry()
    ]
    # รอให้ tasks เสร็จสมบูรณ์ทีละงาน
    results = await asyncio.gather(*tasks)

    
    first_done = min(results, key=lambda x: x[1])
    print(f"Student A eats {first_done[0]} which was ready in {first_done[1]:.2f} seconds.")

# เริ่มโปรแกรม asyncio
asyncio.run(main())
