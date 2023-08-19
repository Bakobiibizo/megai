
    # Clear the Chat History
    def clear_chat_history(self):
        self.chat_history.clear()
        return self.chat_history

    # Open a file dialog for embedding a file
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
            return "error embedding file"

    # Pull uncompressed documents from database
    def use_base_retriever(self, text):
        results = base_retriever(text)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Base search results: \n" + str(results) + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText() + str("Base search failed" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return "error retrieving documents"

    # Embed an entire directory
    def mass_embed(self, text):
        results = create_mass_embedding(folder_path=text)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str(
                    "Embedding created, use !docslong and !docs to pull relevant documents, and !searchmem to query the database"
                    + str(results)
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
            return "error embedding file"

    # Query the database
    def search_memory(self, text):
        results = data_base_memory_search(user_query=text)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Memory search results: \n" + str(results))
                + "\n\n"
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText() + str("No results found" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return "No results found"

    # Add a file to the database
    def add_to_db(self, text):
        results = scrape_site(url=text)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Added to database: \n" + str(results) + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Failed to add to database" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return "Failed to add to database"

    def add_map_db(self, text, collection_name):
        url = text
        results = scrape_site_map(url, collection_name)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Added to database: \n" + str(results) + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Failed to add to database" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return "Failed to add to database"

    # Add a project to the database
    def add_project_to_db(self, text):
        results = run_embed_project(file_path=text)
        if results:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Added to database: \n" + str(results) + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return results
        else:
            self.chat_history.setPlainText(
                self.chat_history.toPlainText()
                + str("Failed to add to database" + "\n\n")
            )
            self.chat_history.moveCursor(QTextCursor.End)
            return "Failed to add to database"

    # Run the ! commands
    def run_command(self, text):
        if text == "!help":
            self.display_help()
            return
        if text == "!exit":
            self.exit_program()
            return
        if text == "!clear":
            self.clear_chat_history()
            return
        if text == "!save":
            self.save_chat_history()
            return
        if text == "!load":
            self.load_chat_history()
            return
        if text == "!embed":
            results = self.open_file_dialog()
            if results:
                return results
            else:
                return "Error creating embedding"
        if text.startswith("!massembed"):
            text = text.removeprefix("!massembed ")
            results = self.mass_embed(text)
            if results:
                return results
            else:
                return "Error creating embedding"
        if text.startswith("!searchmem"):
            text = text.removeprefix("!searchmem ")
            results = self.search_memory(text)
            if results:
                return results
            else:
                return "No results found"
        if text.startswith("!docs"):
            text = text.removeprefix("!docs ")
            results = self.use_base_retriever(text)
            if results:
                return results
            else:
                return "No results found"
        if text.startswith("!addmem"):
            text = text.removeprefix("!addmem ")
            results = self.add_to_db(text)
            if results:
                return results
            else:
                return "Error adding to database"
        if text.startswith("!addmap"):
            text = text.removeprefix("!addmap ")
            split_text = text.split(" ")
            text = split_text[0]
            collection_name = split_text[1]
            results = self.add_map_db(text, collection_name)
            if results:
                return results
            else:
                return "Error creating loading"
        if text.startswith("!addproject"):
            text = text.removeprefix("!addproject ")
            results = self.add_project_to_db(text)
            if results:
                return results
            else:
                return "Error creating loading"
        if text.startswith("!background"):
            text = text.removeprefix("!background ")
            image = QPixmap("img/0000" + str(text) + ".png")
            results = MainWindow.change_background_image(image)
            if results:
                return results
            else:
                return "Error creating loading"
        else:
            if text.startswith("!"):
                self.chat_history.setPlainText(
                    self.chat_history.toPlainText()
                    + str("Command not found. Type !help for a list of commands \n\n")
                )
                self.chat_history.moveCursor(QTextCursor.End)
                return

    # Help info

    def display_help(self):
        self.chat_history.setPlainText(
            self.chat_history.toPlainText()
            + str(
                """
    Commands:
!help       - Display this help message.
!save       - Save chat history.
!load       - Load chat history.
!clear      - Clear chat history.
!exit       - Exit the application.
!docs       - Search the database for related docs.
!searchmem  - Search the database for context on a
                prompt then ask for a more detailed
                response.
!addmem     - [http] Add a list of comma delineated
                website to the database.
!addmap     - [.xml] - Add all the sites froma sitemap
                it to the database.
!embed      - Upload a file to create embeddings.
!massembed  - [dir] - Upload multiple files to create
                embeddings. Follow dir with a space
                then folder path.
!addproject - [dir] - Add python project files to the
                database. Follow with a space then
                folder path. Note this sends your
                project file information to the OpenAI
                API.
!background - Change the background image.
        """
            )
        )

    # Load file into chat

    def load_chat_history(self):
        file_dialog = QFileDialog(self)
        file_dialog.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.7); color: #f9f9f9; font-family: 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            with open(file_name, "r") as file:
                self.chat_history.setPlainText(
                    self.chat_history.toPlainText() + str(file.read()) + "\n\n"
                )

    # save chat history to file
    def save_chat_history(self):
        file_dialog = QFileDialog(self)
        file_dialog.setStyleSheet(
            "background-color: rgba(67, 3, 81, 0.7); color: #f9f9f9; font-family: 'Cascadia Code'; font-size: 14pt; font-weight: bold;"
        )
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            with open(file_name, "a") as file:
                file.write(
                    str(
                        self.chat_history.setPlainText(
                            self.chat_history.toPlainText() + "\n\n"
                        )
                    )
                )

    # Exit
    def exit_program(self):
        """
        Exits the program with a successful status code.
        """
