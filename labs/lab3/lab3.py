"""
Sam Marshall Buck
Lab3
"""


def traffic():
    roads = eval(input("How many roads were surveyed?"))
    total_traveled = 0
    for i in range(1, roads + 1):
        print("How many days was road", i, "surveyed?", end="")
        road_survey = eval(input(" "))
        all_cars = 0
        for j in range(1, road_survey + 1):
            print("How many cars traveled on day ", j, "?", sep="", end=" ")
            cars_traveled = eval(input(" "))
            all_cars = all_cars + cars_traveled
        average = all_cars / road_survey
        print("Road", i, "average vehicles per day: ", average)
        total_traveled = total_traveled + all_cars
    total_average = total_traveled / roads
    final_total = round(total_average, 2)
    print("Total number of vehicles traveled on all roads: ", total_traveled)
    print("Average number of vehicles per road:", final_total)


traffic()
