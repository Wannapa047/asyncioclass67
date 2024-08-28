from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_time = time.time()  # Start timing the producer
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time = time.time()  # End timing the producer
    print('Producer: Done')
    print(f"Producer Time taken: {end_time - start_time:.2f} seconds")

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    start_time = time.time()  # Start timing the consumer
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    end_time = time.time()  # End timing the consumer
    print('Consumer: Done')
    print(f"Consumer Time taken: {end_time - start_time:.2f} seconds")

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())
