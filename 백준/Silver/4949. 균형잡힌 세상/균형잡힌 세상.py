s=''
while True:
    s= list(input())
    if s == ['.']:
        break
    stack=[]
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append('[')
        elif i == ')' and  stack and stack[-1] == '(':
            stack.pop()
        elif i ==  ')' and (not stack or stack[-1] != '('):
            stack.append('no')
            break
        elif i == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif i == ']' and (not stack or stack[-1] != '['):
            stack.append('no')
            break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
