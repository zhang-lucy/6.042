
def factors(n):
    fac=[]
    for x in range (1,n+1):
        if n%x==0:
            fac.append(x)
    return fac

def isPrime(n):
    fac=factors(n)
    for x in range(2,n):
        if x in fac:
            return False
    return True

def gcd(x,y):
    fac_x=factors(x)
    fac_y=factors(y)
    for z in range (len(fac_x)-1,0,-1):
        if fac_x[z] in fac_y:
            return fac_x[z]
    return 1

def generateE(p,q):
    count=10
    e=0
    ret=[]
    if (gcd(e,((p-1)*(q-1)))==1):
            ret.append(e)
            e+=1
            count-=1
    """while (count>0):
        if (gcd(e,((p-1)*(q-1)))==1):
            ret.append(e)
            e+=1
            count-=1"""

    return ret

print(generateE(11,13))

class Sender:
    #Public Key is (e,n) where n=p*q
    def __init__(self, p, q, e):
        self.p=p
        self.q=q
        self.e=e
        n=p*q
        self.n=n
        if not isPrime(p):
            print("Error: "+str(p) +" is not prime.")
        if not isPrime(q):
            print("Error: "+str(q) +" is not prime.")
        if (gcd(e,((p-1)*(q-1)))==1):
            print("Public Key is ("+str(self.e)+", "+str(self.n)+")")
        else:
            print("Error: gcd(e,((p-1)*(q-1)))==1 is not true")
    def getP(self):
        return self.p
    def getQ(self):
        return self.q
    def getE(self):
        return self.e
    def getPublicKey(self):
        return self.e
    def getN(self):
        return self.n
    def encrypt(self,message):
        encryptedMessage=""
        return encryptedMessage


class Receiver:
    def __init__(self, key):
        self.key=key
        self.e=key[0]
        self.n=key[1]
    def decode(self):
        decodedMessage=""
        return decodedMessage

s1=Sender(11,13,17)
print(s1.getP())
print(s1.getQ())
print(s1.getE())
print(s1.getN())

