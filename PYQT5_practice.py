#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.title=" PyQt5 Window "
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("iconfinder_exit_6035.png"))
        
        self.InitWindow()
        
    def InitWindow(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


# In[2]:


import os


# In[4]:


os.getcwd()
os.chdir("D:\code_practice")
os.getcwd()


# In[11]:


from PyQt5.QtCore import QDateTime, QDate,QTime,Qt

datetime = QDateTime.currentDateTime()
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))

date = QDate.currentDate()

print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))

time = QTime.currentTime()

print(time.toString())
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))


# In[1]:


from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox, QStatusBar
from PyQt5.QtCore import QCoreApplication
import sys

class Window_1(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title=" PyQt5 pushButton practice "
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        
        button = QPushButton(" Close ",self)
        button.move(200,200)
        button.setToolTip(" <h3> This is click button </h3> ")
        button.clicked.connect(self.CloseApp)
        
        button_about = QPushButton(" AboutBox ", self)
        button_about.move(400,200)
        button_about.clicked.connect(self.AboutMessage)

        
        self.InitUI()
        
    def InitUI(self):
        
        self.statusBar().showMessage(" I want to Drinking now ! ")
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
        
    def close(self):
        QCoreApplication.instance().quit()
        
    def CloseApp(self):
        reply = QMessageBox.question(self, " Close Message ", " Are you sure to close window ", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.close()
            
    def AboutMessage(self):
        QMessageBox.about(self, " About Message ", " This is about Message box ")
    
        
App_1 = QApplication(sys.argv)
window_1 = Window_1()
sys.exit(App_1.exec())
        
     

