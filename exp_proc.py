def exp_to_postfix(source):


	s=source+'='

	# проход 1

	while s(0)!='=':

	
		#	обработка цифры
		if '.0123456789'.find(s(0)):
			pattern+='D'
			i-1
			while s[0:i].isdigit():
				i+=1
			words.append(s[0:i-1])
			if words(-1).find('.'):
				types.append('INT')
			else:
				types.append('REAL')
			s=s[i:]


		elif s=='(':
			pattern+='('
			brace_deep+=1

		elif s==')':
			pattern+='('
			brace_deep-=1
			if brace_deep<0:
				return "#error: braces no match"


		elif s=='*':

		elif s=='/':

		elif s=='+':

		elif s=='-':

		if not compatibility.find([pattern(-2:)]) :
			return "#error: lexical incompatibility"

			


