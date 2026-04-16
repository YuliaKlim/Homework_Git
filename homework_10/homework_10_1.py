class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        # або можна використати варіант з super(), але в цьому випадку потрібен додадковий параметр **kwargs
        # super().__init__(name, salary, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        # super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        # у цьому класі у варіанті з super() додатковий **kwargs не потрібен
        # super().__init__(name, salary, department=department, programming_language=programming_language)
        self.team_size = team_size

    def __repr__(self):
        return f'TeamLead name: {self.name}, salary: {self.salary}, department: {self.department}, team size: {self.team_size}'

def print_team_lead(class_object):
    required_attributes = ["name", "salary", "department", "programming_language", "team_size"]
    for attribute in required_attributes:
        if hasattr(class_object, attribute):
            print(f'Attribute {attribute} found: {getattr(class_object, attribute)}')
        else:
            print(f'Attribute {attribute} not found')

team_lead = TeamLead('Klimenko', 1500, 'DevOps', 'Python', 10)
dev = Developer('Saling', 1000, 'C++')
print_team_lead(team_lead)
print_team_lead(dev)