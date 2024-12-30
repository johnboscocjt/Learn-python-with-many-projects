import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    # its constructor, where we will be constructing different entities for the clock
    def __init__(self):
        # if any arguements to send to the parent class
        super().__init__()
        
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        
        self.initUI()
        
        
    def initUI(self):
        # the layout of the digital clock will be designed in this function/method
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        
        # layout manager
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size: 150px;"
            # "font-family: Arial;"
            "color: hsl(111,100%,50%);"
            )
        self.setStyleSheet("background-color: black;")
        
        font_id = QFontDatabase.addApplicationFont("digitalclockwidget/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        
        self.timer.timeout.connect(self.update_time)
        # trigger timer
        self.timer.start(1000)
        
        # time
        self.update_time()
            
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    # a window that stays in-place until we exit
    sys.exit(app.exec_())
