from enum import Enum, IntEnum


def print2(text):
    print(f"""Hello,
{text},
========""")


def funcWithFunc(func=print2):
    func("Jacob")


def threeStrings(str1, str2, str3):
    print(str1, str3, str2, sep="_")


def multiArguments(*args):
    print(args)
    threeStrings(*args)


def multiKeyArguments(**args):
    for key, value in args.items():
        print(key, value, sep=" -> ")


if __name__ == "__main__":
    funcWithFunc()
    funcWithFunc(print2)
    multiArguments("arg1", "arg2", "arg3")
    multiKeyArguments(key1="key1", key2="key2")





