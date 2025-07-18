r=31
M = 1234567891


n = int(input())
alpha = list(input())


alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(alpha)):
    alpha[i] = alphabet_list.index(alpha[i]) + 1
    
    
output = 0
for i in range(n):
    output += (alpha[i] * (r ** i))%M
print(output % M)

