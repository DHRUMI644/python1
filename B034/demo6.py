def main():
    input=[2,5,8,1,4,2,5,7,2,9,1]
    output=[]
    for i in input:
        if i not in output:
            output.append(i)    

    print("List after removing duplicates:", output)

if __name__ == "__main__":
    main()