import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("测试窗口")
window.resize(400, 300)
label = QLabel("fuck Qt!", window)
label.setStyleSheet("font-size: 24px; color: red;")
label.move(100, 100)
window.show()
print("Window should be visible now")
sys.exit(app.exec())