def letter2number(lgrade):
    grade = ['F','E','D','D+','C','C+','B','B+','A-','A','A+']
    for i in range(len(grade)):
        if lgrade == grade[i]:
            return i

def letter2number_v2(lgrade):
    grade_dict = {
        'A+':10,
        'A':9,
        'A-':8,
        'B+':7,
        'B':6,
        'C+':5,
        'C':4,
        'D':3,
        'E':2,
        'F':1
    }
    grade_index = grade_dict[lgrade]
    return grade_index

def lookup():
    phonebook = {('Anna','Karenian'):'(123)456-78-90',
                 ('Yu','Tsun'):'(901)234-56-78',
                 ('Hans','Castorp'):'(321)908-76-54'}
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    full_name = (first_name, last_name)
    info = phonebook[full_name]
    print(info)
