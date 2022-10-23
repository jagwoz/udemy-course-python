from enum import Enum, IntEnum


def print2(text):
    print(f"""Hello,
{text},
========""")


def funcWithFunc(func=print2):
    func("Jacob")


if __name__ == "__main__":
    funcWithFunc()
    funcWithFunc(print2)





