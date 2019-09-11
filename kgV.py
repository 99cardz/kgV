#kleinstes gemeinsames Vielfaches

prime_numbers = [2.0,3.0,5.0,7.0,11.0,13.0,17.0,19.0,23.0,29.0,31.0]#more than enough
def input_nenner(n):
    nenner = []
    for i in range(n):
        nenner.append(float(input("Nenner %s:" % i)))
    print(nenner)
    return nenner

def append_to_kgV(kgV_list, single_list):
    print(single_list)
    for prime in single_list:
        if prime not in kgV_list:
            kgV_list[prime_numbers.index(prime)].append(prime)
    return kgV_list
def calculate_kgV(list):
    kgV_list = []
    for n in range(len(prime_numbers)):
        kgV_list.append([])
    for n in range(len(list)):
        single_list = []
        print(single_list)
        number = list[n]
        print("number:", number)
        i = 0
        while i < len(prime_numbers):
            print(i)
            if number in prime_numbers:
                single_list.append(number)
                print("break")
                break
            elif (number/prime_numbers[i]).is_integer():
                single_list.append(prime_numbers[i])
                number = number/prime_numbers[i]
                print("yeah", number)
                i = 0
            else:
                i=+1
                print("+1")
                if i > len(prime_numbers):
                    print("ohno")
        kgV_list = append_to_kgV(kgV_list, single_list)
    return kgV_list

print(list)
print(calculate_kgV(input_nenner(int(input("wie viele nenner?")))))
