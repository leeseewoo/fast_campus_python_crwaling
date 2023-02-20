import re

# A B C D

s = '이 영화는 C등급입니다.'

print(s.split('이 영화는 ')[1].split('등급')[0])
print(re.findall(r'이 (..)는 (.)등급입니다.', s))
