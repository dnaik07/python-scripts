def check_even_odd():
    print("EVEN/ODD CHECKER")
    print("----------------")
    
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"\n{num} is an EVEN number")
        else:
            print(f"\n{num} is an ODD number")
    except ValueError:
        print("\nError: Please enter a valid integer!")

if __name__ == "__main__":
    check_even_odd()