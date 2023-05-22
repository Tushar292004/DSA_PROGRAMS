Operators = set(['+', '-', '*', '/', '(', ')', '^'])
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infix_postfix(expression): 

    stack = [] 
    postfix = ''    
    for i in expression:
        if i not in Operators: 
            postfix+= i

        elif i=='(': 
            stack.append('(')

        elif i==')':
            while stack and stack[-1]!= '(':
                postfix+=stack.pop()
            stack.pop()

        else: 
            while stack and stack[-1]!='(' and Priority[i]<=Priority[stack[-1]]:
                postfix+=stack.pop()
            stack.append(i)

    while stack:
        postfix+=stack.pop()
    return postfix

expression = input('Enter infix expression ')
print('infix notation: ',expression)
print('postfix notation: ',infix_postfix(expression))

#OUTPUT 1
# Enter infix expression A+B
# infix notation:  A+B
# postfix notation:  AB+

# OUTPUT 2
# Enter infix expression A+B+C+(D*E)
# infix notation:  A+B+C+(D*E)
# postfix notation:  AB+C+DE*+