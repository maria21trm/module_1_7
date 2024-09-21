grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
a= sum(grades[0])
b = len(grades[0])
c = a/b #средний балл Aaron
a1 = sum(grades[1])
b1 = len(grades[1])
c1 = a1/b1 #средний балл Bilbo
a2 = sum(grades[2])
b2 = len(grades[2])
c2 = a2/b2 #средний балл Johnny
a3 = sum(grades[3])
b3 = len(grades[3])
c3 = a3/b3 # средний балл Khendrik
a4 = sum(grades[4])
b4= len(grades[4])
c4 = a4/b4 # средний балл Steve
students = list(students)
students.sort()
students = tuple(students)
grades[0] = c
grades[1] = c1
grades[2] = c2
grades[3] = c3
grades[4] = c4
dict_ = dict(zip(students , grades ))
print(dict_)

