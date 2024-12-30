# PyQt5 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        # constructor of the super class
        super().__init__()
        self.setWindowTitle("My jbUI GUI")
        # geometry of where the window appears and the size(x,y,width,height)
        self.setGeometry(700,300,500,500)
        # the window icon, import the relevant library
        self.setWindowIcon(QIcon("gui/icon.jpeg"))
        
         
  
  
        
def main():
    # you can pass an empty list
    app = QApplication(sys.argv)
    
    window = MainWindow()
    # show the window
    window.show()
    # window exist till we interact with it
    sys.exit(app.exec_())

# if we are running this file directly, call the main function
if __name__ == "__main__":
    main()
