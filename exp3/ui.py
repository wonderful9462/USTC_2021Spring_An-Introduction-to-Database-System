# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 1071, 821))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 501))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background:rgb(244, 255, 208)")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_9 = QtWidgets.QWidget(self.tab_3)
        self.widget_9.setGeometry(QtCore.QRect(10, 0, 981, 791))
        self.widget_9.setStyleSheet("background:rgb(244, 255, 208)")
        self.widget_9.setObjectName("widget_9")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setGeometry(QtCore.QRect(10, 220, 951, 571))
        self.widget_10.setObjectName("widget_10")
        self.treeWidget_1 = QtWidgets.QTreeWidget(self.widget_10)
        self.treeWidget_1.setGeometry(QtCore.QRect(10, 10, 821, 351))
        self.treeWidget_1.setMinimumSize(QtCore.QSize(0, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.setFont(font)
        self.treeWidget_1.setStyleSheet("border: 2px solid rgb(255, 212, 39);border-radius:12px;")
        self.treeWidget_1.setObjectName("treeWidget_1")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(6, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(7, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_1.headerItem().setFont(8, font)
        self.treeWidget_1.header().setMinimumSectionSize(32)
        self.label_22 = QtWidgets.QLabel(self.widget_9)
        self.label_22.setGeometry(QtCore.QRect(540, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_3.setGeometry(QtCore.QRect(680, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.widget_9)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_1.setGeometry(QtCore.QRect(120, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_15 = QtWidgets.QLabel(self.widget_9)
        self.label_15.setGeometry(QtCore.QRect(30, 60, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        self.label_16.setGeometry(QtCore.QRect(20, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_17 = QtWidgets.QLabel(self.widget_9)
        self.label_17.setGeometry(QtCore.QRect(320, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_8.setGeometry(QtCore.QRect(430, 120, 411, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_18 = QtWidgets.QLabel(self.widget_9)
        self.label_18.setGeometry(QtCore.QRect(290, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_19 = QtWidgets.QLabel(self.widget_9)
        self.label_19.setGeometry(QtCore.QRect(10, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.widget_9)
        self.label_20.setGeometry(QtCore.QRect(270, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_21 = QtWidgets.QLabel(self.widget_9)
        self.label_21.setGeometry(QtCore.QRect(590, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_6.setGeometry(QtCore.QRect(710, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_1.setGeometry(QtCore.QRect(370, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 255, 0)\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 160, 81, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 255, 0)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 255, 0)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 255, 0)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 160, 81, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background-color: red; \n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_13 = QtWidgets.QWidget(self.tab_4)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 1041, 801))
        self.widget_13.setObjectName("widget_13")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setGeometry(QtCore.QRect(20, 260, 901, 691))
        self.widget_14.setObjectName("widget_14")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.widget_14)
        self.treeWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 321))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "OK")
        self.widget_16 = QtWidgets.QWidget(self.widget_13)
        self.widget_16.setGeometry(QtCore.QRect(10, 10, 331, 71))
        self.widget_16.setObjectName("widget_16")
        self.label_14 = QtWidgets.QLabel(self.widget_16)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 170, 261, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton\n"
"{\n"
"background-color: gray; \n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_8.setGeometry(QtCore.QRect(560, 100, 121, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(93, 255, 244)\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_9.setGeometry(QtCore.QRect(690, 100, 131, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(93, 255, 244)\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 30, 121, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(93, 255, 244)\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_13)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"background-color:red\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_35 = QtWidgets.QLabel(self.widget_13)
        self.label_35.setGeometry(QtCore.QRect(310, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_11.setGeometry(QtCore.QRect(410, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_36 = QtWidgets.QLabel(self.widget_13)
        self.label_36.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_12.setGeometry(QtCore.QRect(140, 80, 261, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_23 = QtWidgets.QLabel(self.widget_13)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget_13)
        self.dateEdit_2.setGeometry(QtCore.QRect(180, 130, 131, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_24 = QtWidgets.QLabel(self.widget_13)
        self.label_24.setGeometry(QtCore.QRect(20, 170, 51, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_34 = QtWidgets.QLabel(self.widget_13)
        self.label_34.setGeometry(QtCore.QRect(320, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_13)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_31 = QtWidgets.QLabel(self.widget_13)
        self.label_31.setGeometry(QtCore.QRect(320, 160, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_14.setGeometry(QtCore.QRect(400, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_33 = QtWidgets.QLabel(self.widget_13)
        self.label_33.setGeometry(QtCore.QRect(320, 210, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_16.setGeometry(QtCore.QRect(400, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.comboBox_1 = QtWidgets.QComboBox(self.widget_13)
        self.comboBox_1.setGeometry(QtCore.QRect(120, 130, 51, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.label_32 = QtWidgets.QLabel(self.widget_13)
        self.label_32.setGeometry(QtCore.QRect(10, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_15.setGeometry(QtCore.QRect(110, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget_17 = QtWidgets.QWidget(self.tab_5)
        self.widget_17.setGeometry(QtCore.QRect(10, 0, 1031, 761))
        self.widget_17.setObjectName("widget_17")
        self.widget_18 = QtWidgets.QWidget(self.widget_17)
        self.widget_18.setGeometry(QtCore.QRect(410, 20, 591, 731))
        self.widget_18.setObjectName("widget_18")
        self.widget_19 = QtWidgets.QWidget(self.widget_17)
        self.widget_19.setGeometry(QtCore.QRect(-20, 10, 1041, 731))
        self.widget_19.setObjectName("widget_19")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_18.setGeometry(QtCore.QRect(470, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_25 = QtWidgets.QLabel(self.widget_19)
        self.label_25.setGeometry(QtCore.QRect(330, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(self.widget_19)
        self.label_27.setGeometry(QtCore.QRect(30, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_15.setGeometry(QtCore.QRect(340, 120, 281, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"background-color: gray; \n"
"}\n"
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_28 = QtWidgets.QLabel(self.widget_19)
        self.label_28.setGeometry(QtCore.QRect(30, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_19.setGeometry(QtCore.QRect(130, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_19)
        self.comboBox_3.setGeometry(QtCore.QRect(400, 20, 51, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_20.setGeometry(QtCore.QRect(470, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 90, 111, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(255, 222, 90)\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_29 = QtWidgets.QLabel(self.widget_19)
        self.label_29.setGeometry(QtCore.QRect(330, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_21.setGeometry(QtCore.QRect(140, 130, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_30 = QtWidgets.QLabel(self.widget_19)
        self.label_30.setGeometry(QtCore.QRect(20, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.widget_19)
        self.treeWidget_3.setGeometry(QtCore.QRect(20, 180, 861, 401))
        self.treeWidget_3.setObjectName("treeWidget_3")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_3.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_3.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_3.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_3.headerItem().setFont(3, font)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 10, 111, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(0, 170, 255)\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_12.setGeometry(QtCore.QRect(760, 10, 121, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton\n"
"{\n"
"background-color:red\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_14.setGeometry(QtCore.QRect(760, 90, 121, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(0, 170, 255)\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.widget_20 = QtWidgets.QWidget(self.widget_17)
        self.widget_20.setGeometry(QtCore.QRect(10, 380, 331, 71))
        self.widget_20.setObjectName("widget_20")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.widget_21 = QtWidgets.QWidget(self.tab_6)
        self.widget_21.setGeometry(QtCore.QRect(10, 10, 861, 581))
        self.widget_21.setObjectName("widget_21")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_17.setGeometry(QtCore.QRect(310, 130, 151, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton\n"
"{\n"
"background-color: yellow; \n"
"}\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.widget_21)
        self.dateEdit_1.setGeometry(QtCore.QRect(310, 50, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.dateEdit_1.setFont(font)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_16.setGeometry(QtCore.QRect(90, 130, 161, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton\n"
"{\n"
"background-color: purple; \n"
"}\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.widget_21)
        self.dateEdit_3.setGeometry(QtCore.QRect(560, 50, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 12, 31), QtCore.QTime(0, 0, 0)))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label = QtWidgets.QLabel(self.widget_21)
        self.label.setGeometry(QtCore.QRect(490, 50, 31, 61))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.treeWidget_4 = QtWidgets.QTreeWidget(self.widget_21)
        self.treeWidget_4.setGeometry(QtCore.QRect(20, 230, 831, 331))
        self.treeWidget_4.setObjectName("treeWidget_4")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_4.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_4.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget_4.headerItem().setFont(2, font)
        self.label_3 = QtWidgets.QLabel(self.widget_21)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_21)
        self.pushButton_18.setGeometry(QtCore.QRect(530, 130, 151, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_1.headerItem().setText(0, _translate("MainWindow", "身份证号"))
        self.treeWidget_1.headerItem().setText(1, _translate("MainWindow", "管理人身份证"))
        self.treeWidget_1.headerItem().setText(2, _translate("MainWindow", "姓名"))
        self.treeWidget_1.headerItem().setText(3, _translate("MainWindow", "联系电话"))
        self.treeWidget_1.headerItem().setText(4, _translate("MainWindow", "家庭住址"))
        self.treeWidget_1.headerItem().setText(5, _translate("MainWindow", "联系人姓名"))
        self.treeWidget_1.headerItem().setText(6, _translate("MainWindow", "联系人手机号"))
        self.treeWidget_1.headerItem().setText(7, _translate("MainWindow", "联系人Email"))
        self.treeWidget_1.headerItem().setText(8, _translate("MainWindow", "联系人关系"))
        self.label_22.setText(_translate("MainWindow", "负责人身份证："))
        self.label_13.setText(_translate("MainWindow", "身份证号："))
        self.label_15.setText(_translate("MainWindow", "姓名："))
        self.label_16.setText(_translate("MainWindow", "客户电话："))
        self.label_17.setText(_translate("MainWindow", "家庭住址："))
        self.label_18.setText(_translate("MainWindow", "联系人姓名："))
        self.label_19.setText(_translate("MainWindow", "联系人电话："))
        self.label_20.setText(_translate("MainWindow", "联系人Email："))
        self.label_21.setText(_translate("MainWindow", "联系人关系："))
        self.pushButton_1.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_3.setText(_translate("MainWindow", "更新"))
        self.pushButton_4.setText(_translate("MainWindow", "查询"))
        self.pushButton_5.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "客户管理"))
        self.label_14.setText(_translate("MainWindow", "账户号："))
        self.pushButton_10.setText(_translate("MainWindow", "清空"))
        self.pushButton_8.setText(_translate("MainWindow", "修改"))
        self.pushButton_9.setText(_translate("MainWindow", "查询"))
        self.pushButton_6.setText(_translate("MainWindow", "开户"))
        self.pushButton_7.setText(_translate("MainWindow", "销户"))
        self.label_35.setText(_translate("MainWindow", "开户支行："))
        self.label_36.setText(_translate("MainWindow", "开户身份证："))
        self.label_23.setText(_translate("MainWindow", "开户日期："))
        self.label_24.setText(_translate("MainWindow", "余额："))
        self.label_34.setText(_translate("MainWindow", "账户类型："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "储蓄"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "贷款"))
        self.label_31.setText(_translate("MainWindow", "利率："))
        self.label_33.setText(_translate("MainWindow", "透支额："))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "="))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "!="))
        self.comboBox_1.setItemText(2, _translate("MainWindow", ">"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "<"))
        self.label_32.setText(_translate("MainWindow", "货币类型："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "账户管理"))
        self.label_25.setText(_translate("MainWindow", "金额："))
        self.label_27.setText(_translate("MainWindow", "贷款号："))
        self.pushButton_15.setText(_translate("MainWindow", "清空"))
        self.label_28.setText(_translate("MainWindow", "支行："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "="))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "!="))
        self.comboBox_3.setItemText(2, _translate("MainWindow", ">"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "<"))
        self.pushButton_13.setText(_translate("MainWindow", "发放"))
        self.label_29.setText(_translate("MainWindow", "发放金额："))
        self.label_30.setText(_translate("MainWindow", "身份证号："))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "贷款号"))
        self.treeWidget_3.headerItem().setText(1, _translate("MainWindow", "金额"))
        self.treeWidget_3.headerItem().setText(2, _translate("MainWindow", "支行"))
        self.treeWidget_3.headerItem().setText(3, _translate("MainWindow", "发放状态"))
        self.pushButton_11.setText(_translate("MainWindow", "添加"))
        self.pushButton_12.setText(_translate("MainWindow", "删除"))
        self.pushButton_14.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "贷款管理"))
        self.pushButton_17.setText(_translate("MainWindow", "储蓄统计"))
        self.pushButton_16.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "~"))
        self.treeWidget_4.headerItem().setText(0, _translate("MainWindow", "支行名"))
        self.treeWidget_4.headerItem().setText(1, _translate("MainWindow", "客户数"))
        self.treeWidget_4.headerItem().setText(2, _translate("MainWindow", "总金额"))
        self.label_3.setText(_translate("MainWindow", "请选择日期区间："))
        self.pushButton_18.setText(_translate("MainWindow", "贷款统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "统计查询"))
