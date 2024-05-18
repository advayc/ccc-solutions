class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = 0
        while len(students) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                c = 0
            else:
                c += 1
                students.append(students.pop(0))
            
            if c == len(students):
                return c
        
        return 0

