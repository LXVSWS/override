def generate_serial(s):
    if len(s) <= 5:
        raise ValueError("Login string must be longer than 5 characters.")

    v4 = (ord(s[3]) ^ 0x1337) + 6221293
    for i in range(len(s)):
        if ord(s[i]) <= 31:
            raise ValueError("Login contains invalid characters.")
        v4 += (v4 ^ ord(s[i])) % 0x539

    return v4

if __name__ == "__main__":
    login = input("Enter login: ")
    try:
        serial = generate_serial(login)
        print(f"Generated serial for login '{login}': {serial}")
    except ValueError as e:
        print(f"Error: {e}")
