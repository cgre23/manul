# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UImanul.ui'
#
# Created: Sun Mar 05 23:56:42 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1159, 1022)
        Form.setMinimumSize(QtCore.QSize(1000, 0))
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Form.setStyleSheet(_fromUtf8("background-color: white"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_write = QtGui.QPushButton(self.tab)
        self.pb_write.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_write.setFont(font)
        self.pb_write.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_write.setObjectName(_fromUtf8("pb_write"))
        self.horizontalLayout_2.addWidget(self.pb_write)
        self.pb_read = QtGui.QPushButton(self.tab)
        self.pb_read.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_read.setFont(font)
        self.pb_read.setStyleSheet(_fromUtf8("color: rgb(85, 255, 255);"))
        self.pb_read.setObjectName(_fromUtf8("pb_read"))
        self.horizontalLayout_2.addWidget(self.pb_read)
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pb_update = QtGui.QPushButton(self.frame)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_update.setFont(font)
        self.pb_update.setObjectName(_fromUtf8("pb_update"))
        self.gridLayout_2.addWidget(self.pb_update, 5, 0, 1, 1)
        self.pb_reset = QtGui.QPushButton(self.frame)
        self.pb_reset.setEnabled(True)
        self.pb_reset.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_reset.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_reset.setFont(font)
        self.pb_reset.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_reset.setObjectName(_fromUtf8("pb_reset"))
        self.gridLayout_2.addWidget(self.pb_reset, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.widget_2 = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(700, 600))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_12.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(400, 200))
        self.widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_12.addWidget(self.widget)
        self.gridLayout_9.addLayout(self.horizontalLayout_12, 0, 0, 1, 2)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_15 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.cb_coupler_kick = QtGui.QCheckBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_coupler_kick.setFont(font)
        self.cb_coupler_kick.setObjectName(_fromUtf8("cb_coupler_kick"))
        self.gridLayout_14.addWidget(self.cb_coupler_kick, 0, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.groupBox_9)
        self.groupBox_10 = QtGui.QGroupBox(self.tab)
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cb_otr55 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr55.setFont(font)
        self.cb_otr55.setObjectName(_fromUtf8("cb_otr55"))
        self.verticalLayout.addWidget(self.cb_otr55)
        self.cb_otr218 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr218.setFont(font)
        self.cb_otr218.setObjectName(_fromUtf8("cb_otr218"))
        self.verticalLayout.addWidget(self.cb_otr218)
        self.cb_otr450 = QtGui.QCheckBox(self.groupBox_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_otr450.setFont(font)
        self.cb_otr450.setObjectName(_fromUtf8("cb_otr450"))
        self.verticalLayout.addWidget(self.cb_otr450)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_13.addWidget(self.groupBox_10)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.cb_lattice = QtGui.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_lattice.setFont(font)
        self.cb_lattice.setObjectName(_fromUtf8("cb_lattice"))
        self.gridLayout_4.addWidget(self.cb_lattice, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.groupBox_3)
        self.gridLayout_9.addLayout(self.horizontalLayout_13, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pb_write_2 = QtGui.QPushButton(self.tab2)
        self.pb_write_2.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_write_2.setFont(font)
        self.pb_write_2.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);"))
        self.pb_write_2.setObjectName(_fromUtf8("pb_write_2"))
        self.horizontalLayout_3.addWidget(self.pb_write_2)
        self.pb_read_2 = QtGui.QPushButton(self.tab2)
        self.pb_read_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_read_2.setFont(font)
        self.pb_read_2.setStyleSheet(_fromUtf8("color: rgb(85, 255, 255);"))
        self.pb_read_2.setObjectName(_fromUtf8("pb_read_2"))
        self.horizontalLayout_3.addWidget(self.pb_read_2)
        self.frame_2 = QtGui.QFrame(self.tab2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pb_update_2 = QtGui.QPushButton(self.frame_2)
        self.pb_update_2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_update_2.setFont(font)
        self.pb_update_2.setObjectName(_fromUtf8("pb_update_2"))
        self.gridLayout_5.addWidget(self.pb_update_2, 5, 0, 1, 1)
        self.pb_reset_2 = QtGui.QPushButton(self.frame_2)
        self.pb_reset_2.setEnabled(True)
        self.pb_reset_2.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_reset_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_reset_2.setFont(font)
        self.pb_reset_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pb_reset_2.setObjectName(_fromUtf8("pb_reset_2"))
        self.gridLayout_5.addWidget(self.pb_reset_2, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget_3 = QtGui.QWidget(self.tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(700, 600))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_4 = QtGui.QWidget(self.tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(400, 200))
        self.widget_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.gridLayout_3.addWidget(self.widget_4, 0, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab3)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.label_18 = QtGui.QLabel(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_18.setFont(font)
        self.label_18.setMargin(5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_19.addWidget(self.label_18)
        self.verticalLayout_10.addLayout(self.verticalLayout_19)
        self.groupBox_7 = QtGui.QGroupBox(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 350))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.pb_edit_obj_func = QtGui.QPushButton(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_edit_obj_func.sizePolicy().hasHeightForWidth())
        self.pb_edit_obj_func.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pb_edit_obj_func.setFont(font)
        self.pb_edit_obj_func.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pb_edit_obj_func.setObjectName(_fromUtf8("pb_edit_obj_func"))
        self.gridLayout_11.addWidget(self.pb_edit_obj_func, 8, 0, 1, 2)
        self.cb_use_predef = QtGui.QCheckBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cb_use_predef.setFont(font)
        self.cb_use_predef.setObjectName(_fromUtf8("cb_use_predef"))
        self.gridLayout_11.addWidget(self.cb_use_predef, 7, 0, 1, 1)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.le_a = QtGui.QLineEdit(self.groupBox_7)
        self.le_a.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_a.setFont(font)
        self.le_a.setText(_fromUtf8(""))
        self.le_a.setObjectName(_fromUtf8("le_a"))
        self.verticalLayout_16.addWidget(self.le_a)
        self.le_b = QtGui.QLineEdit(self.groupBox_7)
        self.le_b.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_b.setFont(font)
        self.le_b.setObjectName(_fromUtf8("le_b"))
        self.verticalLayout_16.addWidget(self.le_b)
        self.le_c = QtGui.QLineEdit(self.groupBox_7)
        self.le_c.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_c.setFont(font)
        self.le_c.setObjectName(_fromUtf8("le_c"))
        self.verticalLayout_16.addWidget(self.le_c)
        self.le_d = QtGui.QLineEdit(self.groupBox_7)
        self.le_d.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_d.setFont(font)
        self.le_d.setObjectName(_fromUtf8("le_d"))
        self.verticalLayout_16.addWidget(self.le_d)
        self.le_e = QtGui.QLineEdit(self.groupBox_7)
        self.le_e.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_e.setFont(font)
        self.le_e.setObjectName(_fromUtf8("le_e"))
        self.verticalLayout_16.addWidget(self.le_e)
        self.le_obf = QtGui.QLineEdit(self.groupBox_7)
        self.le_obf.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.le_obf.setFont(font)
        self.le_obf.setObjectName(_fromUtf8("le_obf"))
        self.verticalLayout_16.addWidget(self.le_obf)
        self.sb_max_pen = QtGui.QSpinBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sb_max_pen.setFont(font)
        self.sb_max_pen.setMinimum(-1000)
        self.sb_max_pen.setMaximum(1000)
        self.sb_max_pen.setProperty("value", 100)
        self.sb_max_pen.setObjectName(_fromUtf8("sb_max_pen"))
        self.verticalLayout_16.addWidget(self.sb_max_pen)
        self.gridLayout_11.addLayout(self.verticalLayout_16, 0, 1, 1, 1)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_15.addWidget(self.label_16)
        self.label_19 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_15.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_15.addWidget(self.label_20)
        self.label_28 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_15.addWidget(self.label_28)
        self.label_29 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_15.addWidget(self.label_29)
        self.label_21 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_15.addWidget(self.label_21)
        self.label_26 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_15.addWidget(self.label_26)
        self.gridLayout_11.addLayout(self.verticalLayout_15, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.groupBox_7)
        self.groupBox_6 = QtGui.QGroupBox(self.tab3)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_13 = QtGui.QLabel(self.groupBox_6)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_13.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox_6)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_13.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.groupBox_6)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_13.addWidget(self.label_15)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.le_alarm = QtGui.QLineEdit(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.le_alarm.setFont(font)
        self.le_alarm.setObjectName(_fromUtf8("le_alarm"))
        self.horizontalLayout_9.addWidget(self.le_alarm)
        self.label_12 = QtGui.QLabel(self.groupBox_6)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.label_alarm = QtGui.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_alarm.setFont(font)
        self.label_alarm.setObjectName(_fromUtf8("label_alarm"))
        self.horizontalLayout_9.addWidget(self.label_alarm)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_17 = QtGui.QLabel(self.groupBox_6)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.sb_alarm_min = QtGui.QDoubleSpinBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_alarm_min.sizePolicy().hasHeightForWidth())
        self.sb_alarm_min.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sb_alarm_min.setFont(font)
        self.sb_alarm_min.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_alarm_min.setMinimum(-100.0)
        self.sb_alarm_min.setMaximum(100.99)
        self.sb_alarm_min.setSingleStep(0.1)
        self.sb_alarm_min.setProperty("value", 0.0)
        self.sb_alarm_min.setObjectName(_fromUtf8("sb_alarm_min"))
        self.horizontalLayout_6.addWidget(self.sb_alarm_min)
        self.label_22 = QtGui.QLabel(self.groupBox_6)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_6.addWidget(self.label_22)
        self.sb_alarm_max = QtGui.QDoubleSpinBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_alarm_max.sizePolicy().hasHeightForWidth())
        self.sb_alarm_max.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sb_alarm_max.setFont(font)
        self.sb_alarm_max.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_alarm_max.setMinimum(-100.0)
        self.sb_alarm_max.setMaximum(100.99)
        self.sb_alarm_max.setSingleStep(0.1)
        self.sb_alarm_max.setObjectName(_fromUtf8("sb_alarm_max"))
        self.horizontalLayout_6.addWidget(self.sb_alarm_max)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.sb_alarm_timeout = QtGui.QDoubleSpinBox(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_alarm_timeout.sizePolicy().hasHeightForWidth())
        self.sb_alarm_timeout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sb_alarm_timeout.setFont(font)
        self.sb_alarm_timeout.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_alarm_timeout.setMinimum(0.0)
        self.sb_alarm_timeout.setMaximum(100.0)
        self.sb_alarm_timeout.setSingleStep(0.1)
        self.sb_alarm_timeout.setProperty("value", 2.0)
        self.sb_alarm_timeout.setObjectName(_fromUtf8("sb_alarm_timeout"))
        self.horizontalLayout_10.addWidget(self.sb_alarm_timeout)
        self.label_24 = QtGui.QLabel(self.groupBox_6)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_10.addWidget(self.label_24)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.gridLayout_10.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.groupBox_6)
        self.groupBox_8 = QtGui.QGroupBox(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.sb_num_iter = QtGui.QSpinBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_num_iter.setFont(font)
        self.sb_num_iter.setMaximum(1000)
        self.sb_num_iter.setProperty("value", 50)
        self.sb_num_iter.setObjectName(_fromUtf8("sb_num_iter"))
        self.gridLayout_12.addWidget(self.sb_num_iter, 4, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_12.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_12.addWidget(self.label_25, 4, 0, 1, 1)
        self.cb_select_alg = QtGui.QComboBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cb_select_alg.setFont(font)
        self.cb_select_alg.setObjectName(_fromUtf8("cb_select_alg"))
        self.gridLayout_12.addWidget(self.cb_select_alg, 2, 1, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_12)
        self.cb_set_best_sol = QtGui.QCheckBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cb_set_best_sol.setFont(font)
        self.cb_set_best_sol.setObjectName(_fromUtf8("cb_set_best_sol"))
        self.verticalLayout_20.addWidget(self.cb_set_best_sol)
        self.verticalLayout_10.addWidget(self.groupBox_8)
        self.g_box_isim = QtGui.QGroupBox(self.tab3)
        self.g_box_isim.setEnabled(True)
        self.g_box_isim.setObjectName(_fromUtf8("g_box_isim"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.g_box_isim)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_23 = QtGui.QLabel(self.g_box_isim)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_8.addWidget(self.label_23)
        self.sb_isim_rel_step = QtGui.QDoubleSpinBox(self.g_box_isim)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_isim_rel_step.setFont(font)
        self.sb_isim_rel_step.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_isim_rel_step.setDecimals(2)
        self.sb_isim_rel_step.setMinimum(0.25)
        self.sb_isim_rel_step.setMaximum(100.0)
        self.sb_isim_rel_step.setSingleStep(0.25)
        self.sb_isim_rel_step.setObjectName(_fromUtf8("sb_isim_rel_step"))
        self.horizontalLayout_8.addWidget(self.sb_isim_rel_step)
        self.verticalLayout_18.addLayout(self.horizontalLayout_8)
        self.cb_use_isim = QtGui.QCheckBox(self.g_box_isim)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cb_use_isim.setFont(font)
        self.cb_use_isim.setObjectName(_fromUtf8("cb_use_isim"))
        self.verticalLayout_18.addWidget(self.cb_use_isim)
        self.verticalLayout_21.addLayout(self.verticalLayout_18)
        self.verticalLayout_10.addWidget(self.g_box_isim)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Ocelot Interface", None))
        self.pb_write.setText(_translate("Form", "Write to Quads", None))
        self.pb_read.setText(_translate("Form", "Read from Quads", None))
        self.pb_update.setText(_translate("Form", "Update Reference", None))
        self.pb_reset.setText(_translate("Form", "Reset All", None))
        self.groupBox_9.setTitle(_translate("Form", "Calc Options", None))
        self.cb_coupler_kick.setText(_translate("Form", "Coupler Kick", None))
        self.groupBox_10.setTitle(_translate("Form", "BackTracking", None))
        self.cb_otr55.setText(_translate("Form", "OTRC 55", None))
        self.cb_otr218.setText(_translate("Form", "OTRB 218", None))
        self.cb_otr450.setText(_translate("Form", "OTRB 450", None))
        self.groupBox_3.setTitle(_translate("Form", "Lattice", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Twiss Parameters", None))
        self.pb_write_2.setText(_translate("Form", "Write to Quads", None))
        self.pb_read_2.setText(_translate("Form", "Read from Quads", None))
        self.pb_update_2.setText(_translate("Form", "Update Reference", None))
        self.pb_reset_2.setText(_translate("Form", "Reset All", None))
        self.groupBox.setTitle(_translate("Form", "Controls", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "Orbit and Dispertion", None))
        self.label_18.setText(_translate("Form", "Objective and Alarm Function Setup", None))
        self.groupBox_7.setTitle(_translate("Form", "Objective Function", None))
        self.pb_edit_obj_func.setText(_translate("Form", "Edit Objective Function", None))
        self.cb_use_predef.setText(_translate("Form", "Use Predefined Objective Function", None))
        self.le_obf.setText(_translate("Form", "A", None))
        self.label_16.setText(_translate("Form", "PV: A", None))
        self.label_19.setText(_translate("Form", "PV: B", None))
        self.label_20.setText(_translate("Form", "PV: C", None))
        self.label_28.setText(_translate("Form", "PV: D", None))
        self.label_29.setText(_translate("Form", "PV: E", None))
        self.label_21.setText(_translate("Form", "Objective Function:", None))
        self.label_26.setText(_translate("Form", "Max Penalty", None))
        self.groupBox_6.setTitle(_translate("Form", "Machine Status", None))
        self.label_13.setText(_translate("Form", "Alarm 1", None))
        self.label_14.setText(_translate("Form", "Limits:     ", None))
        self.label_15.setText(_translate("Form", "Wait", None))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Value:    </span></p></body></html>", None))
        self.label_alarm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">0</span></p></body></html>", None))
        self.label_17.setText(_translate("Form", "Min   ", None))
        self.label_22.setText(_translate("Form", "          Max    ", None))
        self.label_24.setText(_translate("Form", "sec after recovering                             ", None))
        self.groupBox_8.setTitle(_translate("Form", "Scanner Parameters", None))
        self.label_27.setText(_translate("Form", "Select Optimiser Algorithm ", None))
        self.label_25.setText(_translate("Form", "Number Iterations", None))
        self.cb_set_best_sol.setText(_translate("Form", "Set Best Solution After Optimization", None))
        self.g_box_isim.setTitle(_translate("Form", "Simplex/Scipy Scanner Setup", None))
        self.label_23.setText(_translate("Form", "Relative Step in %", None))
        self.cb_use_isim.setText(_translate("Form", "Use Initial Simplex/Step [step =(Max - Min) x RelStep[%]]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Form", "Objective Function", None))

