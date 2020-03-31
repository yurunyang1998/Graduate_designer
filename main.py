# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

This program centers a window
on the screen.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""
from PyQt5.QtWidgets import QFileDialog,QMainWindow,QApplication,QMessageBox,QErrorMessage
from PyQt5.QtGui import QStandardItemModel,QStandardItem
import os
from mainUI import  Ui_MainWindow
import excelparse,sys
import  dicomWarper
import sheetDialog



def listdir(path, list_name): #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
      # if os.path.isdir(file_path):
      #   listdir(file_path, list_name)
      # else:
        list_name.append(file_path)
def alert(Qwidget, message):
        reply = QMessageBox.information(Qwidget, '提示', message, QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Close)


class mainpage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainpage,self).__init__()
        self.setupUi(self)
        self.actionroot.triggered.connect(self.openfiledirectory)
        self.actionset_rt_structure.triggered.connect(self.opendicomfiles)
        self.menu_plastimatch.triggered.connect(self.setplastimatch)
        self.actionchoose_excel_file.triggered.connect(self.openexcelfile)
        self.pushButton.clicked.connect(self.extractrt)
        self.pushButton_2.clicked.connect(self.convertrtstructure2nrrd)
        self.pushButton_3.clicked.connect(self.convertCT2nrrd)

        # self.combo = sheetDialog.SheetDialog()

        self.rootdir=""
        self.excelfile=""
        self.dicomfile=""
        self.plastimatch=""

    def openfiledirectory(self):
        try:
            self.rootdir = QFileDialog.getExistingDirectory(self, '打开文件','./')
            self.filelist = []
            listdir(self.rootdir,self.filelist)   #获取当前文件夹下所有文件路径
            self.listWidget.clear()
            for i in self.filelist:
                # print(i)
                self.listWidget.addItem(i)
        except Exception as e:
            alert(self,str(e))
            print(e)

    def opendicomfiles(self):
        try:
            if(self.rootdir == ""):
                raise FileNotFoundError
            self.dicomfile = QFileDialog.getOpenFileName(self,"选择dicom文件",self.rootdir)[0]
            # print(self.dicomfile)
            self.listWidget_2.clear()
            self.listWidget_2.addItem(self.dicomfile)
            dicomWarper_ = dicomWarper.dicomWarper(self.dicomfile)
            self.showrtinfo(dicomWarper_)

        except FileNotFoundError as e :
            alert(self,"please choose a root diretory firstly")

        except Exception as e:
            print(e)

    def openexcelfile(self):
        try:
            self.excelfile = QFileDialog.getOpenFileName(self, "选择excel文件",'./')[0]
            self.excelParse = excelparse.ExcelParse(self.excelfile,None)

            sheets = self.excelParse.getsheet()

            combox = sheetDialog.SheetDialog()
            combox.AddList(sheets)
            combox.exec_()    #以阻塞方式运行

            sheetname = combox.getsheet()

            self.excelParse.readsheet(self.excelfile,sheetname)   # 读取指定的表
            rows, cols  = self.excelParse.getshape()

            self.excelmodel = QStandardItemModel(rows, cols)
            self.excelmodel.setHorizontalHeaderLabels(self.excelParse.getcolumns())       #设置列名
            for row in range(rows):
                for column in range(cols):
                    item = QStandardItem(str(self.excelParse.getdata(row,column)))
                    # 设置每个位置的文本值
                    self.excelmodel.setItem(row, column, item)
            self.tableView.setModel(self.excelmodel)

        except Exception as e:
            s = sys.exc_info()
            print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
            alert(self,str(e))

    def setplastimatch(self):
        self.plastimatch = QFileDialog.getOpenFileName(self, "选择plstimatch", self.rootdir)[0]
        f = os.popen(self.plastimatch)
        if ("plastimatch version" in f.read()):
            alert(self,"选取成功")
        else:
            alert(self,"选取错误")
            self.plastimatch=""

    def showrtinfo(self,dicomWarper_):
        rt = dicomWarper_.getstruct()
        self.listmodel = QStandardItemModel()
        self.listmodel.clear()
        index = 0
        for i in rt:
            index = index+1
            item = QStandardItem(str("ID : {0}  Name: {1}".format(rt[i]['id'],rt[i]['name'])))
            self.listmodel.setItem(index-1,item)
        self.listView.setModel(self.listmodel)


    def extractrt(self):
        if (self.dicomfile == "" or self.rootdir == "" or self.excelfile == ""):
            alert(self, "请先选择dicomfile 和 根目录 和 excel文件")
            return

        rootlen = len(self.filelist[0])
        midpath = self.dicomfile[rootlen:]
        step = 0
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(len(self.filelist))
        for index, file in enumerate(self.filelist):
            print(index)
            try:
                rtpath = file + midpath
                GTV = self.excelParse.getdata(index, 1)
                dw_ = dicomWarper.dicomWarper(rtpath)
                dw_.removeOtherGTV(GTV, rtpath + '\\..')

                step = step + 1
                self.progressBar.setValue(step)
            except Exception as e:
                alert(self, str(e))
        alert(self,"提取完成！")


    def convertrtstructure2nrrd(self):
        if(self.plastimatch==""):
            self.setplastimatch()

        else:
            rootlen = len(self.filelist[0])
            midpath = self.dicomfile[rootlen:]
            step = 0
            self.progressBar_2.setMaximum(rootlen)
            self.progressBar_2.setValue(0)
            for index, file in enumerate(self.filelist):
                try:

                    fatherpath = os.path.split(file + midpath)[0]
                    input = fatherpath + "/newrtfile.dcm"
                    outputssimg = fatherpath + "/newrtfile.nrrd"
                    referencedct = file + '/CT'

                    if (not os.path.exists(referencedct) or not os.path.exists(input)):
                        raise FileExistsError(referencedct)

                    cmd = "{0} convert --input {1} --output-ss-img {2} --referenced-ct {3}".format(self.plastimatch,
                                                                                                   input, outputssimg,
                                                                                                   referencedct)
                    result = os.popen(cmd)
                    step = step + 1
                    self.progressBar_2.setValue(step)

                    if ("Finished" not in result.read()):
                        raise
                except FileExistsError as e:
                    alert(self, str(e + "not existed"))


                except Exception as e:
                    print(e)
                    alert(self, str(e))
    def convertCT2nrrd(self):
        if (self.dicomfile == "" or self.rootdir == "" or self.excelfile == ""):
            alert(self, "请先选择dicomfile 和 根目录 和 excel文件")
            return
        if (self.plastimatch == ""):
            self.setplastimatch()
        else:
            CTpath =  QFileDialog.getExistingDirectory(self,"选择CT目录", self.filelist[0])
            if(not os.path.exists(CTpath)):
                return

            lens = len(self.filelist[0])
            midpath = CTpath[lens:]
            step = 0
            self.progressBar_3.setValue(0)
            self.progressBar_3.setMaximum(lens)
            for index,file in enumerate(self.filelist):
                try:
                    CTpath = file+midpath
                    outputpath = CTpath+"\\CTdata.nrrd"
                    cmd = "{0} convert --input {1} --output-img {2} ".format(self.plastimatch,CTpath,outputpath)
                    f=os.popen(cmd)
                    result = f.read()
                    if("Finished!" not  in result):
                        raise IOError
                    else:
                        step = step + 1
                        self.progressBar_3.setValue(step)

                except Exception as e:
                    alert(self,file+"convert error")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainpage()
    ex.show()
    sys.exit(app.exec_())


