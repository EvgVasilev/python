with open('salary.txt', 'r', encoding="utf-8") as sal:
    total_salary_sum = 0
    line_num = 0
    less = []
    for line in sal:
        worker, salary = line.split()
        salary = float(salary)
        total_salary_sum += salary
        if salary < 20000:
            less.append(worker)
        line_num += 1
    print(f"Оклад меньше 20000: {less}, Средняя величина дохода сотрудников: {round((total_salary_sum / line_num), 2)}")
