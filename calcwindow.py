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

	def buttonPressed(self):
		clicked = self.sender()
		if (clicked == 'one' or 'two' or 'three' or 'four' or \
		'five' or 'six' or 'seven' or 'eight' or 'nine' or 'zero'):
			if self.ui.label.text() == "0":
				self.ui.label.setText('')
			self.ui.label.setText(self.ui.label.text() + clicked.text())
		# if clicked == 'plus':


