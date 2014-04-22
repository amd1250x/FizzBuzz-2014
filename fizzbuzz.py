lister = []

for i in range (1, 101):
    lister.append(i)

def fibu (ls, n):
    if n < 101:
        #if n is divisible by 3 and not 5
        if n%3 == 0 and n%5 != 0:
            ls[n-1] = "fizz"
            fibu (ls, n+1)
        #if n is divisible by 5 and not 3
        elif n%5 == 0 and n%3 != 0:
            ls[n-1] = "buzz"
            fibu (ls, n+1)
        #n is divisible by 5 and 3
        elif n%3 == 0 and n%5 == 0:
            ls[n-1] = "fizzbuzz"
            fibu (ls, n+1)
        #if n is not divisible by 5 or 3
        else:
            fibu (ls, n+1)
    #if the function reaches the end of the list
    elif n == 101:
        print ls

fibu(lister, 1)
