from sales_person import SalesPerson
class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        adding_people = open(file_name, "r")
        for line in adding_people.readlines():
            strip = line.rstrip()
            splitter = strip.split(",")
            sales_person = SalesPerson(splitter[0], splitter[1].lstrip())
            sales_split = splitter[2].lstrip().rstrip().split(" ")
            for sales in sales_split:
                SalesPerson.enter_sale(sales_person, eval(sales))
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        sales = []
        for i in range(len(self.sales_people)):
            employee = self.sales_people[i]
            person = []
            sales_id = SalesPerson.get_id(employee)
            person.append(int(sales_id))
            name = SalesPerson.get_name(employee)
            person.append(name)
            total_sales = float(SalesPerson.total_sales(employee))
            person.append(total_sales)
            if SalesPerson.met_quota(employee, quota):
                person.append(True)
            else:
                person.append(False)
            sales.append(person)
        return sales

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        if employee_id in self.sales_people:
            return self.sales_people[employee_id + 1]
        return None

    def get_sale_frequencies(self):
        pass

