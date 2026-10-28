import os
import random
import statsmodels.api as sm
import numpy as np

def foo(x):
    with open("output.txt", "w") as info:
        for i in range(x):
            print(i)

            A = np.random.rand(4000,4000)
            B = np.random.rand(4000,4000)
            U,S,V = np.linalg.svd(A)
            A = U @ S @ V.T
            C = A @ B
            info.write(f"Counter: {i}\n")


if __name__ == "__main__":
    count = os.getenv("LIMIT", random.randint(500, 1000))
    print(f"Counting to {count}")
    foo(count)
    print("Done")
