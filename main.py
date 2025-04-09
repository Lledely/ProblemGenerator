import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit,
    QSpinBox, QCheckBox, QPushButton, QMessageBox
)
import logic_wrapper
import constants

class ProblemGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Problem Generator")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.problem_label = QLabel("Problem File Name:")
        self.problem_input = QLineEdit()
        self.problem_input.setText(constants.default_latex_problems_file_name)
        layout.addWidget(self.problem_label)
        layout.addWidget(self.problem_input)

        self.solution_label = QLabel("Solution File Name:")
        self.solution_input = QLineEdit()
        self.solution_input.setText(constants.default_latex_solutions_file_name)
        layout.addWidget(self.solution_label)
        layout.addWidget(self.solution_input)

        self.variants_label = QLabel("Number of Variants:")
        self.variants_input = QSpinBox()
        self.variants_input.setRange(1, 100)
        self.variants_input.setValue(constants.default_number_of_variants)
        layout.addWidget(self.variants_label)
        layout.addWidget(self.variants_input)

        self.dual_checkbox = QCheckBox("Dual Problems")
        layout.addWidget(self.dual_checkbox)

        self.generate_button = QPushButton("Generate")
        layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.generate_problems)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def generate_problems(self):
        number_of_variants = self.variants_input.value()
        do_dual = self.dual_checkbox.isChecked()
        problem_file_name = self.problem_input.text() or constants.default_latex_problems_file_name
        solution_file_name = self.solution_input.text() or constants.default_latex_solutions_file_name
        logic_wrapper.generate(
            number_of_variants, 
            do_dual, 
            problem_file_name, 
            solution_file_name
        )
        QMessageBox.information(
            self, 
            "Success", 
            "Files were created successfully!"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProblemGeneratorGUI()
    window.show()
    sys.exit(app.exec_())
