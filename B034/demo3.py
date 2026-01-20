def main():
    units = int(input("Enter the number of units consumed: "))

    if units == 100:
        bill = 100

    elif units > 100 and units < 200:
        bill = 100 + 2 * (units - 100)

    elif units == 200:
        bill = 300

    else:
        bill = 300 + 3 * (units - 200)

    print("Total bill amount is:", bill, "rs")


if __name__ == "__main__":
    main()