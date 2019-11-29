Kota = ("Jakarta","Bogor","Depok","Bandung","Semarang","Yogyakarta","Surabaya","Malang")
visit = {
    "Jakarta" : False,
    "Bogor" : False,
    "Depok" : False,
    "Bandung" : False,
    "Semarang" : False,
    "Yogyakarta" : False,
    "Surabaya" : False,
    "Malang" : False,

}
provider = ("NCS","RPX","SICEPAT","BLIBLI","NINJA","POS","JNE")
price = (11000,14500,13000,15000,13000,15000,12000)
use = {
    "NCS" : False,
    "RPX" : False,
    "SICEPAT" : False,
    "BLIBLI" : False,
    "NINJA" : False,
    "POS" : False,
    "JNE" : False
}
edge = {
    # kota x ke kota x
    ("Jakarta","Jakarta","BLIBLI") : 1,
    ("Jakarta","Jakarta","NINJA") : 1,
    ("Jakarta","Jakarta","POS") : 1,
    ("Jakarta","Jakarta","JNE") : 1,
    ("Bandung","Bandung","RPX") : 1,
    ("Bandung","Bandung","BLIBLI") : 1,
    ("Bandung","Bandung","NINJA") : 1,
    ("Bandung","Bandung","JNE") : 1,
    ("Bogor","Bogor","SICEPAT") : 1,
    ("Bogor","Bogor","NINJA") : 1,
    ("Depok","Depok","SICEPAT") : 1,
    ("Depok","Depok","POS") : 1,
    ("Semarang","Semarang","NCS") : 1,
    ("Semarang","Semarang","BLIBLI") : 1,
    ("Semarang","Semarang","POS") : 1,
    ("Semarang","Semarang","JNE") : 1,
    ("Yogyakarta","Yogyakarta","SICEPAT") : 1,
    ("Yogyakarta","Yogyakarta","POS") : 1,
    ("Yogyakarta","Yogyakarta","JNE") : 1,
    ("Surabaya","Surabaya","NCS") : 1,
    ("Surabaya","Surabaya","RPX") : 1,
    ("Surabaya","Surabaya","SICEPAT") : 1,
    ("Malang","Malang","RPX") : 1,
    # kota x ke kota y
    ("Jakarta","Bandung","BLIBLI") : 1,
    ("Jakarta","Bandung","NINJA") : 1,
    ("Jakarta","Bandung","JNE") : 1,
    ("Jakarta","Bogor","NINJA") : 1,
    ("Jakarta","Depok","POS") : 1,
    ("Jakarta","Semarang","BLIBLI") : 1,
    ("Jakarta","Semarang","POS") : 1,
    ("Jakarta","Semarang","JNE") : 1,
    ("Jakarta","Yogyakarta","POS") : 1,
    ("Jakarta","Yogyakarta","JNE") : 1,
    ("Bandung","Jakarta","BLIBLI") : 1,
    ("Bandung","Jakarta","NINJA") : 1,
    ("Bandung","Jakarta","JNE") : 1,
    ("Bandung","Bogor","NINJA") : 1,
    ("Bandung","Semarang","BLIBLI") : 1,
    ("Bandung","Semarang","JNE") : 1,
    ("Bandung","Yogyakarta","JNE") : 1,
    ("Bandung","Surabaya","RPX") : 1,
    ("Bandung","Malang","RPX") : 1,
    ("Bogor","Jakarta","NINJA") : 1,
    ("Bogor","Bandung","NINJA") : 1,
    ("Bogor","Depok","SICEPAT") : 1,
    ("Bogor","Yogyakarta","SICEPAT") : 1,
    ("Bogor","Surabaya","SICEPAT") : 1,
    ("Depok","Jakarta","POS") : 1,
    ("Depok","Bogor","SICEPAT") : 1,
    ("Depok","Semarang","POS") : 1,
    ("Depok","Yogyakarta","SICEPAT") : 1,
    ("Depok","Yogyakarta","POS") : 1,
    ("Depok","Surabaya","SICEPAT") : 1,
    ("Semarang","Jakarta","BLIBLI") : 1,
    ("Semarang","Jakarta","POS") : 1,
    ("Semarang","Jakarta","JNE") : 1,
    ("Semarang","Bandung","BLIBLI") : 1,
    ("Semarang","Bandung","JNE") : 1,
    ("Semarang","Depok","POS") : 1,
    ("Semarang","Yogyakarta","POS") : 1,
    ("Semarang","Yogyakarta","JNE") : 1,
    ("Semarang","Surabaya","NCS") : 1,
    ("Yogyakarta","Jakarta","POS") : 1,
    ("Yogyakarta","Jakarta","JNE") : 1,
    ("Yogyakarta","Bandung","JNE") : 1,
    ("Yogyakarta","Bogor","SICEPAT") : 1,
    ("Yogyakarta","Depok","SICEPAT") : 1,
    ("Yogyakarta","Depok","POS") : 1,
    ("Yogyakarta","Semarang","POS") : 1,
    ("Yogyakarta","Semarang","JNE") : 1,
    ("Yogyakarta","Surabaya","SICEPAT") : 1,
    ("Surabaya","Bandung","RPX") : 1,
    ("Surabaya","Bogor","SICEPAT") : 1,
    ("Surabaya","Depok","SICEPAT") : 1,
    ("Surabaya","Semarang","NCS") : 1,
    ("Surabaya","Yogyakarta","SICEPAT") : 1,
    ("Surabaya","Malang","RPX") : 1,
    ("Malang","Bandung","RPX") : 1,
    ("Malang","Surabaya","RPX") : 1
}
path = []
k = 0
# masukin path x to x, dan path x to y dengan 1 edge
for i in edge:
    k += 1
    path.append([i[0],i[1],[i[2],],[]])
    # print(k,":",i[0],",",i[1],",",i[2])

def DFS(head,tail,vst,used,prov):
    # print(head,tail,prov)
    for x in edge :
        if(x[0] == tail and x[1] != tail and vst[x[1]] == False and used[x[2]] == False):
            global k
            k += 1
            vst[x[1]] = True
            used[x[2]] = True
            prov.append(x[2])
            if len(prov) == 2 : 
                path.append( [head,x[1],prov,[tail]] )
            # print(k,":",head,",",x[1],",",end = " ")
            # for i in prov:
            #     print(i, end = " ")
            # print()
            # print(head,x[1],prov)
                DFS(head,x[1],vst,used,prov)
            vst[x[1]] = False
            used[x[2]] = False
            prov.pop()

for i in Kota:
    visit[i] = True
    for x in edge:
        if(x[0] == i and x[1] != i):
            visit[x[1]] = True
            use[x[2]] = True
            DFS(x[0],x[1],visit,use,[x[2]])
            visit[x[1]] = False
            use[x[2]] = False
    visit[i] = False

Order = []
n = int(input())
for i in range(n):
    inp = input().split()
    Order.append((inp[0],inp[1],int(inp[2]),float(inp[3])))

Condition = {}
for i in range(len(Order)) :
    for j in range(len(path)):
        Condition[(i,j)] = ((Order[i][0] == path[j][0]) and (Order[i][1] == path[j][1]))
# Order.sort()
currW = {
    "NCS" : 0.0,
    "RPX" : 0.0,
    "SICEPAT" : 0.0,
    "BLIBLI" : 0.0,
    "NINJA" : 0.0,
    "POS" : 0.0,
    "JNE" : 0.0
}
currR = {
    "NCS" : 0,
    "RPX" : 0,
    "SICEPAT" : 0,
    "BLIBLI" : 0,
    "NINJA" : 0,
    "POS" : 0,
    "JNE" : 0
}
capacity = {
    "NCS" : 65,
    "RPX" : 100,
    "SICEPAT" : 100,
    "BLIBLI" : 375,
    "NINJA" : 250,
    "POS" : 320,
    "JNE" : 630
}
maxrequest = {
    "NCS" : 150,
    "RPX" : 150,
    "SICEPAT" : 600,
    "BLIBLI" : 800,
    "NINJA" : 1350,
    "POS" : 1470,
    "JNE" : 3500
}
price = {
    "NCS" : 11000,
    "RPX" : 14500,
    "SICEPAT" : 13000,
    "BLIBLI" : 15000,
    "NINJA" : 13000,
    "POS" : 15000,
    "JNE" : 12000
}
dp = {}
def pickPath(i,cost,sent):
    global n,path,Order,Condition,currW,currR,capacity,maxrequest,price,dp
    if i >= n : return [cost,sent]
    if ((i,currW["NCS"],currW["RPX"],currW["SICEPAT"],currW["BLIBLI"],currW["NINJA"],currW["POS"],currW["JNE"],currR["NCS"],currR["RPX"],currR["SICEPAT"],currR["BLIBLI"],currR["NINJA"],currR["POS"],currR["JNE"])) in dp : 
        return dp[(i,currW["NCS"],currW["RPX"],currW["SICEPAT"],currW["BLIBLI"],currW["NINJA"],currW["POS"],currW["JNE"],currR["NCS"],currR["RPX"],currR["SICEPAT"],currR["BLIBLI"],currR["NINJA"],currR["POS"],currR["JNE"])]
    ans = [cost,sent]
    for j in range(len(path)):
        if ((i,j) in Condition and Condition[(i,j)]):
            bisa = True
            for k in path[j][2]:
                if (currW[k]+Order[i][3] > capacity[k] or currR[k]+Order[i][2] > maxrequest[k]):
                    bisa = False
            if bisa:
                updtCost = 0
                for k in path[j][2]:
                    currW[k] += Order[i][3]
                    currR[k] += Order[i][2]
                    updtCost += Order[i][3] * price[k]
                tmp = pickPath(i+1,cost + updtCost,sent+1)
                if (tmp[1] > ans[1] or (tmp[1] == ans[1] and tmp[0] < ans[0])) : 
                    ans = tmp
                for k in path[j][2]:
                    currW[k] -= Order[i][3]
                    currR[k] -= Order[i][2]
    tmp = pickPath(i+1,cost,sent)
    if (tmp[1] > ans[1] or (tmp[1] == ans[1] and tmp[0] < ans[0])) : 
        ans = tmp
    print(ans)
    dp[(i,currW["NCS"],currW["RPX"],currW["SICEPAT"],currW["BLIBLI"],currW["NINJA"],currW["POS"],currW["JNE"],currR["NCS"],currR["RPX"],currR["SICEPAT"],currR["BLIBLI"],currR["NINJA"],currR["POS"],currR["JNE"])] = ans
    return dp[(i,currW["NCS"],currW["RPX"],currW["SICEPAT"],currW["BLIBLI"],currW["NINJA"],currW["POS"],currW["JNE"],currR["NCS"],currR["RPX"],currR["SICEPAT"],currR["BLIBLI"],currR["NINJA"],currR["POS"],currR["JNE"])]

ans = pickPath(0,0,0)
print(ans)
# for i in range (n-1):
#     tmp = pickPath(i+1,0,0)
#     print(tmp)
#     if (tmp[1] > ans[1] or (tmp[1] == ans[1] and tmp[0] < ans[0])) : 
#         ans = tmp
print("Cost termurah adalah =",ans[0],"dengan jumlah order terkirim",ans[1])
