def read_2_characters(file):
    while True:
        result = file.read(2)
        if not result:
            break
        yield result


def read_file():
    file_name = 'vc_lines.txt'
    try:
        with open(file_name) as f:
            for lines in read_2_characters(f):
                print(lines)

    except FileNotFoundError as e:
        print("Could not find file: ", e)
        raise FileNotFoundError("Could not find file in read_file")


read_file()
