import time
import asyncio
from asyncio import Queue

# Product and Customer classes remain unchanged
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# Updated checkout_customer function with time adjustment
async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_take = {"id": cashier_number, "time": 0, "customer": 0}
    while not queue.empty():
        customer: Customer = await queue.get()
        cashier_take['customer'] += 1
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")

        for product in customer.products:
            # Adjust checkout time conditionally
            if cashier_number == 2:
                product_take_time = 0.1
            else:
                product_take_time = round(product.checkout_time + (0.1 * cashier_number), ndigits=2)

            print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} for {product_take_time} secs")
            await asyncio.sleep(product_take_time)
            cashier_take["time"] += product_take_time

        print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} "
              f"in {round(cashier_take['time'], ndigits=2)} secs")

        queue.task_done()
    return cashier_take

# Customer generation function remains unchanged
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# Customer generation function remains unchanged
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id) for the_id in range(customer_count, customer_count + customers)]
        for customer in customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")

        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

# Use asyncio.gather to run tasks concurrently
async def main():
    CUSTOMER = 10
    QUEUE = 5
    CASHIERS = 5
    customer_queue = Queue(QUEUE)
    customers_start_time = time.perf_counter()

    # Start the producer task
    customer_producer = asyncio.create_task(customer_generation(customer_queue, CUSTOMER))
    
    # Start the cashier tasks
    cashier_tasks = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(CASHIERS)]
    
    # Wait for all tasks to complete
    await asyncio.gather(customer_producer, *cashier_tasks)
    
    print(20 * '-')
    for task in cashier_tasks:
        cashier = task.result()
        print(f"The Cashier_{cashier['id']} took {cashier['customer']} customers "
              f"total {round(cashier['time'], ndigits=2)} secs.")

    print(f"\nThe supermarket process finished {CUSTOMER} customers "
          f"in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")
    
if __name__ == "__main__":
    asyncio.run(main())
