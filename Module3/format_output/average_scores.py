from statistics import mean


def information():
    input1,input2,input3 = input("what are your 3 scores (comma separated): ").split(',')
    list = [input1, input2, input3]
    list = [int(i) for i in list]
    fname = input("What is your first name: ").capitalize()
    lname = input("What is your last name: ").capitalize()
    age = input("How old are you: ")
    average(list, lname, fname, age)
    #return list, lname, fname, age

#list, lname,fname,age = information()

def average(list, lname, fname, age):
    average_score = round(mean(list),2)
    print(f'{lname}, {fname} age {age} average grade {average_score}')
    return average_score

if __name__ == '__main__':
    information()
