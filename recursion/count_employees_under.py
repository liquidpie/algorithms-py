def count_employees_under(employee_name, employee_database):
    """
        count how many employees report (directly or indirectly) to the person named by employee_name
        
    :param employee_name: name of the employee
    :param employee_database: list of employee name and his/her manager's name
    :return: count of employees under given employee
    """
    count = 0

    for person in employee_database:
        if person.manager == employee_name:
            count += 1
            count += count_employees_under(person.name, employee_database)

    return count


class Person:

    def __init__(self, name, manager):
        self.name = name
        self.manager = manager

if __name__ == '__main__':
    employee_database = list()
    employee_database.append(Person("Betty", "Sam"))
    employee_database.append(Person("Bob", "Sally"))
    employee_database.append(Person("Dilbert", "Nathan"))
    employee_database.append(Person("Joseph", "Sally"))
    employee_database.append(Person("Nathan", "Veronica"))
    employee_database.append(Person("Sally", "Veronica"))
    employee_database.append(Person("Sam", "Joseph"))
    employee_database.append(Person("Susan", "Bob"))
    employee_database.append(Person("Veronica", None))

    employee_name = "Veronica"
    count = count_employees_under(employee_name, employee_database)

    print("Employees under", employee_name, "are:", count)



