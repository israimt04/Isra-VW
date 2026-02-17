class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")


class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Salary: {self.salary}")


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, policies):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.policies = policies

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies}")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, languages):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.languages = languages

    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {self.languages}")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")


class ManagerHR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, team_size, policies):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.team_size = team_size
        self.policies = policies

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies}")


class DeveloperIntern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date, salary, languages, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, salary)
        self.languages = languages
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Programming Languages: {self.languages}")
        print(f"Intern Duration: {self.duration} months")


class SamaRaRxAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):
        super().show_details()
        print("\nMerged Employee List:")
        for emp in self.employees:
            print("----------------------")
            emp.show_details()


if __name__ == "__main__":

    merged_company = SamaRaRxAcquisition("SamaRaRx Technologies", "Bangalore")

    m1 = Manager(101, "Rahul Sharma", "Manager", "01-01-2022", 90000, 10)
    d1 = Developer(102, "Priya Verma", "Developer", "15-03-2023", 70000, ["Python", "Java"])
    hr1 = HR(103, "Ankit Mehta", "HR Executive", "10-05-2021", 60000, ["Recruitment", "Compliance"])
    i1 = Intern(104, "Sneha Kapoor", "Intern", "01-06-2024", 20000, 6)

    mh = ManagerHR(105, "Vikram Singh", "Manager-HR", "01-07-2020", 95000, 8, ["HR Policies"])
    di = DeveloperIntern(106, "Aarav Iyer", "Dev-Intern", "01-08-2024", 30000, ["C++"], 3)

    merged_company.add_employee(m1)
    merged_company.add_employee(d1)
    merged_company.add_employee(hr1)
    merged_company.add_employee(i1)
    merged_company.add_employee(mh)
    merged_company.add_employee(di)

    merged_company.show_details()