
print("hiii! hello world")
def get_a_no(n):
    if n==0 or n==1:
        return 1
    else:
        return n*get_a_no(n-1)
    
def getNumber():        
    return int(input("Enter a number: "))


def main():
    number = getNumber()
    result = get_a_no(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()