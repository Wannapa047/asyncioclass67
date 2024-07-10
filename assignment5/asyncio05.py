import asyncio
import random

# coroutine สำหรับทำอาหาร
async def cook_rice(): #เป็นฟังก์ชันแบบ asynchronous ซึ่งใช้เวลาสุ่มระหว่าง 1 ถึง 11 วินาที (1 + random.random() * 10)
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time) #หยุดการทำงานของ coroutine นี้เป็นระยะเวลาที่สุ่มได้ เพื่อจำลองเวลาที่ใช้ในการทำอาหาร
    print(f"Rice is ready in {cook_time:.2f} seconds")
    return "rice"

async def cook_noodle():
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time)
    print(f"Noodle is ready in {cook_time:.2f} seconds")
    return "noodle"

async def cook_curry():
    cook_time = 1 + random.random() * 10
    await asyncio.sleep(cook_time)
    print(f"Curry is ready in {cook_time:.2f} seconds")
    return "curry"

# main coroutine
async def main():
    # สร้าง tasks สำหรับทำอาหารแต่ละชนิด
    tasks = [
        cook_rice(),
        cook_noodle(),
        cook_curry()
    ]
    # รอให้ tasks เสร็จสมบูรณ์ทีละงาน
    for task in asyncio.as_completed(tasks):
        result = await task
        print(f"Student A eats {result}")
        break  # หยุดหลังจากเมนูแรกเสร็จ

# เริ่มโปรแกรม asyncio
asyncio.run(main()) #รันฟังก์ชัน main ซึ่งเป็นจุดเริ่มต้นของโปรแกรมที่ใช้ asyncio

