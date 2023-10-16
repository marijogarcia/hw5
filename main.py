def part1():
    # Ask for years
    years = int(input("Enter the number of years: "))
    months = 0
    total_rainfall = 0

    # Outer loop
    for i in range(years):
        print("Year " + str(i))
        months += 12
        # Inner loop
        for j in range(12):
            rainfall = float(input("Inches of rainfall in month " + str(j) + ": "))
            total_rainfall += rainfall

    print("Total Months: " + str(months))
    print("Total Rainfall: " + str(total_rainfall))
    print("Average Rainfall: " + str(total_rainfall / months))
    return

part1()


# Part 2
def get_points(num_books):
    if (num_books < 2):
        return 0;
    if (num_books < 4):
        return 5;
    if (num_books < 6):
        return 15;
    if (num_books < 8):
        return 30;
    return 60

def part2():
    num_books = int(input("How many books did you buy this month? "))
    print(str(get_points(num_books)) + " points")

    num_books = int(input("How many books did you buy this month? "))
    print(str(get_points(num_books)) + " points")

    num_books = int(input("How many books did you buy this month? "))
    print(str(get_points(num_books)) + " points")

    num_books = int(input("How many books did you buy this month? "))
    print(str(get_points(num_books)) + " points")

    num_books = int(input("How many books did you buy this month? "))
    print(str(get_points(num_books)) + " points")
    return

part2()