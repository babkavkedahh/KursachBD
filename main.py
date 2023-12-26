import sys
import time

from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):
   def __init__(self):
      super().__init__()
      self.initUI()

   def initUI(self):
      self.setWindowTitle("Проектировачный расчет цепных передач")
      self.setFixedWidth(500)
      self.label1 = QLabel('&a`', self)
      self.label2 = QLabel('&N ', self)
      self.label3 = QLabel('&z2', self)
      self.label4 = QLabel('&n1 ', self)
      self.label5 = QLabel('&j ', self)
      self.label6 = QLabel('&tp ', self)
      self.LineEdit1 = QLineEdit(self)
      self.LineEdit2 = QLineEdit(self)
      self.LineEdit3 = QLineEdit(self)
      self.LineEdit4 = QLineEdit(self)
      self.LineEdit5 = QLineEdit(self)
      self.LineEdit6 = QLineEdit(self)
      self.label1.setBuddy(self.LineEdit1)
      self.label2.setBuddy(self.LineEdit2)
      self.label3.setBuddy(self.LineEdit3)
      self.label4.setBuddy(self.LineEdit4)
      self.label5.setBuddy(self.LineEdit5)
      self.label6.setBuddy(self.LineEdit6)

      self.label11 = QLabel('Введите число', self)
      self.label21 = QLabel('Введите число', self)
      self.label31 = QLabel('Введите число', self)
      self.label41 = QLabel('Введите число', self)
      self.label51 = QLabel('Введите число', self)
      self.label61 = QLabel('Введите число', self)


      mainLayout = QGridLayout(self)
      mainLayout.addWidget(self.label1, 0, 0)
      mainLayout.addWidget(self.label2, 1, 0)
      mainLayout.addWidget(self.label3, 2, 0)
      mainLayout.addWidget(self.label4, 3, 0)
      mainLayout.addWidget(self.label5, 4, 0)
      mainLayout.addWidget(self.label6, 5, 0)
      mainLayout.addWidget(self.LineEdit1, 0, 1, 1, 2)
      mainLayout.addWidget(self.LineEdit2, 1, 1, 1, 2)
      mainLayout.addWidget(self.LineEdit3, 2, 1, 1, 2)
      mainLayout.addWidget(self.LineEdit4, 3, 1, 1, 2)
      mainLayout.addWidget(self.LineEdit5, 4, 1, 1, 2)
      mainLayout.addWidget(self.LineEdit6, 5, 1, 1, 2)
      mainLayout.addWidget(self.label11, 0, 3)
      mainLayout.addWidget(self.label21, 1, 3)
      mainLayout.addWidget(self.label31, 2, 3)
      mainLayout.addWidget(self.label41, 3, 3)
      mainLayout.addWidget(self.label51, 4, 3)
      mainLayout.addWidget(self.label61, 5, 3)

      self.btn = QPushButton('&Рассчитать')
      self.btn.setEnabled(False)
      mainLayout.addWidget(self.btn, 6, 1)
      self.LineEdit1.textEdited.connect(self.my_slot_function1)
      self.LineEdit2.textEdited.connect(self.my_slot_function2)
      self.LineEdit3.textEdited.connect(self.my_slot_function3)
      self.LineEdit4.textEdited.connect(self.my_slot_function4)
      self.LineEdit5.textEdited.connect(self.my_slot_function5)
      self.LineEdit6.textEdited.connect(self.my_slot_function6)

      self.btn.clicked.connect(self.buttonClicked)

      self.output = QLabel("Ответ:")
      mainLayout.addWidget(self.output, 6, 2)
      self.label71 = QLabel('шаг цепи t =', self)
      self.label72 = QLabel('число зубьев ведущей звёздочки z1 = ', self)
      mainLayout.addWidget(self.label71, 7, 0)
      mainLayout.addWidget(self.label72, 7, 2)

   def buton(self):
      if self.label11.text() == '' and self.label21.text() == '' and self.label31.text() == '' and self.label41.text() == '' and self.label51.text() == '' and self.label61.text() == '':
         self.btn.setEnabled(True)
      else:
         self.btn.setEnabled(False)
   def my_slot_function1(self,text):
      if not (text.isdigit()):
         self.label11.setText('Написано не число')
      else:
         self.label11.setText('')
      self.buton()
   def my_slot_function2(self,text):
      if not (text.isdigit() or text == ''):
            self.label21.setText('Написано не число')
      else:
         self.label21.setText('')
      self.buton()

   def my_slot_function3(self,text):
      if not (text.isdigit() or text == ''):
            self.label31.setText('Написано не число')
      else:
         self.label31.setText('')
      self.buton()

   def my_slot_function4(self,text):
      if not (text.isdigit() or text == ''):
            self.label41.setText('Написано не число')
      else:
         self.label41.setText('')
      self.buton()


   def my_slot_function5(self, text):
      if not (text.isdigit() or text == ''):
            self.label51.setText('Написано не число')
      else:
         self.label51.setText('')
      self.buton()

   def my_slot_function6(self,text):
      if not (text.isdigit() or text == ''):
            self.label61.setText('Написано не число')
      else:
         self.label61.setText('')
      self.buton()


   def buttonClicked(self):
      self.delta_a = float(self.LineEdit1.text())
      self.n= float(self.LineEdit2.text())
      self.z2=float(self.LineEdit3.text())
      self.n1=float(self.LineEdit4.text())
      self.j= float(self.LineEdit5.text())
      self.tp = float(self.LineEdit6.text())

      self.t = T(self.delta_a, self.n, self.n1, self.j)
      self.label71 = QLabel(f' {self.t}', self)
      self.z1 = Z1(self.n1,self.t)
      self.label72 = QLabel(f'z1 = {self.z1}', self)
      self.mainLayout.addWidget(self.output, 7, 0)
      self.mainLayout.addWidget(self.output, 7, 2)
      self.a = a(lamb(zc(self.delta_a, self.tp, self.z1, self.z2), self.z1, self.z2, self.t), delta(self.z2, self.z1, self.t))
      self.output.setText(f'Ответ: {self.a}')


Ky = lambda n1: 10*((n1/10)**(1/9))
Kv = lambda n1:(n1/10)**(2/3)
Ky_v = lambda n1: i if ((i:=Ky(n1))>(j:=Kv(n1))) else (i:=j)
Km = lambda j: 1 if j==1 else 1.7 if j==2 else 2.5 if j==3 else 3

def T(delta_a,N,n1,j):
   min_t = 30.5*(N*Ky_v(n1)/(n1*Km(j)))**(1/3)
   minim = i if((i:=delta_a/80) > min_t) else min_t
   for x in [12.7,15.875,19.05,25.4,31.75,38.1,44.45,50.8]:
      if minim < x < delta_a/30:
         return x
   time.sleep(1000)#нет подходящего числа среди госта

def Z1(n1,t):
   mass = [
            [12.7,2780,2900,3000],
            [15,875,2000,2070,2150],
            [19.05,1520,1580,1640],
            [25.4,1000,1030,1070],
            [31.75,725,750,780],
            [38.1,540,560,580,],
            [44.45,430,445,460,],
            [50.8,350,365,375]
           ]

   for x in mass:
      if x[0] != t:
         mass.pop(0)
   if n1 <mass[0][1]:
      return 20
   elif n1<mass[0][2]:
      return 25
   else:
      return 30

zc = lambda delta_a,tp,z1,z2: ((2*delta_a)/tp) + ((z1+z2)/2) + ((z2-z1)**2)*tp/(40*delta_a)
lamb = lambda zc,z1,z2,t: zc*t-(t*(z1+z2)/2)
delta = lambda z2,z1,t: (z2-z1)*t/6.28
a = lambda x,y:(x+((x**2)-8*(y**2))**0.5)/4

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QLabelBuddy()
   main.show()

   sys.exit(app.exec_())

