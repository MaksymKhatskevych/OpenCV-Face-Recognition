import easyocr


def recognition(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path)
    return result

def main():
    file_path = input("Enter path to file: ")
    print(recognition(file_path=file_path))

if __name__ == "__main__":
    main()
