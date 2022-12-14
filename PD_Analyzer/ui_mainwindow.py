# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created: Wed Mar 08 18:40:58 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 754)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.splitter = QtGui.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.msgTreeView = QtGui.QTreeView(self.splitter)
        self.msgTreeView.setObjectName("msgTreeView")
        self.rawTableWidget = QtGui.QTableWidget(self.splitter)
        self.rawTableWidget.setObjectName("rawTableWidget")
        self.rawTableWidget.setColumnCount(0)
        self.rawTableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuCapture = QtGui.QMenu(self.menuBar)
        self.menuCapture.setObjectName("menuCapture")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent_Files = QtGui.QAction(MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExamples = QtGui.QAction(MainWindow)
        self.actionExamples.setObjectName("actionExamples")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next = QtGui.QAction(MainWindow)
        self.actionFind_Next.setObjectName("actionFind_Next")
        self.actionGoto = QtGui.QAction(MainWindow)
        self.actionGoto.setObjectName("actionGoto")
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionEvent_Trigger = QtGui.QAction(MainWindow)
        self.actionEvent_Trigger.setObjectName("actionEvent_Trigger")
        self.actionBuffer_Setting = QtGui.QAction(MainWindow)
        self.actionBuffer_Setting.setObjectName("actionBuffer_Setting")
        self.actionMessage_View = QtGui.QAction(MainWindow)
        self.actionMessage_View.setObjectName("actionMessage_View")
        self.actionRaw_Data = QtGui.QAction(MainWindow)
        self.actionRaw_Data.setObjectName("actionRaw_Data")
        self.actionAbout_PD_Analyzer = QtGui.QAction(MainWindow)
        self.actionAbout_PD_Analyzer.setObjectName("actionAbout_PD_Analyzer")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExamples)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Next)
        self.menuEdit.addAction(self.actionGoto)
        self.menuCapture.addAction(self.actionConnect)
        self.menuCapture.addAction(self.actionDisconnect)
        self.menuCapture.addAction(self.actionRun)
        self.menuCapture.addAction(self.actionPause)
        self.menuCapture.addAction(self.actionStop)
        self.menuCapture.addAction(self.actionEvent_Trigger)
        self.menuCapture.addAction(self.actionBuffer_Setting)
        self.menuView.addAction(self.actionMessage_View)
        self.menuView.addAction(self.actionRaw_Data)
        self.menuAbout.addAction(self.actionAbout_PD_Analyzer)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuCapture.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "USB PD Analyzer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCapture.setTitle(QtGui.QApplication.translate("MainWindow", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_Files.setText(QtGui.QApplication.translate("MainWindow", "Recent Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExamples.setText(QtGui.QApplication.translate("MainWindow", "Examples", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Next.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoto.setText(QtGui.QApplication.translate("MainWindow", "Goto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEvent_Trigger.setText(QtGui.QApplication.translate("MainWindow", "Event Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuffer_Setting.setText(QtGui.QApplication.translate("MainWindow", "Buffer Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMessage_View.setText(QtGui.QApplication.translate("MainWindow", "Message View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRaw_Data.setText(QtGui.QApplication.translate("MainWindow", "Raw Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_PD_Analyzer.setText(QtGui.QApplication.translate("MainWindow", "About PD Analyzer", None, QtGui.QApplication.UnicodeUTF8))

