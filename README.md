# Thi is a program for learning OOP

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install GemmyTheNerd
```

### วิธีเล่น

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from GemmyTheNerd import Student, SpecialStudent
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
	
```

โปรแกรมฝึกพิมพ์ "Pimsampas" version 0.1

<<< วิธีเล่น>>>>
- หลังจากเปิดเตรียมตัวพิมพ์ภายใน 5 วินาที
- พิมพ์ตามคำศัพท์สีเขียว พิมพ์ผิดไม่ได้ ต้องพิมพ์ให้ถูกเท่านั้น (ยากไหม 55)
- โปรแกรมจะนับ 1-60 แล้วจะหยุดเกมทันที
- โปรแกรมรอให้ผู้เล่นหยุดหายใจอีก 10 วินาทีแล้วเริ่มใหม่ 555
- ถ้าอยากดูแป้นพิมพ์ภาษาอังกฤษให้กด F1 ภาษาไทยกด F2
- สามารถเพิ่มคำศัพท์ได้ในไฟล์ data.csv ให้กด F5 เพื่อเปิดโฟลเดอร์ที่เก็บไฟล์ CSV
- แก้ไขไฟล์ CSV โดยใช้ Notepad (คลิกขวา Edit) 

(รอลุงอัพเดต version ใหม่จะทำให้ง่ายกว่านี้ 555)

<<< ปุ่มลัดต่างๆ >>>
- กดปุ่ม F1 เพื่อดูคีย์บอร์ดภาษาอังกฤษ 
- กดปุ่ม F2 เพื่อดูคีย์บอร์ดภาษาภาษาไทย
- กดปุ่ม F5 เพื่อเปิดโฟลเดอร์เก็บไฟล์ csv
- กดปุ่ม F10 เพื่อดูวิธีการเล่น
- กดปุ่ม F12 เล่นใหม่

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer

ปล. ขออภัย version 0.1 ลุงใช้เวลาพัฒนาแค่คืนเดียว เลยไม่ได้สมบูรณ์จ้าาาา
ปล2. ใน Mac เล่นได้ แต่ฟังชั่นคีย์บอร์ดยังติดปัญหา ไฟล์ data.csv อยู่ใน /Users/ชื่อusername
ปล3. Windows จะเก็บไฟล์ data.csv ไว้ในโฟลเดอร์ที่ติดตั้ง Python เช่น C:\Python38\data.csv หรือ แนะนำให้สร้างไฟล์ test.py แล้วพิมพ์ว่า import pimsampas แล้วรัน ไฟล์ data.csv จะอยู่ในโฟลเดอร์เดียวกับที่เซฟ


| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer] |
