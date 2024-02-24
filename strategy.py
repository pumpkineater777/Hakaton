import random

def get(v, X, Y):
    if len(v) <= 5:
        sred = 0
        for i in range(len(v)):
            sred += v[i][1]
        sred /= len(v)
        if sred*5*1.5+Y < X:
            v.clear()
            return sred*5*1.5+Y >= X
    g = []
    for i in range(len(v)):
        g.append(v[i][1])
    g.sort()
    l11 = g[int(len(g)*0.35)]
    r11 = g[int(len(g)*0.85)]
    x11 = r11-l11+0.000001
    for i in range(len(v)):
        if v[i][1] > r11+x11*1.5:
            v[i][0] = 0
        elif v[i][1] < l11-x11*1.5:
            v[i][0] = 0
        else:
            v[i][0] = 1
    p = 0.98546987
    t = []
    k = 1
    x=max(0,len(v)-21)-1
    l = v[len(v)-1][1]
    r = -1
    for i in range(len(v)-1,x, -1):
        t.append([k*v[i][0], v[i][1]])
        k *= p
        l = min(l, v[i][1])
        r = max(r, v[i][1])

    r *= 1.04

    l *= 0.96
    r += 0.0000001
    l -= 0.0000001
    d = 15
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
    cnt = int(cnt)
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
                cnt1 += blok[j]
                if cnt1 >= num_bl:
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
                cnt1 += blok[j]
                if cnt1 >= num_bl:
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
    v.clear()
    t.clear()
    g.clear()
    return loc_Y > loc_Y_zavtra