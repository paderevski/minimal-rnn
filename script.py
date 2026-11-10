import os
import random
import time

def foo(x):
    with open("output.txt", "w") as info:
        for i in range(x):
            print(i)

            # A = np.random.rand(4000,4000)
            # B = np.random.rand(4000,4000)
            # U,S,V = np.linalg.svd(A)
            # A = U @ np.diag(S) @ V.T
            # C = A @ B
            info.write(f"Sleeping Counter: {i}\n")
            time.sleep(1)


if __name__ == "__main__":
    count = os.getenv("LIMIT", random.randint(30, 90))
    print(f"Counting to {count}")
    foo(count)
    print("Done")
