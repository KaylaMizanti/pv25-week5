import sys, re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton,
    QFormLayout, QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setGeometry(200, 100, 400, 500)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.age_input = QLineEdit()
        self.age_input.setValidator(QIntValidator(1, 150))
        self.phone_input = QLineEdit()
        self.phone_input.setText("+62 ")
        self.address_input = QTextEdit()

        self.gender_input = QComboBox()
        self.gender_input.addItems(["", "Laki-laki", "Perempuan"])

        self.education_input = QComboBox()
        self.education_input.addItems(["", "SMA", "D3", "S1", "S2", "S3"])

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Age:", self.age_input)
        form_layout.addRow("Phone Number:", self.phone_input)
        form_layout.addRow("Address:", self.address_input)
        form_layout.addRow("Gender:", self.gender_input)
        form_layout.addRow("Education:", self.education_input)

        pink_style = """
        QPushButton {
            background-color: #d63384;
            color: white;
            border-radius: 6px;
            padding: 6px 12px;
        }
        QPushButton:hover {
            background-color: #e83e8c;
        }
        """
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet(pink_style)
        self.save_button.clicked.connect(self.validate)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet(pink_style)
        self.clear_button.clicked.connect(self.clear)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        self.identity_label = QLabel("Kayla Mizanti | NIM: F1D022127")
        self.identity_label.setAlignment(Qt.AlignCenter)
        self.identity_label.setStyleSheet("color: gray; font-weight: bold; margin-top: 10px;")

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.identity_label)

        self.setLayout(main_layout)

    def validate(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        if not name:
            self.show_msg("Name cannot be empty")
            return
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) or not email.endswith(".com"):
            self.show_msg("Email is invalid or must end with .com")
            return
        if not age.isdigit() or int(age) < 17:
            self.show_msg("Age must be at least 17")
            return
        if not phone.strip() or not re.match(r'^\+62\s?\d{5,}$', phone):
            self.show_msg("Phone number must start with +62 and contain at least 5 digits after.")
            return
        if not address:
            self.show_msg("Address cannot be empty")
            return
        if not gender:
            self.show_msg("Gender must be selected")
            return
        if not education:
            self.show_msg("Education must be selected")
            return

        QMessageBox.information(self, "Success", "Data saved successfully!")
        self.clear()

    def clear(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.setText("+62 ")
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

    def show_msg(self, text):
        QMessageBox.warning(self, "Validation Failed", text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormValidation()
    window.show()
    sys.exit(app.exec_())
