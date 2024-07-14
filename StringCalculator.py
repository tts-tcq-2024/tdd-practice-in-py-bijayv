def add(num):
    if(num == ""):
        return 0
    n = number_split(num)
    s = number_sum(n)
    return s

def number_split(num):
    if(len(num) == 1):
        return list(num)
    if(num.startswith("//")):
        num = num.replace("//","")
        num = num.replace("\n", "")
        return (num[1:].split(num[0]))
    num = num.replace("\n",",")
    return num.split(",")

def number_sum(n):
    for i in range(0,len(n)):
        n[i] = int(n[i])
        if(n[i] >1000):
            n[i] = 0
    s = number_check(n)
    return s

def number_check(a):
    l = []
    s = 0
    sum = 0 
    for i in range(0,len(a)): 
        if(a[i] < 0):
            l.append(a[i])
            s = 1
            continue
        sum = sum + a[i]
    return (num_neg(sum,s,l))
    
def num_neg(sum,s,l):
    if (s == 0):
        return sum
    else:
        raise Exception ("Negative No not allowed " + str(l))
        #print("Negative No not allowed " + str(l))
