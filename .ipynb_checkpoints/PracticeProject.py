# PracticeProject.py

# Code to practice using Git

def main():
    """Calculate the nth Fibonacci number"""
    # 1, 1, 2, 3, 5, 8, 13, 21, 34...

    # Ask use for which fib number they want
    num = int(input("Which fib number do you want"))

    # Start at n = 1 -> 1
    #          n = 2 -> 1
    #          n = 3 -> 2
    if num == 1 or num == 2:
        print(f"The {num}st/nd Fibonacci number is 1")

if __name__ == "__main__":
    main()
