import sys
from PyQt5.QtGui import QIcon  # pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    icon = QIcon("imgs/favicon.ico")
    app.setWindowIcon(icon)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
