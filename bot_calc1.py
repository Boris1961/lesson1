def calc(exp_s):
    for s in "+-*/":
        opr=s
        opns=exp_s.split(s)
        if len(opns)==2:
            opn1=opns[0]
            opn2=opns[1]
            if not opn1.isdigit():
                return "Error: No digit"
            if not opn2.isdigit():
                return "Error: No digit"
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


    """

  while s(0)!='=':

  
    # обработка цифры
    if '.0123456789'.find(s[0]):
      pattern+='D'
      i-1
      while s[0:i].isdigit():
        i+=1
      c_word=s[0:i-1]
      if c_word.find('.'):
        types.append('REAL')
      else:
        types.append('INT')
      postfix.append(c_word)
      s=s[i:]



    elif s[0]=='(':
      pattern+='('
      stack_opr.append('(')
      brace_deep+=1



    elif s[0]==')':
      pattern+=')'
      brace_deep-=1
      if brace_deep<0:
        return "#error: braces no match"
      if stack_opr(-1)=='(':
        return "#warning: in braces no operation"
      while stack_opr[-1]!='(':
        postfix.append(stack_opr[-1])
        stack_opr=stack_opr[:-1]
      stack_opr=stack_opr[:-1]



    elif s[0]=='*':
      if s[1]=='*':
        postfix.append('**')
    

    elif s=='/':

    


    elif s=='+':

    


    elif s=='-':

    if not compatibility.find([pattern(-2:)]) :
      return "#error: lexical incompatibility"

"""

      



