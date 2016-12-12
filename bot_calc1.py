def calc(exp_s):
   for s in "+-*/":
       opr=s
       opns=exp_s.split(s)
       if len(opns)==2:
           opn1=opns[0]
           opn2=opns[1]
           for n in range(0, len(opn1)-1):
               if "0123456789".find(opn1[n])==-1:
                   return "Error"
           for n in range(0, len(opn2)-1):
               if "0123456789".find(opn2[n])==-1:
                   return "Error"
           opn1=int(opn1)
           opn2=int(opn2)
           if opr=="+":
               return str(opn1+opn2)
           elif opr=="-":
               return str(opn1-opn2)
           elif opr=="/":
               if opn2==0:
                   return "Error: деление на ноль."
               return str(opn1/opn2)
           elif opr=="*":
               return str(opn1*opn2)

   return "Error"  

if __name__ == '__main__':
    print(calc("125*56"))
