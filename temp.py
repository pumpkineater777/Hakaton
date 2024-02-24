# v-кэшбек
# X-бюджет
# Y-затраченно

import random


# кешбек, бюджет, сколько потреченно
def get(v, Y, X):
    p = 0.9
    t = []
    x = max(0, len(v)-20)-1
    k = 1
    l = v[len(v)-1][1]
    r = -1
    for i in range(len(v)-1, x, -1):
        t.append([k, v[i][1]])
        k *= p
        l = min(l, v[i][1])
        r = max(r, v[i][1])
    d = 5
    shag = (r-l)/d
    blok = []
    for i in range(0, d):
        blok.append(0)
    cnt = 0
    for i in range(0, len(t)):
        bl = int((t[i][1]-l)//shag)
        if bl >= d:
            bl -= 1
        cnt += t[i][0]
        blok[bl] += t[i][0]
    cnt *= 100
    cnt=int(cnt)
    n = 10000
    loc_Y = 0
    loc_Y_zavtra = 0
    for _ in range(n):
        loc_Y1 = Y
        loc_Y1_zavtra = Y
        for i in range(5):

            num_bl = random.randint(0, cnt)
            num_bl /= 100
            cnt1 = 0
            for j in range(d):
                if cnt1 <= num_bl:
                    num_bl = j
                    break
            l1 = l+num_bl*d
            l1 *= 100
            r1 = l+(num_bl+1)*d
            r1 *= 100
            r1 -= 1
            l1 = int(l1)
            r1 = int(r1)
            chis = random.randint(l1, r1)
            chis /= 100
            loc_Y1 += chis
        for i in range(6):
            num_bl = random.randint(0, cnt)
            num_bl /= 100
            cnt1 = 0
            for j in range(d):
                if cnt1 <= num_bl:
                    num_bl = j
                    break
            l1 = l + num_bl * d
            l1 *= 100
            r1 = l + (num_bl + 1) * d
            r1 *= 100
            r1 -= 1
            l1 = int(l1)
            r1 = int(r1)
            chis = random.randint(l1, r1)
            chis /= 100
            loc_Y1_zavtra += chis
        ans1 = min(loc_Y1, X)
        ans1 = ans1-5*(loc_Y1-ans1)
        ans2 = min(loc_Y1_zavtra, X)
        ans2 = ans2-5*(loc_Y1_zavtra-ans2)
        loc_Y += ans1
        loc_Y_zavtra += ans2
    loc_Y /= n
    loc_Y_zavtra /= n
    return loc_Y < loc_Y1_zavtra


v = [[1, 34], [2, 179.63], [3, 137.81], [4, 103.13]]


Y = 454.57
X = 1250.14
print(get(v, X, Y))
