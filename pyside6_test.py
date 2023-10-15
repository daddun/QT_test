from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Window:
    def __init__(self):
        super(Window, self).__init__()

        # 加载ui文件
        qfile = QFile("side6.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        # 创建ui窗口对象
        self.ui = QUiLoader().load(qfile)
        # self.ui.button.clicked.connect(self.btnClick)

    def btnClick(self):
        info = self.ui.textEdit.toPlainText()   # 获取文本信息
        print(info)

if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = Window()
    w.ui.show()
    app.exec()