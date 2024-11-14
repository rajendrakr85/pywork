from functools import reduce
import pandas as pd
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1), 1)
#print(factorial(5))

#print(reduce(lambda x, y: x * y, range(1, 5+1), 1))


nested_list=[12,23,34,[55,66,77,[23,54,65,76,[90,78,76,43]]]]

print([sublist4 for sublist1 in nested_list
            for sublist2 in (sublist1 if isinstance(sublist1, list) else [sublist1])
            for sublist3 in (sublist2 if isinstance(sublist2, list) else [sublist2])
            for sublist4 in (sublist3 if isinstance(sublist3, list) else [sublist3])])


def flatten(nested_list):
    return ([item for sublist in nested_list for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])])

#print(flatten(nested_list))

print([sublist2 for sublist1 in nested_list
        for sublist2 in (flatten(sublist1) if isinstance(sublist1, list)
                                           else [sublist1])])


data = {'Student': ['John', 'Jane', 'Mike', 'Sara', 'Tom'],
        'Math': [35, 50, 30, 45, 60],
        'Science': [20, 45, 38, 30, 65], 
        'English': [50, 30, 60, 25, 45],
        'History': [40, 50, 20, 30, 70] }

df = pd.DataFrame(data)
failed_student = df.set_index('Student').lt(40)
#print(failed_student)

failed_subject = failed_student.apply(lambda row: row.index[row].tolist(), axis=1)
#print(failed_subject)


