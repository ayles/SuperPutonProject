# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projects\HSE\SuperPutonProject\ui_src\relevant.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 386)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(10000000, 10000000))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.dl_progress_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.dl_progress_label.setFont(font)
        self.dl_progress_label.setObjectName("dl_progress_label")
        self.verticalLayout.addWidget(self.dl_progress_label)
        self.extract_pb_label = QtWidgets.QLabel(self.centralwidget)
        self.extract_pb_label.setText("Распаковка файлов:")
        self.extract_pb_label.setObjectName("extract_pb_label")
        self.verticalLayout.addWidget(self.extract_pb_label)
        self.extract_pb = QtWidgets.QProgressBar(self.centralwidget)
        self.extract_pb.setProperty("value", 24)
        self.extract_pb.setObjectName("extract_pb")
        self.verticalLayout.addWidget(self.extract_pb)
        self.parsing_pb_label = QtWidgets.QLabel(self.centralwidget)
        self.parsing_pb_label.setObjectName("parsing_pb_label")
        self.verticalLayout.addWidget(self.parsing_pb_label)
        self.parseProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.parseProgressBar.setProperty("value", 24)
        self.parseProgressBar.setObjectName("parseProgressBar")
        self.verticalLayout.addWidget(self.parseProgressBar)
        self.year_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.year_label.setFont(font)
        self.year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.verticalLayout.addWidget(self.year_label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.beginDownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.beginDownloadButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beginDownloadButton.sizePolicy().hasHeightForWidth())
        self.beginDownloadButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.beginDownloadButton.setFont(font)
        self.beginDownloadButton.setCheckable(False)
        self.beginDownloadButton.setFlat(False)
        self.beginDownloadButton.setObjectName("beginDownloadButton")
        self.verticalLayout.addWidget(self.beginDownloadButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CBParser"))
        self.title_label.setText(_translate("MainWindow", "Скачивание актуальных данных"))
        self.status_label.setText(_translate("MainWindow", "Подождите..."))
        self.dl_progress_label.setText(_translate("MainWindow", "Загружено: "))
        self.parsing_pb_label.setText(_translate("MainWindow", "Обработка данных:"))
        self.parseProgressBar.setFormat(_translate("MainWindow", "%p% (добавлено %v из %m)"))
        self.year_label.setText(_translate("MainWindow", "Актуальные данные: 2019 год"))
        self.beginDownloadButton.setText(_translate("MainWindow", "Начать загрузку"))
        self.menu.setTitle(_translate("MainWindow", "Выход"))
        self.menu_2.setTitle(_translate("MainWindow", "О программе"))

