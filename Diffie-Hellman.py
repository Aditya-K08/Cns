def dh():
    n = int(input('Enter n(prime number): '))
    g = int(input('Enter g(prime number): '))
    print("\n")

    x = int(input('Enter a random number (Private Key for User1): '))
    A = pow(g, x, n)
    print(f"Sent to User2: {A}")
    print("\n")

    y = int(input('Enter a random number (Private Key for User2): '))
    B = pow(g, y, n)
    print(f"Sent to User1: {B}")
    print("\n")

    shared_key_1 = pow(B, x, n)
    shared_key_2 = pow(A, y, n)

    print(f"Shared Key for User1: {shared_key_1}")
    print(f"Shared Key for User2: {shared_key_2}")
    print("\n")

    return


dh()