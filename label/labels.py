# PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
# class for alignment
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        # geometry of the font such as position, width and height
        label.setGeometry(0,0,500,100)
        # some css like properties
        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        # label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignBottom)

        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()