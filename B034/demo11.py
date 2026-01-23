def main():
    input=[1,4,2]
    permutations=[]
    for i in range(len(input)):
        for j in range(len(input)):
            for k in range(len(input)):
                if i!=j and j!=k and i!=k:
                    permutations.append([input[i], input[j], input[k]]) 
    print("All possible permutations are:", permutations)
if __name__ == "__main__":
    main()