
from logic import *

def main():
    """
    Main function for executing the setup for the logic and laying the groundwork for the gui
    :return:
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
