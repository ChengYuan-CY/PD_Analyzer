#-------------------------------------------------
#
# Project created by QtCreator 2017-02-13T11:47:48
#
#-------------------------------------------------

QT       += core gui
QT       += serialport

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = PD_Analyzer
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += main.cpp\
        mainwindow.cpp \
    aboutpdanalyzerdialog.cpp

HEADERS  += mainwindow.h \
    aboutpdanalyzerdialog.h

FORMS    += mainwindow.ui \
    aboutpdanalyzerdialog.ui \
    buffersetting.ui \
    findDialog.ui \
    xx_mainwindow.ui

DISTFILES += \
    communication.py

INCLUDEPATH += -I C:\Python27_32bit\include
LIBS += -L C:\Python27_32bit\libs -lpython27

RESOURCES += \
    open.qrc
