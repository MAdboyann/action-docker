# pass_fail.py

def main():
    try:
        percentage = float(input("Enter your percentage: "))
        if percentage < 0 or percentage > 100:
            print("Invalid percentage! Enter a value between 0 and 100.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    if percentage >= 40:
        print("Congratulations! You Passed ✅")
    else:
        print("Sorry! You Failed ❌")

if __name__ == "__main__":
    main()

