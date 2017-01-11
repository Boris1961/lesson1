# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object) :
		# Виртуальный питомец
	def __init__ (self,name) :
		print("Появилась на свет новая зверюшка!")
		# print("__name__" + __name__)
		# print("__bases__" + __bases__)
		# print("__module__" + __module__)
		# Применение атрибуrов
		self.name = name
	
	def __str__ (self):
		rep = "Объект класса Critter\n"
		rep +="имя: "+ self.name + "\n"
		return rep

	def talk(self):
		print("Привет. Меня зовут" + self.name + "\n")

# основная часть
crit1 = Critter("Бoбик")
crit1.talk()
crit2 = Critter( "Мурзик")
crit2.talk()
print("Bывoд объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name:")
print(crit1.name)



print("Critter.__dict__ ", Critter.__dict__)
print("Critter.__bases__ ", Critter.__bases__)
print("Critter.__module__ ", Critter.__module__)


print("crit1.__dict__ ", crit1.__dict__)

"""
print("__bases__", crit1.__bases__)
print("__module__", crit1.__module__)
"""

input("\n\nHaжмитe Enter. чтобы выйти.")
