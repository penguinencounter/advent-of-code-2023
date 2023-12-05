import re;p,m={},{};f=lambda x:set(re.findall(r'\d+',x));s=p.__setitem__
for i,k in enumerate(open(0).readlines()):p[k]=1;m[i+1]=k
for k,v in p.items():n,l,r=re.search(r'(\d+):(.*)\|(.*)',k).groups();_=(
a:=int(n),[s(m[x+1],p[m[x+1]]+v)for x in range(a,a+len(f(l)&f(r)))])
print(sum(p.values()))