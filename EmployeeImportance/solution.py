class Employee:

    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    

    def getImportance(self, employees, id) -> int:

        wanted_employees = []
        employee_dict = {e.id: e for e in employees}
        #print(employee_dict)
        current_employee = employee_dict[id].id
        wanted_employees.append(current_employee)
        importance = 0
        #print(current_employee)
        while wanted_employees:
            importance += employee_dict[current_employee].importance
            #print(importance)
            wanted_employees.remove(current_employee)
            tempList = employee_dict[current_employee].subordinates
            #print("this is templist {} and its type {}".format(tempList, type(tempList)))
            wanted_employees.extend(employee_dict[current_employee].subordinates)
            if wanted_employees:
                current_employee = wanted_employees[0]
            #print(wanted_employees)
        return importance
        



        


first = Employee(1, 5 , [2,3])
second = Employee(2,3,[4])
third = Employee(3,4,[])
fourth = Employee(4,1,[])


x = Solution()
employees = [first, second, third, fourth]
id = 1

print(x.getImportance(employees, id))


