
import re

str1 = 'HTTPS://HNWZZ.CN/00000003WR1DARP0003J,C00000517'
# s='*\/:?"<>|'
#
# str2 =re.findall(s,str1,re.S)
# print(str2)

# str1 = '\巴拉<1"!11【】>1*hgn/p:?|'    #样例
s='["HTTPS://HNWZZ.CN/"]'
a = re.findall(s, str1, re.S)
a = "".join(a)
print(a)