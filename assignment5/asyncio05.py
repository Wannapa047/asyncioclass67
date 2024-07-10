import asyncio
import random

# coroutine สำหรับทำอาหาร
async def cook_rice():
    cook_time = 1 + random.random()
    await asyncio.sleep(cook_time)
    print(f"Rice is ready in {cook_time:.2f} seconds")
    return "rice", cook_time

async def cook_noodle():
    cook_time = 1 + random.random()
    await asyncio.sleep(cook_time)
    print(f"Noodle is ready in {cook_time:.2f} seconds")
    return "noodle", cook_time

async def cook_curry():
    cook_time = 1 + random.random()
    await asyncio.sleep(cook_time)
    print(f"Curry is ready in {cook_time:.2f} seconds")
    return "curry", cook_time

# main coroutine
async def main():
    # สร้าง tasks สำหรับทำอาหารแต่ละชนิด
    tasks = [
        asyncio.create_task(cook_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]
    # รอให้ tasks เมนูแรกเสร็จสมบูรณ์แล้วนำไปกิน
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first_result = None
    for task in done:
        first_result, cook_time = await task
    for task in pending:
        await task
    
    print(f"Student A eats {first_result}")

# เริ่มโปรแกรม asyncio
asyncio.run(main())
