import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_hostcomputer import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class update_serial(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super(update_serial, self).__init__()
        self.setupUi(self)

        '''
            Bind a user-defined function to a user-defined signal. When 
            the receiver receives this signal, it will execute this function
        '''
        self.update_serialport.clicked.connect(self.refresh_serial_clicked)
        self.open_serialport.clicked.connect(self.open_window_clicked)

    '''serialport update'''    
    def refresh_serial_clicked(self):
        self.serialport_select.clear()
        serialport = QSerialPort()
        serialport_list = QSerialPortInfo.availablePorts()
        if len(serialport_list) == 0: print('Serial port detection failed!')
        else: print('Serial port detection succeeded')
        for serialport_info in serialport_list:
            serialport.setPort(serialport_info)
            if serialport.open(QSerialPort.ReadWrite) == False:
                self.serialport_select.addItem(serialport_info.portName())
                serialport.close()

    def open_window_clicked(self):
        comName = self.Com_Name_Combo.currentText()
        comBaud = int(self.Com_Baud_Combo.currentText())
        self.com.setPortName(comName)
        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except:
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        self.Com_Close_Button.setEnabled(True)
        self.Com_Open_Button.setEnabled(False)
        self.Com_Refresh_Button.setEnabled(False)
        self.Com_Name_Combo.setEnabled(False)
        self.Com_Baud_Combo.setEnabled(False)
        self.Com_isOpenOrNot_Label.setText('  已打开')
        self.com.setBaudRate(comBaud)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ui = Ui_MainWindow()
    # mainWindow = QMainWindow()
    # ui.setupUi(mainWindow)
    mainWindow = update_serial()
    mainWindow.show()
    sys.exit(app.exec_())