def main():
    pre_input = [2, 5, 8, 1, 4, 2, 5, 7, 2, 9, 1]
    user_input = int(input("Enter a target to find addition of index of two numbers: "))

    for i in range(len(pre_input)):
        for j in range(i + 1, len(pre_input)):
            if pre_input[i] + pre_input[j] == user_input:
                print(f"Numbers found: {pre_input[i]}, {pre_input[j]} at index {i}, {j}")
                print("Sum of index:", i + j)
                return 


if __name__ == "__main__":
    main()
