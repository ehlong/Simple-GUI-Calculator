from PyQt5.QtWidgets import QApplication
from calcwindow import CalcWindow


app = QApplication([])
window = CalcWindow()
window.show()
app.exec_()
