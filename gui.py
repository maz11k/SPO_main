from main import Logic
from PyQt5 import QtWidgets, QtCore, QtGui

import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Анализ текста")
        MainWindow.resize(542, 681)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 530, 121, 51))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 91))
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 141, 51))
        self.label_3.setObjectName("label_3")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 80, 191, 241))
        self.listView.setObjectName("listView")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 60, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.clck)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ текста"))
        self.pushButton.setText(_translate("MainWindow", "Анализ текста"))
        self.label.setText(_translate("MainWindow", "Самые частовстречающиеся слова:"))
        self.label_3.setText(_translate("MainWindow", "Общее количество слов:"))
        self.label_4.setText('')

    def clck(self):
        lst = Logic().main()
        lsted = []
        c = 0
        for i in lst:
            if c == 0:
                c += 1
                continue
            else:
                ed = i.split()
                ed.remove(ed[-1])
                ed.remove('->')
                lsted.append(ed)
        self.label_4.setText(str(lst[0]))
        model = QtGui.QStandardItemModel()
        model.removeRows(0, model.rowCount())
        self.listView.setModel(model)
        for i in lst:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        x = [o[0] for o in reversed(lsted)]
        y = [o[-1] for o in reversed(lsted)]
        fig, ax = plt.subplots()
        ax.bar(x, y)
        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(8)
        fig.set_figheight(6)
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
