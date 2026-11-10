import os
import random
import time
import numpy as np

def foo(x):
    with open("output.txt", "w") as info:
        for i in range(x):
            print(i)

            A = np.random.rand(9000,9000)
            B = np.random.rand(9000,9000)
            # U,S,V = np.linalg.svd(A)
            # A = U @ np.diag(S) @ V.T
            C = A @ B
            info.write(f"Sleeping Counter: {i}\n")
            time.sleep(1)


if __name__ == "__main__":
    try:
        count = min(int(os.getenv("LIMIT", random.randint(30, 90))),3600)
    except ValueError:
        count = 60
    print(f"Counting to {count}")
    foo(count)
    print("Done")
