from pprint import pprint

class Person:
	def __init__(self, name=None, age=None):
		self.name = name if name != None else 'None'
		self.age = age if age != None else 0

	def introduce(self):
		print('My name is {}. I\'m {} year{} old.'.format(self.name, self.age, 's' if self.age > 1 else ''))

def main():
	p = Person()
	p.introduce()

	p = Person('AAA', 20)
	p.introduce()

	



if __name__ == "__main__":
	main()