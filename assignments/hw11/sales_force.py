from sales_person import SalesPerson
class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        adding_people = open(file_name, "r")
        for line in adding_people.readlines():
            strip = line.rstrip()
            splitter = strip.split(",")
            employee_id = int(splitter[0])
            name = splitter[1]
            sales = splitter[2]
            person = SalesPerson(employee_id, name), sales
            self.sales_people.append(person)

    def quota_report(self, quota):
        my_data = open("sales_data.txt", "r")
        float_list = []
        for line in my_data.readlines():
            strip = line.rstrip()
            splitter = strip.split(",")
            my_sum = ""
            for value in splitter[2::3]:
                my_sum += value
                my_sum.lstrip()
            new = my_sum.split(" ")
            new.remove('')
            for i in new:
                float_list.append(float(i))
        my_sum_1 = 0
        for value in float_list[0:3]:
           my_sum_1 += value
        my_sum_2 = 0
        for value in float_list[3:8]:
            my_sum_2 += value
        my_sum_3 = 0
        for value in float_list[8:12]:
            my_sum_3 += value
        my_sum_4 = 0
        for value in float_list[12:16]:
            my_sum_4 += value
        my_sum_5 = 0
        for value in float_list[16:19]:
            my_sum_5 += value

    def top_seller(self):


    def individual_sales(self, employee_id):
        if employee_id in self.sales_people:
            return self.sales_people[employee_id + 1]
        return None

    def get_sale_frequencies(self):

