def main():
    result = []
    numbers = [3, 5, 2, 4, 1]

    total = 0
    for i in numbers:
        total += i
        result.append(total)

    print("cumulative sum is:", result)


if __name__ == "__main__":
    main()
