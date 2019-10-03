# Tetris_pyqt5（俄罗斯方块）
Tetris using pyqt5

俄罗斯方块是一款经典的游戏  
本程序基于python3.7，使用pyqt5完成了图形界面的俄罗斯方块  

## 运行方式  
直接运行main.py文件

## 操作方式  
* 左右键移动方块
* 上下键旋转方块
* D键加速方块下落
* 空格直接放置底部
* 左下角显示分数

## 文件结构
* Tetrominoe.py定义8种方块的索引，用0-7表示
* Shape.py使用Terominoe.py中的索引，封装了方块的坐标和形状，以及相应的方法
* Board.py实现了游戏主要的逻辑
* Tetris.py使用pyqt5定义游戏界面、窗口
* main.py是游戏的入口，直接运行即可开始游戏
