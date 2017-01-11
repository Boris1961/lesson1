# Просто зверюшка
# Демонстрирует простейшие класс и объект
class Critter(object) :
	def talk(self) :
		print(self)
		print("Привет. Я зверюшка - экземпляр класса Critter.")

# основная часть
crit = Critter("Муму")
crit.talk()
input(" \ n \ nHaжмитe Enter. чтобы выйти.")
