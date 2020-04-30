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
		self.ui.neg.clicked.connect(self.buttonPressed)		# connections for all presses
		self.plus = 0
		self.minus = 0
		self.equals = 0
		self.div = 0
		self.mul = 0
		self.hold1 = 0
		self.hold2 = 0
		self.dec = 0
		self.action = 0										# flags for control

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
					clicked == self.ui.zero]				# set of all number presses
		if any(numbers):
			if self.action == 0:							# if number pressed with no math
				if self.ui.label.text() == "0":
					self.ui.label.setText('')
				self.ui.label.setText(self.ui.label.text() + clicked.text())
			else:											# if number pressed with math
				self.ui.label.setText('')
				self.ui.label.setText(self.ui.label.text() + clicked.text())
				self.action = 0
		if clicked == self.ui.plus:
			self.plus = 1
			self.action = 1
			hold = self.ui.label.text()
			if '.' in hold:
				self.dec = 1
			if self.dec == 1:								# control for dec
				self.hold1 = float(hold)
				self.dec = 0
			else:
				self.hold1 = int(hold)
		if clicked == self.ui.minus:
			self.minus = 1
			self.action = 1
			hold = self.ui.label.text()
			if '.' in hold:
				self.dec = 1
			if self.dec == 1:								# control for dec
				self.hold1 = float(hold)
				self.dec = 0
			else:
				self.hold1 = int(hold)
		if clicked == self.ui.mul:
			self.mul = 1
			self.action = 1
			hold = self.ui.label.text()
			if '.' in hold:
				self.dec = 1
			if self.dec == 1:								# control for dec
				self.hold1 = float(hold)
				self.dec = 0
			else:
				self.hold1 = int(hold)
		if clicked == self.ui.div:
			self.div = 1
			self.action = 1
			hold = self.ui.label.text()
			if '.' in hold:
				self.dec = 1
			if self.dec == 1:								# control for dec
				self.hold1 = float(hold)
				self.dec = 0
			else:
				self.hold1 = int(hold)
		if clicked == self.ui.equals:
			self.action = 1
			hold = self.ui.label.text()
			if '.' in hold:
				self.dec = 1
			if self.plus == 1:
				self.plus = 0
				if self.dec == 1:							# control for dec
					self.hold2 = float(hold)
					self.dec = 0
				else:
					self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 + self.hold2))
			if self.minus == 1:
				self.minus = 0
				if self.dec == 1:							# control for dec
					self.hold2 = float(hold)
					self.dec = 0
				else:
					self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 - self.hold2))
			if self.mul == 1:
				self.mul = 0
				if self.dec == 1:							# control for dec
					self.hold2 = float(hold)
					self.dec = 0
				else:
					self.hold2 = int(hold)
				self.ui.label.setText(str(self.hold1 * self.hold2))
			if self.div == 1:
				self.div = 0
				if self.dec == 1:							# control for dec
					self.hold2 = float(hold)
					self.dec = 0
				else:
					self.hold2 = int(hold)
				if self.hold2 == 0:
					self.ui.label.setText("Div By 0 Error")		# test for div by 0
				else:
					self.ui.label.setText(str(self.hold1 / self.hold2))
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
			if self.dec == 1:								# control for dec
				self.hold1 = float(hold)
				self.dec = 0
			else:
				self.hold1 = int(hold)
			self.ui.label.setText(str(self.hold1 * -1))
		if clicked == self.ui.dec:
			if self.dec == 0:
				self.dec = 1
				self.ui.label.setText(self.ui.label.text() + clicked.text())