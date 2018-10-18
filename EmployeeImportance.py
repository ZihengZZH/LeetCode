'''

You are given a data structure of employee information, which includes the employee's unique id, 
his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
They have importance value 15, 10 and 5, respectively. 
Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. 
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, 
you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. 
They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

'''


# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    # recursive beats 41%
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        for e in employees:
            if e.id == id:
                employee = e
                res += e.importance
        if not employee.subordinates:
            return employee.importance
        else:
            for sub in employee.subordinates:
                res += self.getImportance(employees, sub)
        return res

    importance = 0
    
    # a little faster beats 50%
    def getImportance_fast(self, employees, id):
        employee_map = dict()
        for e in employees:
            employee_map[e.id] = e
        for emp in employees:
            if emp.id == id:
                self.helper(employee_map, id)
                break
        return self.importance

    def helper(self, employee_map, curid):
        self.importance += employee_map[curid].importance
        for sub in employee_map[curid].subordinates:
            self.helper(employee_map, sub)


if __name__ == "__main__":

    employees = [Employee(1, 5, [2,3]), Employee(2, 3, []), Employee(3, 3, [])]
    
    solu = Solution()
    print(solu.getImportance_fast(employees, 1))