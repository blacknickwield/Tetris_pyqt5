"""
PyQt5实现俄罗斯方块

author：张艺川
last edit time：2019年10月3号

参考：http://code.py40.com/2052.html
代码包括四个类：Tetris, Board, Tetrominoe, Shape

Tetris类存放游戏
Board编写游戏逻辑
Tetrominoe类包含所有俄罗斯名字
Shape包含俄罗斯方块的代码

在比赛开始后立即启动
我们可以通过按p键暂停游戏
空格键将立即把俄罗斯方块块底部

分数是已经删除的行数
"""
import sys
from PyQt5.QtWidgets import QApplication
from Tetris import Tetris


if __name__ == '__main__':

    # 每一pyqt5应用程序必须创建一个应用程序对象
    # sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)

    # 实例化Tetris()
    tetris = Tetris()

    # 系统exit()方法确保应用程序干净的退出
    sys.exit(app.exec_())
