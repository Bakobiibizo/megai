    def create_user_input(self):
        user_input = CustomTextEdit()
        user_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        user_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        user_input.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.8);color: white; font-family: 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
        user_input.setFixedHeight(50)
        user_input.textChanged.connect(self.adjust_user_input_height)
