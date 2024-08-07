import time
import asyncio

class Coffee:
    def __init__(self):
        self.name = "Coffee"
    def __str__(self):
        return self.name

class Egg:
    def __init__(self):
        self.name = "Egg"
    def __str__(self):
        return self.name

class Bacon:
    def __init__(self):
        self.name = "Bacon"
    def __str__(self):
        return self.name

class Toast:
    def __init__(self):
        self.name = "Toast"
    def __str__(self):
        return self.name

class Juice:
    def __init__(self):
        self.name = "Juice"
    def __str__(self):
        return self.name

async def PourCoffee():
    print(f"{time.ctime()} – Begin pour coffee...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} – Finish pour coffee...")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} – Begin apply butter...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} – Finish apply butter...")

async def FryEggs(eggs):
    print(f"{time.ctime()} – Begin fry eggs...")
    print(f"{time.ctime()} – Heat pan to fry eggs")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} – Frying", egg+1, "eggs")
        await asyncio.sleep(1)
    print(f"{time.ctime()} – Finish fry eggs...")
    print(f"{time.ctime()} – >>>>>>>>> Fry eggs are ready...")
    return Egg()

async def FryBacon():
    print(f"{time.ctime()} – Begin fry bacon...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} – Finish fry bacon...")
    print(f"{time.ctime()} – >>>>>>>>> Fry bacon is ready...")
    return Bacon()

async def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} – Toasting bread", slice + 1)
        await asyncio.sleep(1)
        print(f"{time.ctime()} – Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} – Toast", slice + 1, "ready")
    print(f"{time.ctime()} – >>>>>>>>> Toast are ready\n")
    return Toast()

async def PourJuice():
    print(f"{time.ctime()} – Begin pour juice...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} – Finish pour juice...")
    return Juice()

async def main():
    coffee = await PourCoffee()
    print(f"{time.ctime()} – >>>>>>>>> {coffee} is ready\n")
    
    fry_eggs_task = FryEggs(2)
    fry_bacon_task = FryBacon()
    toast_bread_task = ToastBread(2)

    eggs, bacon, toast = await asyncio.gather(fry_eggs_task, fry_bacon_task, toast_bread_task)
    
    print(f"{time.ctime()} – >>>>>>>>> Nearly to finished...\n")
    juice = await PourJuice()
    print(f"{time.ctime()} – >>>>>>>>> Breakfast is ready: {coffee}, {eggs}, {bacon}, {toast}, {juice}\n")

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} – Breakfast cooked in ", elapsed, "seconds.")