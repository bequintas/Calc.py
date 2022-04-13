import math

def operate(a, b, oper):
    if(oper == "+"):
        return a + b
    if(oper == "-"):
        return a - b
    if(oper == "*"):
        return a * b
    if(oper == "x"):
        return a * b
    if(oper == "/"):
        return a / b


while(1):
    op = str(input("Insira a operação: "))    
    n1 = float(input("Inserir número: "))
    n2 = float(input("Inserir número: "))
    print("RESULTADO:>>  ", operate(n1, n2, op))
