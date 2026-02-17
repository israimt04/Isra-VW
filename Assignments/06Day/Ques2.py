class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")

    def _financial_report(self):
        print("Confidential Financial Report: Revenue ₹500 Crore")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")

    def _policy_update(self):
        print("Confidential Policy Update: Leave policy revised.")


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee, Company):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company,
                 company_name, company_location):
        NewEmployee.__init__(self, emp_id, emp_name, designation, joining_date, previous_company)
        Company.__init__(self, company_name, company_location)

    def access_financial_report(self):
        self._financial_report()


class HR(NewEmployee):
    def access_policy_update(self):
        self._policy_update()


class Developer(NewEmployee):
    pass


class Intern(NewEmployee):
    pass


class ManagerHR(Manager, HR):
    def access_all_confidential(self):
        self._financial_report()
        self._policy_update()


class DeveloperIntern(Developer, Intern):
    pass


class SoroRaRxAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):
        super().show_details()
        print("\nMerged Employee List:")
        for emp in self.employees:
            print("------------------")
            emp.show_details()


if __name__ == "__main__":

    company = SoroRaRxAcquisition("SoroRaRx Technologies", "Hyderabad")

    m1 = Manager(201, "Rohit Sharma", "Manager", "01-01-2022",
                 "Infosys", "SoroRaRx Technologies", "Hyderabad")

    hr1 = HR(202, "Ananya Mehta", "HR Executive",
             "10-03-2021", "TCS")

    d1 = Developer(203, "Karan Verma", "Developer",
                   "15-07-2023", "Wipro")

    i1 = Intern(204, "Sneha Iyer", "Intern",
                "01-08-2024", "College Project")

    mh = ManagerHR(205, "Vikram Rao", "Manager-HR",
                   "05-05-2020", "Capgemini",
                   "SoroRaRx Technologies", "Hyderabad")

    company.add_employee(m1)
    company.add_employee(hr1)
    company.add_employee(d1)
    company.add_employee(i1)
    company.add_employee(mh)

    company.show_details()

    print("\nManager accessing financial report:")
    m1.access_financial_report()

    print("\nHR accessing policy update:")
    hr1.access_policy_update()

    print("\nManagerHR accessing all confidential data:")
    mh.access_all_confidential()