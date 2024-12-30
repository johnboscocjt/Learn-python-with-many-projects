# PyQt5 Layouts
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel 
                             


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        # putting the button to the constructor
        self.button = QPushButton("Click me!", self)
        
        # a label
        self.label = QLabel("Hello",self)
        
        # anything to deal with the UI has to deal with the below function
        self.initUI()
        
    def initUI(self):
        # self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        
        # signal and the slot for the onclick
        self.button.clicked.connect(self.on_click)
        
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 30px;")
        
    # connecting the button to the function
    def on_click(self):
        # print("Button Clicked!")
        # # self to belong to the main window
        # self.button.setText("Clicked")
        # self.button.setDisabled(True)
        self.label.setText("Goodbye")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()