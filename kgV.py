#kleinstes gemeinsames Vielfaches

prime_numbers = [2.0,3.0,5.0,7.0,11.0,13.0,17.0,19.0,23.0,29.0]#more than enough

def input_nenner(n):
    nenner = []
    for i in range(n):
        nenner.append(float(input("Nenner %s:" % i)))
    print(nenner)
    return nenner

def calculate_kgV(list):
    multibles_list = []
    for n in range(len(list)):
        number = list[n]
        print("number:", number)
        i = 0
        while i < len(prime_numbers):
            if number in prime_numbers:
                multibles_list.append(number)
                break
            if (number/prime_numbers[i]).is_integer():
                multibles_list.append(prime_numbers[i])
                number = number/prime_numbers[i]
                print("yeah", number)
                i = 0
            else:
                i=+1


    return multibles_list
print(calculate_kgV(input_nenner(int(input("wie viele nenner?")))))
