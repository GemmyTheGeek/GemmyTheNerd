class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		self.AddEXP(10)

	def Hello(self):
			print('Hello World! My name is {}!'.format(self.name))

	def Coding(self):
		print('{}: Currently coding...'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print('- {} has {} EXP'.format(self.name,self.exp))
		print('- Learned {} times'.format(self.lesson))

	def AddEXP(self, score):
		self.exp += score


class SpecialStudent(Student):

	def __init__(self,name,father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill Gates', 'Thomas Edison']
		if father in mafia:
			self.exp += 100

	def AddEXP(self,score):
		self.exp += (score * 3)
		self.lessson += 1

	def AskEXP(self,score=10):
		print('*Holding Gun* Gimme some EXP!')
		self.AddEXP(score)

print(__name__)

if __name__ == '__studentclass__':

	print('===== 1 Jan =====')
	