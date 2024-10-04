stack=[]
com=input("Enter command to be done (push/pop/peek):")
def push(stack,x):
    stack.append(x)
def pop(stack):
    if len(stack)==0:
        print("Stack is empty!")
    else:
        print("the poped item in stack:",stack.pop())
def peek(stack):
    if len(stack)!=0:
        print("The first item in the stack",stack[-1])
    else:
        print("stack is empty!")
ans="y"
while (ans.lower()=="y"):
    if (com.lower()=="push"):
        a=int(input("Enter integer to be added:"))
        push(stack,a)
        print("stack:",stack)
    elif (com.lower()=="pop"):
        pop(stack)
        print("stack after pop:",stack)
    elif (com.lower()=="peek"):
        peek(stack)
    ans=input("Continue:(y/n):")
    if (ans.lower()!="y"):
        print("exiting stack!")
        break
    else:
        com=input("Enter command to be done (push/pop/peek):")