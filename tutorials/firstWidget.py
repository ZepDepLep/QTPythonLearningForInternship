import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("<font color=red size=50>Hello world</font>")
label.show()
app.exec()