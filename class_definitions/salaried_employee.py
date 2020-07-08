from class_definitions.employee import Employee


class SalariedEmployee(Employee):
    """
    Salaried Employee Class
    """
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary):
        """
        Constructor for Salaried Employee
        :param last_name: required
        :param first_name: required
        :param address: required
        :param phone_number: required
        :param start_date: required
        :param salary: required
        """
        super().__init__(last_name, first_name, address, phone_number)
        self._start_date = start_date
        self._salary = salary

    def give_raise(self):
        pass

    def display(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':
    pass
