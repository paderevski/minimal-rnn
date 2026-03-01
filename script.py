def foo(x):
    with open("output.txt", "w") as info:
        for i in range(x):
            info.write(f"Counter: {i}\n")


if __name__ == "__main__":
    foo(1000)
