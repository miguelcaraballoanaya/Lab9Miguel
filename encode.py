def encode():
    password = str(input("Please enter your password to encode: "))
    encoded = []
    for char in password:
        if char == "1":
            encoded.append(4)
        elif char == "2":
            encoded.append(5)
        elif char == "3":
            encoded.append(6)
        elif char == "4":
            encoded.append(7)
        elif char == "5":
            encoded.append(8)
        elif char == "6":
            encoded.append(9)
        elif char == "7":
            encoded.append(0)
        elif char == "8":
            encoded.append(1)
        elif char == "9":
            encoded.append(2)
        elif char == "0":
            encoded.append(3)
    encoded_password = ""
    for i in range(len(encoded)):
        encoded_password += encoded[i]