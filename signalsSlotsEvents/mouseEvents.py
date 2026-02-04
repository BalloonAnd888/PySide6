import sys 

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
    
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # Handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton:
            # Handle the middle-button press in here
            self.label.setText("mousePressEvent MIDDLE")
        
        elif e.button() == Qt.MouseButton.RightButton:
            # Handle the right-button press in here
            self.label.setText("mousePressEvent RIGHT")
    
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # Handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton:
            # Handle the middle-button press in here
            self.label.setText("mousePressEvent MIDDLE")
        
        elif e.button() == Qt.MouseButton.RightButton:
            # Handle the right-button press in here
            self.label.setText("mousePressEvent RIGHT")
    
    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # Handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton:
            # Handle the middle-button press in here
            self.label.setText("mousePressEvent MIDDLE")
        
        elif e.button() == Qt.MouseButton.RightButton:
            # Handle the right-button press in here
            self.label.setText("mousePressEvent RIGHT")

app = QApplication(sys.argv) 

window = MainWindow()
window.show() 

app.exec()
