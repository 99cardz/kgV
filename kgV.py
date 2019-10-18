#kleinstes gemeinsames Vielfaches

prime_list = []

def generate_pries(max):
    while num < max:
    	nummern.append(num)
    	for i in range(1, int(num)):
    		div = float(i)
    		if (num/div).is_integer():
    			##print(num)
    			prime_list.append(num)
    	num += 1

    for num in nummern:
    	##print(num)
    	if prime_list.count(num) > 1:
    		##print(num)
    		for x in range(prime_list.count(num)):
    			prime_list.remove(num)
    print(*prime_list)


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
