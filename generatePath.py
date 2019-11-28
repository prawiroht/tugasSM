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
    path.append([i[0],i[1],[i[2],]])
    print("Path ke",k,":",i[0],",",i[1],",",i[2])

def DFS(head,tail,vst,used,prov):
    # print(head,tail,prov)
    for x in edge :
        if(x[0] == tail and x[1] != tail and vst[x[1]] == False and used[x[2]] == False):
            global k
            k += 1
            vst[x[1]] = True
            used[x[2]] = True
            prov.append(x[2])
            path.append( [head,x[1],prov] )
            print("Path ke",k,":",head,",",x[1],",",prov)
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

# print(path)