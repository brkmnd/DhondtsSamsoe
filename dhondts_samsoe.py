lister0 = {
          "A":829
        , "C":595
        , "F":335
        , "O":27
        , "V":654
        , "Ø":128
        }
lister1 = {
          "AFØ" :
              lister0["A"]
            + lister0["F"]
            + lister0["Ø"]
        , "COV" :
              lister0["C"]
            + lister0["O"]
            + lister0["V"]
        }

total_antal =   ( lister0["A"]
                + lister0["C"]
                + lister0["F"]
                + lister0["O"]
                + lister0["V"]
                + lister0["Ø"]
                )

lister = lister0

#antal_mandater = 11
antal_mandater = 6


valgforbund = ["A","F","Ø"]
#valgforbund = [l[0] for l in lister.items()]

res = []
res_lister_order = [l for l in lister if l in valgforbund]
res_lister = {l:[] for l in lister}

for l in lister.items():
    l_navn = l[0]
    l_s = l[1]
    if not (l_navn in valgforbund):
        continue
    for n0 in range(1,antal_mandater + 1):
        res.append((l_navn,l_s / n0))
        res_lister[l_navn].append(str(l_s) + "/" + str(n0) + " = " + str(round(l_s/n0)))

res.sort(reverse=True,key=lambda x: x[1])

ms = {l:0 for l in valgforbund}

def nmellemrum(i,r):
    res = ""
    if i < 10:
        res = str(i) + "  : "
    else:
        res = str(i) + " : "
    res += r[0] + ", " + str(round(r[1]))
    return res

for i in range(len(res)):
    r = res[i]
    rn = r[0]
    print(nmellemrum(i + 1,r))
    if i < antal_mandater:
        ms[rn] += 1

for m in ms.items():
    print(m[0] + "  : " + str(m[1]))

htmlUd = ""
for i in range(0,antal_mandater + 1):
    if i == 0:
        htmlUd += "<tr class='overskrift'>"
        htmlUd += "<td>"
        htmlUd += "</td>"
    else:
        htmlUd += "<tr>"
        htmlUd += "<td>"
        htmlUd += str(i)
        htmlUd += "</td>"
    for l in res_lister_order:
        if i == 0:
            htmlUd += "<td>"
            htmlUd += l
            htmlUd += "</td>"
        else:
            htmlUd += "<td>"
            htmlUd += res_lister[l][i - 1]
            htmlUd += "</td>"
    htmlUd += "</tr>"
    htmlUd += "\n"

print(htmlUd)

    
