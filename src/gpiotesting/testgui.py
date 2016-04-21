from PySide.QtCore import *
from PySide.QtGui import *
import sys 
from gpiopi_nomult import * 

def action():
    sunRoofOpen()
    QMessageBox.information(win, "Goodbye", "Go to Hellokittyland")
 
def action2():   
    QMessageBox.warning(win, "I'm warning you!", "Go away already") 

app = QApplication(sys.argv)
win = QDialog()
button1 = QPushButton("Hello")
button2 = QPushButton("Hell")
layout = QVBoxLayout()
layout.addWidget(button1)
layout.addWidget(button2)
win.setLayout(layout)
button1.clicked.connect(action)
button2.clicked.connect(action2)
win.show()
app.exec_() 
