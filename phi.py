def factors(n):
    fac=[]
    for x in range (1,n+1):
        if n%x==0:
            fac.append(x)
    return fac

def relativelyPrime(n,x):
    fac_n=factors(n)
    fac_x=factors(x)
    loop=min(n,x)
    for y in range(1,len(fac_n)):
        if fac_n[y] in fac_x:
            return False
    return True

def phi(n):
    count=0
    n_factors=factors(n)
    for x in range(0,n-1):
        if relativelyPrime(n,x):
            #print(x)
            count+=1
    return count

def Z_n_star(n):
    return phi(n)

def eulersTheorem(n,k):
    if not relativelyPrime(n,k):
        print("Error: "+str(n)+" and "+str(k)+" are not relatively prime. Euler's Theorem does not hold.")
    else:
        print("n = "+str(n))
        print("k = "+str(k))
        print("phi("+str(n)+") = "+str(phi(n)))
        calculate=k**(phi(n))
        print("calculated value for k^phi(n): "+str(calculate))
        calculate_mod_n=calculate%n
        print("mod n is (expected 1): "+str(calculate_mod_n))
        print(str(k)+"^phi("+str(n)+") = 1 (mod "+str(n)+")")


eulersTheorem(5,2)
