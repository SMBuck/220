class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales_list = []

    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales_list.append(float(sale))

    def total_sales(self):
        my_sum = 0
        for sale in self.sales_list:
            my_sum += sale
        return my_sum

    def get_sales(self):
        return self.sales_list

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self:
            return -1
        elif other.total_sales() < self:
            return 1
        return 0

    def __str__(self):
        return '{}-{}:{}'.format(self.employee_id, self.name, self.total_sales())
