# count = 0
# 반복문 : 문자를 하나씩(앞이든 뒤든) 뽑는다.
#         뽑은 문자가 다음 문자와 같으면, continue
#         다르면, 조건문 : 리스트에 그 문자가 있는가? => 있으면 반복문 탈출
#                                               => 없으면 리스트에 문자 추가
#         조건문 : 문자열 길이가 0이면 => count += 1

count = 0
def checker(word):
    global count
    ref = len(word)
    letters = []
    for i in range(ref):
        if letters.__contains__(word[i]) : break
        if i == ref - 1 : count += 1; break
        if word[i] == word[i+1] : continue
        letters.append(word[i])


n = int(input())
for i in range(n): checker(input())
print(count)
