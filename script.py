import os
import random


def foo(x):
    with open("output.txt", "w") as info:
        for i in range(x):
            info.write(f"Counter: {i}\n")


if __name__ == "__main__":
    count = os.getenv("LIMIT", random.randint(500, 1000))
    print(f"Counting to {count}")
    foo(count)
    print("Done")
