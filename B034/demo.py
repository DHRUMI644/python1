# print("hiii! hello world")
print("This is a demo file in the B034 directory.")
# if age > 18:    
print("You are an adult.")


def main():

    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


        def getNumber():            
            number = int(input("Enter a number: "))
            return number
        
        def checkOddEven(num):            
         return bool(num % 2)
        
        def checkoddevenseries(num):
            def main():
                    number = getNumber()
                    if checkOddEven(number) %2==0:
                        print("The number is even.")
                    else:
                        print("The number is odd.")

if __name__ == "__main__":
    main()
