# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projects\HSE\SuperPutonProject\ui_src\main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 541)
        MainWindow.setWindowTitle("CBParser")
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setWhatsThis("")
        self.label.setAccessibleName("")
        self.label.setAccessibleDescription("")
        self.label.setText("CBParser")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.dl_archives_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.dl_archives_button.setFont(font)
        self.dl_archives_button.setToolTip("")
        self.dl_archives_button.setStatusTip("")
        self.dl_archives_button.setWhatsThis("")
        self.dl_archives_button.setAccessibleName("")
        self.dl_archives_button.setAccessibleDescription("")
        self.dl_archives_button.setText("Скачать архивные данные")
        self.dl_archives_button.setObjectName("dl_archives_button")
        self.verticalLayout.addWidget(self.dl_archives_button)
        self.dl_relevant_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.dl_relevant_button.setFont(font)
        self.dl_relevant_button.setToolTip("")
        self.dl_relevant_button.setStatusTip("")
        self.dl_relevant_button.setWhatsThis("")
        self.dl_relevant_button.setAccessibleName("")
        self.dl_relevant_button.setAccessibleDescription("")
        self.dl_relevant_button.setText("Скачать актуальные данные")
        self.dl_relevant_button.setObjectName("dl_relevant_button")
        self.verticalLayout.addWidget(self.dl_relevant_button)
        self.start_viewer_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.start_viewer_button.setFont(font)
        self.start_viewer_button.setToolTip("")
        self.start_viewer_button.setStatusTip("")
        self.start_viewer_button.setWhatsThis("")
        self.start_viewer_button.setAccessibleName("")
        self.start_viewer_button.setAccessibleDescription("")
        self.start_viewer_button.setText("Просмотр загруженных данных")
        self.start_viewer_button.setObjectName("start_viewer_button")
        self.verticalLayout.addWidget(self.start_viewer_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setToolTip("")
        self.pushButton.setStatusTip("")
        self.pushButton.setWhatsThis("")
        self.pushButton.setAccessibleName("")
        self.pushButton.setAccessibleDescription("")
        self.pushButton.setText("Выход")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


