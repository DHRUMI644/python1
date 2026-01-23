def main():
    num=[2,6,8,1,4,2,7,9,2,2,2,6,6,6,6,6]
    majority_element= max(set(num), key= num.count)
    print("Majority Element is:", majority_element)
if __name__ == "__main__":
    main()