# Harshit's salary is 100
# Mohit salary is 50


with open('exercise1.txt' , 'r') as rf :
    with open('output_ex.txt' , 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary}')