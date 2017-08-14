from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import xlwt
import sys
import test
import time
class OnePage(QDialog):
    def __init__(self, parent=None):
        super(OnePage, self).__init__(parent)
        self.resize(1100, 600)
        self.content = None
        self.LIST = []
        self.init()
    def init(self):
        self.shop=QLineEdit()
        self.keywords=QLineEdit()
        self.highPrice=QLineEdit()
        self.lowPrice=QLineEdit()
        self.shop.setFixedSize(120, 20)
        self.keywords.setFixedSize(120, 20)
        self.highPrice.setFixedSize(60, 20)
        self.lowPrice.setFixedSize(60, 20)
        self.gettitlebutton=QPushButton('获取标题')
        self.copytitlebutton=QPushButton('一键复制标题')
        self.copyurlbutton=QPushButton('一键复制链接')
        self.outbutton=QPushButton('导出')
        self.gettitlebutton.setFixedSize(70,25)
        self.copytitlebutton.setFixedSize(85,25)
        self.copyurlbutton.setFixedSize(85,25)
        self.outbutton.setFixedSize(60,25)
        self.lableshop=QLabel('店铺：')
        self.lablekeyword=QLabel('关键词：')
        self.lablehigh=QLabel('最高价：')
        self.lablelow=QLabel('最低价：')
        self.lablestate=QLabel('状态：')
        self.lableshop.setFixedSize(30,20)
        self.lablekeyword.setFixedSize(40,20)
        self.lablehigh.setFixedSize(45,20)
        self.lablelow.setFixedSize(45,20)
        self.contenttable=QTableWidget()
        self.contenttable.setColumnCount(3)
        self.contenttable.setHorizontalHeaderLabels(['编号', '标题', '链接'])
        self.contenttable.verticalHeader().setVisible(False)
        self.contenttable.setColumnWidth(0,100)
        self.contenttable.setColumnWidth(1,480)
        self.contenttable.setColumnWidth(2,479)
        self.nextpagebutton=QPushButton("获取全部")




        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox.addWidget(self.lableshop)
        hbox.addWidget(self.shop)
        hbox.addWidget(self.lablekeyword)
        hbox.addWidget(self.keywords)
        hbox.addWidget(self.lablehigh)
        hbox.addWidget(self.highPrice)
        hbox.addWidget(self.lablelow)
        hbox.addWidget(self.lowPrice)
        hbox.addWidget(self.gettitlebutton)
        hbox.addWidget(self.copytitlebutton)
        hbox.addWidget(self.copyurlbutton)
        hbox.addWidget(self.outbutton)
        hbox.addWidget(self.lablestate)
        vbox.addLayout(hbox)
        vbox.addWidget(self.contenttable)
        hbox2=QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(self.nextpagebutton)
        hbox2.addStretch()
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

        self.gettitlebutton.clicked.connect(self.returnlist)
        self.contenttable.itemClicked.connect(self.outselect)
        self.copytitlebutton.clicked.connect(self.copyfunction)
        self.copyurlbutton.clicked.connect(self.copyfunction)
        self.outbutton.clicked.connect(self.outdata)
        self.nextpagebutton.clicked.connect(self.nextpage)


#     #根据self.urlist 显示下一页
    def nextpage(self):
        # if self.LIST:
        #     self.dealLIST()  # 显示下页的内容（因为重复调用了next（list））
        #     # self.lablestate.setText('当前页已更新！')
        # else:
        #     self.lablestate.setText('没有下一页了！')
        if self.LIST:
            lis = list(self.LIST)
            for i in range(0, len(lis)):
                l = lis[i]
                self.titlelist.extend(l[0])
                self.urllist.extend(l[1])
                rowcount = self.contenttable.rowCount()  # 清空之前搜索的数据
                for i in range(0, rowcount):
                    self.contenttable.removeRow(0)
                self.a = 0
                self.showTablecontent(self.titlelist, self.urllist)
        else:
            self.lablestate.setText('请输入店铺名！')
    #这个函数是一个解析self.LIST的函数，它将解析后的数据传递给showtable函数展示数据给用户
    def dealLIST(self):
        lis = self.LIST
        try:
            t = next(lis)
            tit = t[0]
            url = t[1]
            self.titlelist.extend(tit)  # 导出用
            self.urllist.extend(url)  # 导出用
            self.showTablecontent(tit, url)#展示数据
            self.lablestate.setText('当前页已展示！')
        except:
            #告诉用户数据获取完了
            self.lablestate.setText('数据获取结束！')

    #这是一个初始化test中shop类的函数，这个函数将返回第一次获取的list列表（点击获取数据按钮时执行）
    def returnlist(self):
        self.titlelist = []  # 存储最后导出的数组
        self.urllist = []
        self.a = 0#初始化页数
        rowcount = self.contenttable.rowCount()#清空之前搜索的数据
        for i in range(0, rowcount):
            self.contenttable.removeRow(0)
        SHOPNAME = self.checkinput()#检查店铺名的输入情况
        KEY = test.deal_keyword(self.keywords.text())#对输入的关键字进行转码
        LOW = self.lowPrice.text()
        HIGH = self.highPrice.text()
        if SHOPNAME:
            SHOP = test.shop(SHOPNAME)#初始化shop类
            LIST = SHOP.getneed(KEY, LOW, HIGH)
            if LIST != False:
                self.LIST = LIST#返回的是个可迭代对象
                self.dealLIST()#显示第一页的内容
            else:
                #list列表没有获取到数据，要让用户知道list为空
                self.lablestate.setText('获取数据失败！')
                # return False

    #这是一个校验输入内容的功能函数(主要校验店铺名，因为店铺名不能为空)
    def checkinput(self):
        shopname = self.shop.text()  # 输入的店铺名称
        if shopname:
            return shopname
        else:
            #(希望在这里执行将店铺名没有输入展示给用户)
            self.lablestate.setText('请输入店铺名称！')
            return False

    #这是一个展示列表的功能函数，需要两个列表参数
    def showTablecontent(self, tit, url):
        # self.contenttable.clearContents()#每次翻页清空之前页面
        for i in range(0, len(tit)):
            self.contenttable.insertRow(i)
            self.newnumber = QTableWidgetItem(str(self.a+1))
            self.newtitle = QTableWidgetItem(tit[i])
            self.newurl = QTableWidgetItem(url[i])
            self.contenttable.setItem(i, 0, self.newnumber)
            self.contenttable.setItem(i, 1, self.newtitle)
            self.contenttable.setItem(i, 2, self.newurl)
            self.a += 1


    #这两个函数是复制功能函数（当选中列表中的内容时，点击按钮可以复制）
    def outselect(self, Item = None):
        if Item==None:
            return
        self.content = Item.text()
    def copyfunction(self):
        #设置Item.text（）到剪切板
        if self.content:
            clipboard =QApplication.clipboard()
            clipboard.setText(self.content)
        else:
            self.lablestate.setText('未选中内容!')
            #print('未选中内容')


    #导出用已获取列表导出到excle(需要的是全部数据的列表（这个动作必须在翻完所有页后才会得到正确执行）)
    def outdata(self):
        QMessageBox.information(self, "提示", "即将开始导出，请确认！", QMessageBox.Ok)
        if self.LIST:
            lis = list(self.LIST)
            for i in range(0, len(lis)):
                l = lis[i]
                self.titlelist.extend(l[0])
                self.urllist.extend(l[1])
        # if self.titlelist:
            f = xlwt.Workbook()  # 创建工作簿
            sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
            first_col = sheet1.col(0)
            first_col.width = 256*8
            sec_col = sheet1.col(1)
            sec_col.width = 256*65
            thr_col = sheet1.col(2)
            thr_col.width = 256*80
            # 创建sheet
            for i in range(len(self.titlelist)):
                sheet1.write(i, 0, i+1, xlwt.easyxf('align: wrap on, vert centre, horiz centre;'))
                sheet1.write(i, 1, self.titlelist[i], xlwt.easyxf('align: wrap on, vert centre, horiz centre;'))  # 表格的第一行开始写。第一列，第二列。。。。
                sheet1.write(i, 2, self.urllist[i], xlwt.easyxf('align: wrap on, vert centre, horiz centre;'))
            # sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
            f.save(self.shop.text()+self.lowPrice.text()+'-'+self.highPrice.text()+'.xls')  # 保存文件
            self.lablestate.setText('导出成功')
        else:
            self.lablestate.setText('导出失败！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = OnePage()
    t.setWindowTitle('淘宝助手')
    t.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
    t.show()
    app.exec_()

