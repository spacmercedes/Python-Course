# try:
#     file = open("data.txt")
# except FileNotFoundError:
#     file = open("data.txt", "w")
#     file.write("Eggs")
# except KeyError as error_message:
#     print("file does not exsit")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

