cnt = 0

def new_employee(name, job, cnt):
    cnt += 1
    return ({'name': name, 'job':job}, cnt)

def get_name(employee):
    print(employee['name'])

def change_job(employee, job):
    employee['job'] = job
    return employee
	
# dodajemy komputer

def new_computer(name, type):
    return {'name': name, 'type': type}
	
def give_computer_to_employee(computer, employee):
    computer['employee'] = employee	

	