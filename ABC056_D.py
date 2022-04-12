from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="056"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc070_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  A.sort()
  A=[A[i] for i in range(N) if A[i]<K]
  N=len(A)
  mask=(1<<(K+1))-1
  if N==0: print(0)
  else:
    l,r=-1,N
    while r-l>1:
      mid=(l+r)//2
      dp=1
      for i in range(N):
        if i==mid: continue
        dp=((dp<<A[i])|dp)&mask
      if (dp&((1<<K)-1))>>(K-A[mid])!=0: r=mid
      else: l=mid
    print(r)
  """ここから上にコードを記述"""

  print(test_case[__+1])