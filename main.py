from gui import ProblemGeneratorGUI
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProblemGeneratorGUI()
    window.show()
    sys.exit(app.exec_())
