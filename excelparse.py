import  pandas as pd
import  logging
from PyQt5.QtWidgets import QMessageBox
import sys


def alert(Qwidget, message):
    reply = QMessageBox.information(Qwidget, '提示', message, QMessageBox.Ok | QMessageBox.Close,
                                 QMessageBox.Close)


class ExcelParse:
    def __init__(self,filename,sheet=0):
        self.data =pd.read_excel(filename, sheet)

    def readsheet(self,filename,sheetname):
        self.data = pd.read_excel(filename,sheet_name=sheetname)

    def getshape(self):
        if(self.data is not None):
            return self.data.shape

    def getsheet(self):
        return self.data.keys()

    def getdata(self,row,col):
        return self.data.ix[row,col]

    def getcolumns(self):
        return self.data.columns
if __name__ == '__main__':
    excel = ExcelParse("C:\\Users\yurunyang\Desktop\毕业设计\INFO_GTVcontours_HN.xlsx",None)
    # print(excel.getdata(13,2))
    print(excel.getsheet())