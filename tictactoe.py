from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 320, 320))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.frame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 100, 320, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 320, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(100, 0, 10, 320))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(210, 0, 10, 320))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.index0 = QtWidgets.QPushButton(self.frame)
        self.index0.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.index0.setText("")
        self.index0.setObjectName("index0")
        self.index1 = QtWidgets.QPushButton(self.frame)
        self.index1.setGeometry(QtCore.QRect(110, 0, 100, 100))
        self.index1.setText("")
        self.index1.setObjectName("index1")
        self.index2 = QtWidgets.QPushButton(self.frame)
        self.index2.setGeometry(QtCore.QRect(220, 0, 100, 100))
        self.index2.setText("")
        self.index2.setObjectName("index2")
        self.index3 = QtWidgets.QPushButton(self.frame)
        self.index3.setGeometry(QtCore.QRect(0, 105, 100, 100))
        self.index3.setText("")
        self.index3.setObjectName("index3")
        self.index4 = QtWidgets.QPushButton(self.frame)
        self.index4.setGeometry(QtCore.QRect(110, 105, 100, 100))
        self.index4.setText("")
        self.index4.setObjectName("index4")
        self.index5 = QtWidgets.QPushButton(self.frame)
        self.index5.setGeometry(QtCore.QRect(220, 105, 100, 100))
        self.index5.setText("")
        self.index5.setObjectName("index5")
        self.index6 = QtWidgets.QPushButton(self.frame)
        self.index6.setGeometry(QtCore.QRect(0, 210, 100, 100))
        self.index6.setText("")
        self.index6.setObjectName("index6")
        self.index7 = QtWidgets.QPushButton(self.frame)
        self.index7.setGeometry(QtCore.QRect(110, 210, 100, 100))
        self.index7.setText("")
        self.index7.setObjectName("index7")
        self.index8 = QtWidgets.QPushButton(self.frame)
        self.index8.setGeometry(QtCore.QRect(220, 210, 100, 100))
        self.index8.setText("")
        self.index8.setObjectName("index8")
        self.PLAYER_TURN = QtWidgets.QLabel(self.centralwidget)
        self.PLAYER_TURN.setGeometry(QtCore.QRect(10, 430, 441, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.PLAYER_TURN.setFont(font)
        self.PLAYER_TURN.setObjectName("PLAYER_TURN")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(672, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.X_SCORE = QtWidgets.QLabel(self.centralwidget)
        self.X_SCORE.setGeometry(QtCore.QRect(560, 330, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.X_SCORE.setFont(font)
        self.X_SCORE.setObjectName("X_SCORE")
        self.Y_SCORE = QtWidgets.QLabel(self.centralwidget)
        self.Y_SCORE.setGeometry(QtCore.QRect(560, 410, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Y_SCORE.setFont(font)
        self.Y_SCORE.setObjectName("Y_SCORE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.X_SCORE_INT = 0
        self.O_SCORE_INT = 0
        self.PLAYER_TURN_TEXT = "Player\'s Turn --> "
        self.PLAYER_TURN_SYMB = "X"
        self.index0.clicked.connect(lambda: self.play(self.index0))
        self.index1.clicked.connect(lambda: self.play(self.index1))
        self.index2.clicked.connect(lambda: self.play(self.index2))
        self.index3.clicked.connect(lambda: self.play(self.index3))
        self.index4.clicked.connect(lambda: self.play(self.index4))
        self.index5.clicked.connect(lambda: self.play(self.index5))
        self.index6.clicked.connect(lambda: self.play(self.index6))
        self.index7.clicked.connect(lambda: self.play(self.index7))
        self.index8.clicked.connect(lambda: self.play(self.index8))
        self.resetButton.clicked.connect(self.RESET_BUTTON)
        self.BUTTONS = [self.index0, self.index1, self.index2, self.index3, self.index4, self.index5, self.index6, self.index7, self.index8]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PLAYER_TURN.setText(_translate("MainWindow", self.PLAYER_TURN_TEXT + self.PLAYER_TURN_SYMB))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.X_SCORE.setText(_translate("MainWindow", "X Score -->"))
        self.Y_SCORE.setText(_translate("MainWindow", "Y Score -->"))

    def switch(self):
        if self.PLAYER_TURN_SYMB == "X":
            self.PLAYER_TURN_SYMB = "O"
        else:
            self.PLAYER_TURN_SYMB = "X"

    def play(self, btn):
        if btn.text() == "":
            btn.setText(self.PLAYER_TURN_SYMB)
            self.switch()
        else:
            self.pop_msg("Invalid Move", f"Player {btn.text()} has already taken this move, Please choose another move")
        self.UPDATE_LABELS()
        self.ROUND_END()

    def UPDATE_LABELS(self):
        self.PLAYER_TURN.setText(self.PLAYER_TURN_TEXT + self.PLAYER_TURN_SYMB)
        self.X_SCORE.setText("X SCORE --> " + str(self.X_SCORE_INT))
        self.Y_SCORE.setText("O SCORE --> " + str(self.O_SCORE_INT))

    def RESET_BUTTON(self):
        self.index0.setText("")
        self.index1.setText("")
        self.index2.setText("")
        self.index3.setText("")
        self.index4.setText("")
        self.index5.setText("")
        self.index6.setText("")
        self.index7.setText("")
        self.index8.setText("")

    def pop_msg(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec()

        # 0 1 2 || 3 4 5 || 6 7 8
        # 0 3 6 || 1 4 7 || 2 5 8
        # 0 4 8 || 2 4 6

    def ROUND_END(self):
        if self.BUTTONS[0].text() == self.BUTTONS[1].text() == self.BUTTONS[2].text() != "":
            self.ROUND_UP(self.BUTTONS[0].text())
        elif self.BUTTONS[3].text() == self.BUTTONS[4].text() == self.BUTTONS[5].text() != "":
            self.ROUND_UP(self.BUTTONS[3].text())
        elif self.BUTTONS[6].text() == self.BUTTONS[7].text() == self.BUTTONS[8].text() != "":
            self.ROUND_UP(self.BUTTONS[6].text())
        elif self.BUTTONS[0].text() == self.BUTTONS[3].text() == self.BUTTONS[6].text() != "":
            self.ROUND_UP(self.BUTTONS[0].text())
        elif self.BUTTONS[1].text() == self.BUTTONS[4].text() == self.BUTTONS[7].text() != "":
            self.ROUND_UP(self.BUTTONS[1].text())
        elif self.BUTTONS[2].text() == self.BUTTONS[5].text() == self.BUTTONS[8].text() != "":
            self.ROUND_UP(self.BUTTONS[2].text())
        elif self.BUTTONS[0].text() == self.BUTTONS[4].text() == self.BUTTONS[8].text() != "":
            self.ROUND_UP(self.BUTTONS[0].text())
        elif self.BUTTONS[2].text() == self.BUTTONS[4].text() == self.BUTTONS[6].text() != "":
            self.ROUND_UP(self.BUTTONS[2].text())


    def ROUND_UP(self, Winner):
        self.pop_msg("Round ended", f"Player {Winner} has won")
        self.RESET_BUTTON()
        if Winner == "X":
            self.X_SCORE_INT += 1
        else:
            self.O_SCORE_INT += 1
        self.switch()
        self.UPDATE_LABELS()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.UPDATE_LABELS()
    MainWindow.show()
    sys.exit(app.exec_())
