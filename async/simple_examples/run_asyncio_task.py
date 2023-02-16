import asyncio
from datetime import datetime
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'Task1'))

    task2 = asyncio.create_task(
        say_after(2, 'Task2'))

    task3 = asyncio.create_task(
        say_after(2, 'Task3'))

    task4 = asyncio.create_task(
        say_after(2, 'Task4'))

    start_time = datetime.utcnow()
    print(f"started at {start_time.strftime('%T.%f')}")

    await task1
    await task2
    await task3
    await task4

    end_time = datetime.utcnow()
    work_time_seconds = (end_time-start_time).total_seconds()

    print(f"Finished at {end_time.strftime('%T.%f')}")
    print(f"Worked for ~ {work_time_seconds} seconds")

asyncio.run(main())
