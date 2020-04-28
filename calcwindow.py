from PyQt5.QtWidgets import QMainWindow
from ui_calc_window import Ui_Calculator


class CalcWindow(QMainWindow):
	def __init__(self):
		super(CalcWindow, self).__init__()
		self.ui = Ui_Calculator()
		self.ui.setupUi(self)
		self.ui.one.clicked.connect(self.buttonPressed)
		self.ui.two.clicked.connect(self.buttonPressed)
		self.ui.three.clicked.connect(self.buttonPressed)
		self.ui.four.clicked.connect(self.buttonPressed)
		self.ui.five.clicked.connect(self.buttonPressed)
		self.ui.six.clicked.connect(self.buttonPressed)
		self.ui.seven.clicked.connect(self.buttonPressed)
		self.ui.eight.clicked.connect(self.buttonPressed)
		self.ui.nine.clicked.connect(self.buttonPressed)
		self.ui.zero.clicked.connect(self.buttonPressed)
		self.ui.dec.clicked.connect(self.buttonPressed)
		self.ui.div.clicked.connect(self.buttonPressed)
		self.ui.mul.clicked.connect(self.buttonPressed)
		self.ui.plus.clicked.connect(self.buttonPressed)
		self.ui.minus.clicked.connect(self.buttonPressed)
		self.ui.equals.clicked.connect(self.buttonPressed)
		self.ui.ac.clicked.connect(self.buttonPressed)
		self.ui.neg.clicked.connect(self.buttonPressed)
		self.plus = 0
		self.minus = 0
		self.equals = 0
		self.div = 0
		self.mul = 0
		self.hold1 = 0
		self.hold2 = 0


	def buttonPressed(self):
		clicked = self.sender()
		numbers = [clicked == self.ui.one,
					clicked == self.ui.two,
					clicked == self.ui.three,
					clicked == self.ui.four,
					clicked == self.ui.five,
					clicked == self.ui.six,
					clicked == self.ui.seven,
					clicked == self.ui.eight,
					clicked == self.ui.nine,
					clicked == self.ui.zero]
		if any(numbers):
			if self.ui.label.text() == "0":
				self.ui.label.setText('')
			self.ui.label.setText(self.ui.label.text() + clicked.text())
		if clicked == self.ui.plus:
			self.plus = 1
			hold = self.ui.label.text()
			self.hold1 = int(hold)
		if clicked == self.ui.minus:
			self.minus = 1
			hold = self.ui.label.text()
			self.hold1 = int(hold)
		if clicked == self.ui.mul:
			self.mul = 1
			hold = self.ui.label.text()
			self.hold1 = int(hold)
		if clicked == self.ui.div:
			self.div = 1
			hold = self.ui.label.text()
			self.hold1 = int(hold)
		if clicked == self.ui.equals:
			if self.plus == 1:
				self.plus = 0
				hold = self.ui.label.text()
				self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 + self.hold2))
			if self.minus == 1:
				self.minus = 0
				hold = self.ui.label.text()
				self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 - self.hold2))
			if self.mul == 1:
				self.mul = 0
				hold = self.ui.label.text()
				self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 * self.hold2))
			if self.div == 1:
				self.div = 0
				hold = self.ui.label.text()
				self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 // self.hold2) + '.' \
										+ str(self.hold1 % self.hold2))
		if clicked == self.ui.ac:
			self.plus = 0
			self.minus = 0
			self.equals = 0
			self.div = 0
			self.mul = 0
			self.hold1 = 0
			self.hold2 = 0
			self.ui.label.setText('0')
		if clicked == self.ui.neg:
			hold = self.ui.label.text()
			self.hold1 = float(hold)
			self.ui.label.setText(str(self.hold1 * -1))
