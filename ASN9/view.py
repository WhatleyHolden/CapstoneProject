from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        MainWindow.resize(520, 330)
        MainWindow.setMinimumSize(QSize(520, 330))
        MainWindow.setWindowTitle("Assignment 9 MVC Calculator")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lblTitle = QLabel(self.centralwidget)
        self.lblTitle.setObjectName("lblTitle")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.lblTitle.setFont(title_font)
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.lblTitle.setStyleSheet("background-color: #DCEEF2; padding: 10px;")
        self.verticalLayout.addWidget(self.lblTitle)

        self.grpCalculator = QGroupBox(self.centralwidget)
        self.grpCalculator.setObjectName("grpCalculator")
        self.gridLayout = QGridLayout(self.grpCalculator)
        self.gridLayout.setObjectName("gridLayout")

        self.lblFirstNumber = QLabel(self.grpCalculator)
        self.lblFirstNumber.setObjectName("lblFirstNumber")
        self.lblFirstNumber.setStyleSheet("background-color: blue; color: white; padding: 6px;")
        self.gridLayout.addWidget(self.lblFirstNumber, 0, 0, 1, 1)

        self.txtFirstNumber = QLineEdit(self.grpCalculator)
        self.txtFirstNumber.setObjectName("txtFirstNumber")
        self.txtFirstNumber.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.txtFirstNumber, 0, 1, 1, 1)

        self.lblSecondNumber = QLabel(self.grpCalculator)
        self.lblSecondNumber.setObjectName("lblSecondNumber")
        self.lblSecondNumber.setStyleSheet("background-color: blue; color: white; padding: 6px;")
        self.gridLayout.addWidget(self.lblSecondNumber, 1, 0, 1, 1)

        self.txtSecondNumber = QLineEdit(self.grpCalculator)
        self.txtSecondNumber.setObjectName("txtSecondNumber")
        self.txtSecondNumber.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.txtSecondNumber, 1, 1, 1, 1)

        self.lblResult = QLabel(self.grpCalculator)
        self.lblResult.setObjectName("lblResult")
        result_font = QFont()
        result_font.setPointSize(16)
        result_font.setBold(True)
        self.lblResult.setFont(result_font)
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setStyleSheet("background-color: #E8F5E9; padding: 12px;")
        self.gridLayout.addWidget(self.lblResult, 2, 0, 1, 2)

        self.verticalLayout.addWidget(self.grpCalculator)

        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName("fraButtons")
        self.fraButtons.setFrameShape(QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnAdd = QPushButton(self.fraButtons)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnSubtract = QPushButton(self.fraButtons)
        self.btnSubtract.setObjectName("btnSubtract")
        self.btnSubtract.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btnSubtract)

        self.btnClear = QPushButton(self.fraButtons)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btnClear)

        self.btnExit = QPushButton(self.fraButtons)
        self.btnExit.setObjectName("btnExit")
        self.btnExit.setMinimumWidth(90)
        self.horizontalLayout.addWidget(self.btnExit)

        self.verticalLayout.addWidget(self.fraButtons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Assignment 9 MVC Calculator", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", "Simple MVC Calculator", None))
        self.grpCalculator.setTitle(QCoreApplication.translate("MainWindow", "Add or Subtract Two Numbers", None))
        self.lblFirstNumber.setText(QCoreApplication.translate("MainWindow", "First Number:", None))
        self.txtFirstNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", "Example: 10", None))
        self.lblSecondNumber.setText(QCoreApplication.translate("MainWindow", "Second Number:", None))
        self.txtSecondNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", "Example: 5", None))
        self.lblResult.setText(QCoreApplication.translate("MainWindow", "Result will appear here", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", "Add", None))
        self.btnSubtract.setText(QCoreApplication.translate("MainWindow", "Subtract", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", "Clear", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
