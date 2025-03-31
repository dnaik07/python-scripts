def calculate_sum():
    total = 0
    print("SUM OF NUMBERS FROM 1 TO 50")
    print("---------------------------")
    
    for num in range(1, 51):
        total += num
    
    print(f"\nThe sum of all integers from 1 to 50 is: {total}")

if __name__ == "__main__":
    calculate_sum()