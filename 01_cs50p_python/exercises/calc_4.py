def main():
    x = int(input("What is x? "))
    print(f"{x} squared is {square(x)}")

def square(n):
    return n * n

main()