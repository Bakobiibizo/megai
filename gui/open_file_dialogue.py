    def open_large_text_input(self):
        self.large_text_input_dialog = LargeTextInputDialog(self)
    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.7); color: #f9f9f9; font-family: 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            results = create_embedding(file_name)
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str(
                    "Embedding created, use !docslong and !docs to pull relevant documents"
                    + "\n\n"
                )
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText() + str("Embedding failed" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
class LargeTextInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Large Text Input")
        self.resize(400, 600)
        self.text_input = QTextEdit()
        self.text_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_input.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.7); color: #f9f9f9; font-family 'Cascadia Code'; font-size: 12pt; font-weight: bold;"
        )
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(
            "background-color:rgba(67, 3, 81, 0.7); color: #f9f9f9; font-family 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_input)
        self.layout.addWidget(self.send_button)
