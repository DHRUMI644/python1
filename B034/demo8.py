def main():
    numbers = [1, 3, 5, 6, 7]
    number = int(input("Enter a number to check its presence: "))

    if number in numbers:
        print(f"{number} is present in the list.")
        position = numbers.index(number)
        print(f"Position of {number} in the list: {position}")
    else:
        print(f"{number} is not present in the list.")


if __name__ == "__main__":
    main()
