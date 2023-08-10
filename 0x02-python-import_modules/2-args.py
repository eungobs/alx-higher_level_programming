#!user/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        args = "arguments"
    elif argc == 1:
        args = "argument"
    else:
        args = "arguments"

    print(f"Number of {args}: {argc}:", end="")
    if argc == 0:
        print(".")
    else:
        print()
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
