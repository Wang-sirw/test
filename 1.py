import jieba
f = open("C:\\Users\\18149\\Desktop\\沉默的羔羊.txt",encoding = 'UTF-8')
ls = jieba.lcut(f.read())
dict = {}
for i in ls:
    dict[i] = dict.get(i,0) + 1
maxc = 0
maxw = ""
for s in dict:
    if dict[s] > maxc and len(s) >2:
        maxc = dict[s]
        maxw = s
    if dict[s] == maxc and len(s) > 2 and s > maxw:
        maxw = s
print(maxw)
f.close()
