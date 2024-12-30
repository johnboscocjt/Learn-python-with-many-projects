# PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        
        # simple way is adding the picture to the label and then use the label to display it
        # self refer tothe window  object, which is parent widget
        label = QLabel(self)
        label.setGeometry(0,0,500,500)

        pixmap = QPixmap("picture/icon.jpeg")
        label.setPixmap(pixmap)
        
        # scale the image to the size of the label
        label.setScaledContents(True)
        
        # label.setGeometry(0,0,label.width(),label.height())

        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()