###############################################
# Imports used                                #
# You may import other libraries if necessary #
###############################################
import sys

#################################################
# Constants used                                #
# You may add other constants here if necessary #
#################################################

# constant tuple named DEPARTMENT to store the department that can be selected when add
DEPARTMENT = ("HR", "IT", "Admin", "Finance")


# Function ID mapped with name
RETURN = ""
DISPLAY_ALL_EMPLOYEES = 1
ADD_AN_EMPLOYEE = 2
REMOVE_AN_EMPLOYEE = 3
UPDATE_EMPLOYEE_SALARY = 4
DISPLAY_STATISTICS = 5

# Other constants here



#################################################
# Functions used                                #
# You may add other functions here if necessary #
#################################################

# limit the string length with space
def str_limit(strr, length):
    '''
    :param strr: string to input
    :param length: the final length of string (should be larger than the original length)
    :return: longer string
    '''
    space_num = length - len(strr)
    if space_num < 0:
        return strr[0:length]
    else:
        return str(strr + ' ' * space_num)


# write a function display_all_employees for menu item 1 to display all employees in system
def display_all_employees(list_dict_employees):
    '''
    :param list_dict: a list of dictionaries containing keys of 'ID', 'Name', 'Salary' and 'Department'
    :return: None (print all employee data)
    '''
    # complete your function here
    # this function have no return value
    print('All employee(s) information:')
    print('ID        |', str_limit('Name', 24), ' | Salary         | Department')
    for dicts in list_dict_employees:
        print(dicts['ID'], ' |',
              str_limit(dicts['Name'], 24), ' | $',
              str_limit(str(dicts['Salary']), 11), ' |',
              dicts['Department'])


# write a function display_stat for menu item 5 to display company statistics in system
def display_stat(list_dict_employees):
    # complete your function here
    # this function have no return value
    # create a dictionary with dept name as keys
    dict_stat = dict([(dept, []) for dept in DEPARTMENT])
    list_salary = []
    for ele in list_dict_employees:
        list_salary.append(ele['Salary'])
        if ele['Department'] == DEPARTMENT[0]:
            dict_stat[DEPARTMENT[0]].append(ele['Salary'])
        elif ele['Department'] == DEPARTMENT[1]:
            dict_stat[DEPARTMENT[1]].append(ele['Salary'])
        elif ele['Department'] == DEPARTMENT[2]:
            dict_stat[DEPARTMENT[2]].append(ele['Salary'])
        elif ele['Department'] == DEPARTMENT[3]:
            dict_stat[DEPARTMENT[3]].append(ele['Salary'])
    print('Company statistics:')
    print('Department | No. of staff | Highest Salary | Lowest Salary | Average Salary')
    for keyss in dict_stat.keys():
        if len(dict_stat[keyss]) == 0:  # if there is no such department
            print(str_limit(keyss, 10), '|',  # department name
                  str_limit(str(0), 12), '| $',  # number of staff
                  str_limit(str(0), 12), '| $',  # highest salary
                  str_limit(str(0), 11), '| $',  # lowest salary
                  str_limit(str(0), 13))  # average salary
        else:
            print(str_limit(keyss, 10), '|',  # department name
                  str_limit(str(len(dict_stat[keyss])), 12), '| $',  # number of staff
                  str_limit(str(max(dict_stat[keyss])), 12), '| $',  # highest salary
                  str_limit(str(min(dict_stat[keyss])), 11), '| $',  # lowest salary
                  str_limit(str(sum(dict_stat[keyss]) / len(dict_stat[keyss])), 13))  # average salary
    print('Total number of staff:', len(list_dict_employees))
    print('Highest Salary: $', max(list_salary))
    print('Lowest Salary: $', min(list_salary))
    print('Average Salary: $', sum(list_salary) / len(list_salary))


# write a function read_employee_from_file to read in employee’s information from file named "employee.txt" located in the same folder
def read_employee_from_file(file_path):
    '''
    :param file_path: file path to input
    :return: a dictionary of employee data
    '''
    list_dict_employees = list()
    # complete your function here
    # this function should return a list of dictionary contains all employee's information
    with open('employee_list.txt', 'r') as f:
        lines = f.read().splitlines()
    employees = lines[5:11]  # only 6th to 11th rows are displayed
    for e in employees:
        e_list = e.split(',')  # get a list of contents in the string
        e_dict = {'ID': e_list[0].strip(),
                  'Name': e_list[1].strip(),
                  'Salary': float(e_list[2].strip()),
                  'Department': e_list[3].strip()}
        list_dict_employees.append(e_dict)
    # This static variable is for your development in early stage
    # Zero marks will be given if you assigned the employee data by this static variable    
    """
    list_dict_employees = [
        {"ID": "IVE00001", "Name": "Kelvin Yip", "Salary" : 43210.5, "Department": "IT" },
        {"ID": "IVE00002", "Name": "Cow Leung", "Salary" : 32105.4, "Department": "Admin" },
        {"ID": "IVE00003", "Name": "Leung Pig Hung", "Salary" : 21054.3, "Department": "HR" },
        {"ID": "IVE00004", "Name": "Michael Fung", "Salary" : 10543.2, "Department": "Finance" },
        {"ID": "IVE00005", "Name": "Joe Yeung", "Salary" : 6543.2, "Department": "IT" },
        {"ID": "IVE00006", "Name": "Martin Kung", "Salary" : 5432.1, "Department": "Admin" }
    ]
    """
    return list_dict_employees
    

# You may implement other necessary functions here


# Main function starts here
def main():
    # Read employees record from file
    list_dict_employees = read_employee_from_file('employee_list.txt')
    # Welcome message
    print("Welcome to Employee Management System.")
    # Main menu
    while True:
        print("=======================================")
        print("Employee Management System Menu:")
        print("No. | Function")
        print("1   | Display all employee")
        print("2   | Add an employee")
        print("3   | Remove an employee")
        print("4   | Update employee salary")
        print("5   | Display company statistics")
        input_num = input("Please input your choice. (1 – 5, Enter to exit):")
        # When user pressed enter - break
        if input_num == RETURN:
            break
        # raise error if wrong functionID input is detected
        input_num = int(input_num)
        while input_num not in range(1, 6):
            print('Invalid input for choice')
            input_num = int(input('Please input your choice. (1 - 5, Enter to exit):'))
        # When user input 1 to display all employee
        if input_num == DISPLAY_ALL_EMPLOYEES:
            display_all_employees(list_dict_employees)  # only display the former 24 letters of the employee name
        # When user input 2 to add an employee
        elif input_num == ADD_AN_EMPLOYEE:
            input_name = str(input("Please input employee's name, Enter to return:"))
            # When user pressed enter - continue
            if input_name == RETURN:
                continue
            # raise error if wrong name input is detected
            while any(map(str.isdigit, input_name)):
                print('Not a valid employee name')
                print("Employee's name should not contain digit")
                input_name = str(input("Please input employee's name:"))
            input_salary = float(input("Please input employee's salary:"))
            # raise error if wrong salary input is detected
            while input_salary <= 0:
                print("Employee's salary should be greater than 0")
                input_salary = float(input("Please input employee's salary:"))
            input_dept = str(input("Please input employee's department:"))
            # raise error if wrong department input is detected
            while input_dept not in DEPARTMENT:
                print('Not a valid department')
                print("Employee's department should be HR/IT/Admin/Finance")
                input_dept = str(input("Please input employee's department:"))
            last_id = list_dict_employees[-1]['ID']  # get last ID
            new_id = 'IVE' + str(int(last_id[5:]) + 1).zfill(5)
            list_dict_employees.append({'ID': new_id,
                                        'Name': input_name,
                                        'Salary': input_salary,
                                        'Department': input_dept})
            print('***** Employee Added Successfully *****')
        # When user input 3 to remove employee record
        elif input_num == REMOVE_AN_EMPLOYEE:
            display_all_employees(list_dict_employees)
            input_id = input("Please input employee's ID to remove record, Enter to return:")
            # When user pressed enter - continue
            if input_id == RETURN:
                continue
            # get the employee id list
            id_list = []
            for dicts in list_dict_employees:
                id_list.append(dicts['ID'])
            # raise error if wrong employeeID input is detected
            while input_id not in id_list:
                print("Not a valid employee's ID")
                print("Employee's ID record not found")
                input_id = input("Please input employee's ID to remove record")
            del list_dict_employees[id_list.index(input_id)]
            print('***** Employee Removed Successfully *****')
        # When user input 4 to update an employee salary
        elif input_num == UPDATE_EMPLOYEE_SALARY:
            display_all_employees(list_dict_employees)
            input_id = input("Please input employee's ID, Enter to return:")
            # When user pressed enter - continue
            if input_id == RETURN:
                continue
            # get the employee ID list
            id_list = []
            for dicts in list_dict_employees:
                id_list.append(dicts['ID'])
            # raise error if wrong employeeID input is detected
            while input_id not in id_list:
                print("Not a valid employee's ID")
                print("Employee's ID record not found")
                input_id = input("Please input employee's ID:")
            input_salary = float(input("Please input employee's updated salary:"))
            # raise error if wrong salary input is detected
            while input_salary <= 0:
                print("Employee's salary should be greater than 0")
                input_salary = float(input("Please input employee's updated salary:"))
            list_dict_employees[id_list.index(input_id)]['Salary'] = input_salary
            print('***** Employee salary updated successfully *****')
        # When user input 5 to display company statistics
        elif input_num == DISPLAY_STATISTICS:
            display_all_employees(list_dict_employees)
            display_stat(list_dict_employees)


if __name__ == "__main__":
    main()
