import numpy as np

stackSize= int(input("Enter the size of Stack:-"))
stack = np.array([])
print("Stack operation keywords")
print("'push' 'pop' 'isEmpty' 'isFull' 'peek' 'count' 'change' 'display'")
print("To exit program just type 'exit'")
def push():
    global stack
    if isFull():
        print("Stack is overflow")
        return
    else:
        try:
            element = (input("Enter the element:-"))
            stack = np.append(stack, element)
            print("Element successfully added")
            return
        except:
            print("Enter the similar datatype element")
def pop():
    global stack
    if isEmpty():
        print("Stack is underflow")
        return
    else:
        stack = np.delete(stack, ((stack.size)-1))
        print("Element successfully removed")
        print(stack)
        return
def isEmpty():
    if stack.size == 0:
        return True
    else:
        return False
def isFull():
    if stack.size == stackSize:
        return True
    else:
        return False
def peek():
    global stack
    position = int(input("Give the position:-"))
    if position in range(stack.size):
        print("Element is:-", stack[position])
    else:
        print("Invalid position provided")
def count():
    global stack
    if isEmpty():
        print("stack is empty")
    else:
        print("Total number of element is:-", stack.size)
def change():
    global stack
    position = int(input("Give the position:-"))
    if position in range(stack.size) and not isEmpty():
        try:
            element = (input("Enter the element:-"))
            stack[position] = element
            print("Element successfully added")
            return
        except:
            print("Enter the similar datatype element")
    else:
        print("Invalid position provided")
        return
def diaplay():
    global stack
    print(stack)
while True:
    operationKeyWord = input("Enter the keyword of operation:-")
    if operationKeyWord == "exit":
        break
    elif operationKeyWord == "push":
        push()
    elif operationKeyWord == "pop":
        pop()
    elif operationKeyWord == "isEmpty":
        print("Yes") if isEmpty() else print("No")
    elif operationKeyWord == "isFull":
        print("Yes") if isFull() else print("No")
    elif operationKeyWord == "peek":
        peek()
    elif operationKeyWord == "count":
        count()
    elif operationKeyWord == "change":
        change()
    elif operationKeyWord == "display":
        diaplay()
    else:
        print("Enter appropriate keyword")