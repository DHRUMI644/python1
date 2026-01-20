def segregatemarks(lst):
    a = []
    b = []
    c = []

    for val in lst:
        if val >= 80:
            a.append(val)
        elif val >= 50:
            b.append(val)
        else:
            c.append(val)

    return a, b, c



def main():
    marks = [45, 67, 89, 90, 34, 56, 78, 12, 99, 60]

    A_grade, B_grade, C_grade = segregatemarks(marks)

    print(f"A grade students are: {A_grade}")
    print(f"B grade students are: {B_grade}")
    print(f"C grade students are: {C_grade}")


if __name__ == "__main__":
    main()
