def extract_file(data):
    needed_infomration = data[-1].split(".")
    file_name = needed_infomration[0]
    extension = needed_infomration[1]
    print(f"File name: {file_name}")
    print(f"Extension: {extension}")


d = input().split("\\")
extract_file(d)
