def week(i):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(i, "Invalid day")

def main():
    day_number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
    print(week(day_number))



if __name__ == "__main__":
    main()
