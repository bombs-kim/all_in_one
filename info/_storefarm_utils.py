from random import randint

BI_RC = ([None]*48 + [n for n in range(0,10)] +
         [None]*7  + [n for n in range(10,36)] +
         [None]*6  + [n for n in range(10,36)])

def intAt(a, b):
    c = BI_RC[ord(a[b])]
    return c

# Be careful that keys are int in this implementation
class BigInteger(dict):
    def __init__(self, a, b=None, c=None):
        if a != None:
            # if ("number" == typeof a) this.fromNumber(a, b, c);
            # else if (b == null && "string" != typeof a) this.fromString(a, 256);
            # else this.fromString(a, b)
            self.fromString(a, b)

    # def __getitem__(self, key):
    #     try:
    #         return self[key]
    #     except:
    #         return getattr(self, strkey)

    def clamp(self):
        a = self.s & self.DM
        while self.t > 0 and self[self.t-1] == a:
            self.t -= 1

    def bitLength(self):
        if self.t <= 0:
            return 0
                                    # Not sure
        return self.DB * (self.t - 1) + int.bit_length(
            self[self.t - 1] ^ self.s ^ self.DM)

    def modPowInt(self, a, b):


    def subTo(self, a, b):
        c,d,e = 0,0,min(a.t, self.t)
        while c < e:
            d += self[c] - a[c]
            b[c] = d & self.DM
            c += 1
            d >>= self.DB
        if a.t < self.t:
            d -= a.s
            while c < self.t:
                d += self[c]
                b[c] = d & self.DM
                c += 1
                d >>= self.DB
            d += self.s
        else:
            d += self.s
            while c < a.t:
                d -= a[c]
                b[c] = d & self.DM
                d >>= self.DB
            d -= a.s
        b.s = -1 if d < 0 else 0
        if d < -1:
            b[c] = this.DV + d
            c += 1
        elif d > 0:
            b[c] = d
            c += 1
        b.t = c
        b.clamp()


    def fromInt(self, a):
        self.t = 1;
        self.s = -1 if a < 0 else 0
        if a > 0:
            self[0] = a;
        elif a < -1:
            # Naver sucked on this. DV is undefined..
            # DV should be self.DV I guess
            self[0] = a # + DV;
        else:
            self.t = 0

    # a is a string
    # ex) 'b9d56fed8ad1f13997edc9396527704778bcdb2cb210d098ab2161a2072c4ab318848a2258426feda12b6ba77e12e4c8032d1887e13d7d1722747d72d3a58927bdd0bc6e40470497ece424507ca3a2da4bff30395c28c2d8951d6361c46d4bf65e9f6bf20adb76ed437121c8f872278c481a674227734474934cc8690953bec3';
    def fromString(self, a, b):
        if b == 16:
            c = 4
        elif b == 8:
            c =3
        elif b == 256:
            c = 8
        elif b == 2:
            c = 1
        elif b == 32:
            c = 5;
        elif b == 4:
            c = 2;
        else:
            print("Error?")
            return
        self.t = 0
        self.s = 0

        d = len(a)
        e = False
        f = 0

        d -= 1 # !IMPORTANT
        while d >= 0:
            if c == 8:
                try:
                    ad = int(a[d])
                    # Original code
                    # var g = a[d] & 255
                    # Naver sucked on this. Because, surprisingly,
                    # <char> & 255 always evaluates to 0
                    # https://stackoverflow.com/questions/22212103/
                    # bitwise-operations-on-strings-in-javascript
                    if ad > 10:
                        ad = 0
                    g = ad & 255
                except:
                    g = 0
            else:
                g = intAt(a, d)
            if g < 0:
                if a[d] == '-':
                    e = True
                d -= 1 # !IMPORTANT
                continue

            e = False
            if f == 0:
                self[self.t] = g
                self.t += 1
            elif f + c > self.DB:
                self[self.t-1] = self.get(self.t-1, 0) | (
                    g & (1 << self.DB - f) - 1) << f
                self[self.t-1] |= g >> self.DB -f
                self.t += 1
            else:
                self[self.t-1] |= g << f
            f += c
            if f >= self.DB:
                f -= self.DB
            d -=1 # !IMPORTANT
        # Naver sucked again
        try:
            a0 = int(a[0]) # if this cause no error
        except:
            a0 = 0
        if c == 0 and (a0 & 128) != 0:
            self.s = -1;
            if f > 0:
                self[self.t-1] |= (
                    1 << self.DB - f) - 1 << f
        self.clamp()
        if e:
            BigInteger.ZERO.subTo(self, self)

# Assuming Mozilla??
dbits = 28
BigInteger.DB = dbits
BigInteger.DM = (1 << dbits) - 1
BigInteger.DV = 1 << dbits

BigInteger.ZERO = BigInteger(None)
BigInteger.ZERO.fromInt(0)
BigInteger.ONE = BigInteger(None)
BigInteger.ONE.fromInt(1)


# a: str
# b: some number
def pkcs1pad2(a, b) :
    if (b < len(a) + 11):
        print("Message too long for RSA")
        return None
    # take care
    c = [None] * b
    d = len(a) - 1
    while (d >= 0 and b > 0):
        b -= 1
        c[b] = ord(a[d])
        d -= 1
    b -= 1
    c[b] = 0

    # take care
    while b > 2:
        b -= 1
        c[b] = randint(0, 255)
    b -= 1
    c[b] = 2;
    b -= 1
    c[b] = 0;
    return BigInteger(c)


class RSAKey:
    def __init__(self):
        self.n = None
        self.e = 0
        self.d = None
        self.p = None
        self.q = None
        self.dmp1 = None
        self.dmq1 = None
        self.coeff = None

    def setPublic(self, a, b):
        self.n = BigInteger(a, 16)
        self.e = int(b, 16)

    def doPublic(self, a):
        return
        pass

    def encrypt(self, a):
        b = pkcs1pad2(a, self.n.bitLength() + 7 >> 3)
        # Ignored
        # if (b == null) return null;
        c =
        pass
