# PyQt5 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")    
        self.button3 = QPushButton("#3")           
        # anything to deal with the UI has to deal with the below function
        self.initUI()
        
    def initUI(self):
        # layout manager added to the central widget, then the central widget will be added to the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        
        central_widget.setLayout(hbox)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        # css
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }              
              
            QPushButton#button1{
                background-color: red;
            }      
            
            QPushButton#button2{
                background-color: green;
            }  
            
            QPushButton#button3{
                background-color: blue;
            } 
            
            QPushButton#button3:hover{
                background-color: red;
            }
            QPushButton#button2:hover{
                background-color: blue;
            } 
            QPushButton#button1:hover{
                background-color: green;
            }               
        """)
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()