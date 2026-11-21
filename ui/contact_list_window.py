"""The module defines the ContactListWindow class."""

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from ui.base.main_window import MainWindow


PHONE_DIGIT_COUNT = 10

class ContactListWindow(MainWindow):
    """Represents the main window of the contact list application"""
    
    def __init__(self) -> None:
        """Initializes a new instance of the ContactListWindow class."""

        super().__init__()

        self.setWindowTitle("Contact Manager")

        self.__set_initial_widget_state()
        self.__connect_signals()

    def __set_initial_widget_state(self) -> None:
        """Sets the widgets to their initial state."""

        self._name_line_edit.setPlaceholderText("Contact Name")
        self._phone_line_edit.setInputMask("(000) 000-0000;_")

        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)

    def __connect_signals(self) -> None:
        """Connects the widget signals to their slots."""
        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)
        self._add_button.clicked.connect(self.__on_add_clicked)
        self._remove_button.clicked.connect(self.__on_remove_clicked)
        self._contact_table.itemSelectionChanged.connect(
            self.__on_selection_changed)
        
         
    @Slot()
 
    def __on_input_changed(self) -> None:
        """Enables the add button when the name and phone inputs are valid.

        The name must not be empty and the phone number must have all
        10 digits entered.
        """

        name = self._name_line_edit.text().strip()
        phone = self._phone_line_edit.text()
        digit_count = sum(character.isdigit() for character in phone)

        self._add_button.setEnabled(
            name != "" and digit_count == PHONE_DIGIT_COUNT)