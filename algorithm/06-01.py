SIZE = 5
stack= [None for _ in range(SIZE)]
top = -1

#push
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥',stack)

# pop
data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)
print('바닥',stack)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)
print('바닥',stack)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)
print('바닥',stack)