    def create_chat_history(self):
        chat_history = QTextEdit()
        chat_history.setReadOnly(True)
        chat_history.ensureCursorVisible()
        chat_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        chat_history.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        chat_history.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.8);color: white; font-family: 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
    def send_message(self, user_message):
        user_message = self.user_input.toPlainText()
        self.user_input.clear()
        if user_message is not None:
            if user_message.startswith("!"):
                self.run_command(user_message)
            elif user_message.strip():
                self.chat_history.setPlainText(
                    self.chat_history.toPlainText() + "You: " + user_message + "\n\n"
                )
                self.chat_history.moveCursor(QTextCursor.End)
                response = chat_gpt(user_message)
                self.chat_history.setPlainText(
                    self.chat_history.toPlainText() + "Assistant: " + response + "\n\n"
                )
                self.chat_history.moveCursor(QTextCursor.End)
                return response
        else:
