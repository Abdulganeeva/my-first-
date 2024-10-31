def find_max(employees1, employees2, ):
    salary_max = -1
    employee_max = None

    for e in employees1:
        if e["salary"] >= salary_max:
            salary_max = e["salary"]
            employee_max = e

    for e in employees2:
        if e["salary"] > salary_max:
            salary_max = e["salary"]
            employee_max = e



    return employee_max["name"]


employees1 = [
    {"name": "Anya", "salary": 500},
    {"name": "Sveta", "salary": 800},
    {"name": "Katya", "salary": 300},
    {"name": "Olya", "salary": 800},
]


employees2 = [
    {"name": "Olya", "salary": 100},
    {"name": "Viktor", "salary": 300},
    {"name": "Max", "salary": 450},
]

print(find_max(employees1, employees2,))

