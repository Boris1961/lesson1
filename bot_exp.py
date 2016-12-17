from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def compile_str_to_postfix(esource):


	# синтаксический анализ и разбиение на выражения на литералы

	pattern_scheme=""
	pattern_detail=""
	words=[]
	lex_incomp_sch = [ "D.", "D(", "DD", "()", "%%", "%)" ]
	lex_incomp_det = [ "(*", "(^", "(/" ]


	if esource.find('=')>=0:
		return('#error: sintax error')
	s=esource+'='

	brace_deep=0


	while s[0]!='=':


		if '.0123456789'.find(s[0])>0: 		#	обработка цифры

			pattern_scheme+='D'
			i=1
			while '.0123456789'.find(s[i])>=0:
				i+=1
			c_word=s[0:i]
			if c_word.count('.')==0:
				pattern_detail+=('I')
			elif c_word.count('.')==1:
				pattern_detail+=('R')
			else:
				return "#error: namber is wrong"



		elif s[0]=='(':
			pattern_scheme+='('
			pattern_detail+='('
			c_word='('
			brace_deep+=1
			


		elif s[0]==')':
			pattern_scheme+=')'
			pattern_detail+=')'
			brace_deep-=1
			if brace_deep<0:
				return "#error: braces no match"
			c_word=')'
			

		elif s[0]=='*':
			if s[1]=='*':
				pattern_scheme+='%'
				pattern_detail+='^'
				c_word='**'
			else:
				pattern_scheme+='%'
				pattern_detail+='*'
				c_word='*'


		elif s[0]=='/':

			pattern_scheme+='%'
			pattern_detail+='/'
			c_word='/'
		


		elif s[0]=='+':


			if len(words)==0 or words[-1]=='(':
				pattern_scheme+='D'
				pattern_detail+='I'	
				words.append('0')

			pattern_scheme+='%'
			pattern_detail+='+'
			c_word='+'
		


		elif s[0]=='-':

			if len(words)==0 or words[-1]=='(':
				pattern_scheme+='D'
				pattern_detail+='I'	
				words.append('0')

			pattern_scheme+='%'
			pattern_detail+='-'
			c_word='-'


		s=s[len(c_word):]
		words.append(c_word)


		if len(pattern_scheme)>1 and (lex_incomp_sch.count(pattern_scheme[-2]+pattern_scheme[-1])>0 or lex_incomp_det.count(pattern_detail[-2]+pattern_detail[-1])>0):
			return "#error: lexical shit"




	if brace_deep!=0:
		return "#error: braces no match"

	
	# компиляция списка литералов в постфиксную запись

	operators_priority  =  {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4}
	
	stack=[]
	postfix=[]


	for i in range(0,len(words)):

		c_word_det=pattern_detail[i]
		c_word_sch=pattern_scheme[i]

		if c_word_det=='I':
			postfix.append(int(words[i]))

		elif c_word_det=='R':
			postfix.append(float(words[i]))

		elif c_word_det=='(' :
			stack.append(c_word_det)

		elif c_word_det==')' :
			while stack[-1]!='(' :
				postfix.append(stack.pop())
			stack.pop()

		elif c_word_sch=='%':
			
			if len(stack)==0 or stack[-1]=='(' or operators_priority[c_word_det]>operators_priority[stack[-1]]:
				stack.append(c_word_det)
			else:
				while len(stack)>0 and stack[-1]!='(' :
					postfix.append(stack.pop())
				stack.append(c_word_det)



	while len(stack)>0:
		postfix.append(stack.pop(-1))

	return postfix


def execute_postfix(postfix):

	stack=[]
	
	for c_item in postfix :
		

		if not c_item in ['+', '-', '/', '*', '^'] :

			stack.append(c_item)
		
		else:
			
			opn2=stack.pop()
			opn1=stack.pop()
		
			if c_item=='+' :
				stack.append(opn1+opn2)

			elif c_item=='-' :
				stack.append(opn1-opn2)

			elif c_item=='*' :			
				stack.append(opn1*opn2)

			elif c_item=='/' :
				if opn2==0:
					return "#error: null division"

				stack.append(opn1/opn2)

			elif c_item=='^' :
				stack.append(opn1**opn2)

			else:
				return "#error: unknown"


	return stack.pop()


def main(): 
    updater = Updater("312039735:AAFzeUt-LKAnHjr9n58unpfO8_CAsxbCq70")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("abort", abort_bot))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def abort_bot(bot, update):
    print('Вызван /abort')
    bot.sendMessage(update.message.chat_id, text-'ухожу-ухожу-ухожу...')
    exit()

def talk_to_me(bot, update):
    print('Пришло сообщение: {}'.format(update.message.text))
    bot_command=update.message.text
    bot.sendMessage(update.message.chat_id, str(execute_postfix(compile_str_to_postfix(bot_command))))

if __name__ == '__main__':
	main()
