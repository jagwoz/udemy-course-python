if __name__ == "__main__":
    file = open('file', 'w')
    try:
        # r - read, w - write, a - append
        # r+ - read and write, w+ - write and read, a+ - append (write only to end) and read
        file.write('text')
    finally:
        file.close()


    with open('file', 'a') as file:
        file.write('text')

    with open('file', 'r', encoding='UTF-8') as file:
        first_line = file.readline()
        next_line = file.readline()
        all_with_slash_ns = file.readlines()
        text_list = file.read().splitlines()
        # for line in file:
        actual_position = file.tell()
        file.seek(0)  # jump to start position
