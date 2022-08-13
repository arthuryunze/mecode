# QT中三个Edit区别



QLineEdit是单行文本输入，一般用于用户名、密码等少量文本交互地方。
QTextEdit用于多行文本，也可以显示HTML格式文本。
QPlainTextEdit与QTextEdit很像，但它多用于需要与文本进行处理的地方，而QTextEdit多用于显示，可以说，QPlainTextEdit对于plain text处理能力比QTextEdit强。


## QListWidget添加Item

使用第一种方式：

```cpp
QStringList strList;



	strList<< "Item1"<<"Item2"<< "Item3"<<"Item4";



 



	this->addItems(strList);
```





### 获取QListWidget中的所有内容 

遍历

```
for` `(``int` `j = 0; j < ui->listWidget->count(); j++)
{
    ``QString itemText = ui->listWidget->item(j)->text();
｝
```

### Qt QListWidget clear() 清空所有项

QListWidget clear()



### QListWidget删除Item

第一种是

QListWidgetItem *takeItem(int row);

第二种是

inline void removeItemWidget(QListWidgetItem *item);

需要知道删除的Item的对象。 



### QListWidget 内部拖拽

[[技术博客\]Pyqt5实现Widget内部拖拽 - assem - 博客园](https://www.cnblogs.com/dszw/p/10919956.html)

QWidget 打开acceptDrops

QAbstractItemView 打开dragEnabled





### Qt高分屏适配

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)





##  [     [编程心得\]PyQt中让按钮保持按下状态         ](https://www.cnblogs.com/emagic/archive/2012/05/15/2500984.html)         







近日舍得在开发SuperMemo转换精灵体验版的时候遇到了一个问题,舍得需要左侧一个竖排的工具栏,工具栏中的按钮点下后高亮为蓝色,而且点击后一直保持这种高亮状态.直到另一个按钮按下,把它替换掉为止,就象下面这个效果:

[![SNAG-0043](https://images.cnblogs.com/cnblogs_com/emagic/201205/201205150959032856.png)](http://images.cnblogs.com/cnblogs_com/emagic/201205/201205150959034874.png)

在实际使用的时候发现了问题:当鼠标在主窗口的其它位置点击的时候,这个蓝色高亮状态就消失了,舍得尝试了很多种方法,什么信号槽啊，事件啊啥的，一直找不到一个妥善的解决方案，这几乎已经成为舍得心头的一根刺了。

直到今天，在度娘的帮助下，找到了一篇文章《[Qt保持状态的Button](http://hi.baidu.com/cmdmac_scut_edu_cn/blog/item/e46d6fee91c8cff6b3fb95ca.html)》，直觉告诉我这个可以解决，马上动手测试，终于把这根刺给干掉了。

下面是解决的方案：

在按钮中应用下面的函数：

```
        self.scriptBtn.setCheckable(True)
        self.scriptBtn.setAutoExclusive(True)
```

像舍得上面这幅图中总共5个按钮，需要一一设置。

然后在QSS样式表中设置：

```
QPushButton::checked,QToolButton::checked{
    background: #3C79F2;
    border-color: #11505C;
    font-weight: bold;
    font-family:"Microsoft YaHei";
}
```

就完成了舍得预期的效果,每个按钮点中后高亮,直至另一个按钮被点击;鼠标即使在非按钮区点击,高亮效果仍然保留.  

reference: [[编程心得\]PyQt中让按钮保持按下状态 - 舍得学苑 - 博客园](https://www.cnblogs.com/emagic/archive/2012/05/15/2500984.html)



### 字体颜色设置



```css
/*字体为微软雅黑*/
    font-family:Microsoft Yahei;
    /*字体大小为20点*/
    font-size:20pt;
    /*字体颜色为白色*/    
    color:white;
    /*背景颜色*/  
    background-color:rgb(14 , 150 , 254);
```



### QSlider 滑块

[PyQt - QSlider Widget & Signal - Tutorialspoint](https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm)





### QLabel隐藏

`hiding the label`

```
    ``self``.label_2.setHidden(``True``)
```



### 设置回车快捷键

```
self.signIn.setShortcut(QtCore.Qt.Key_Return)  #笔记
```





### pyqt支持MySQL数据库

#### How to Build the QMYSQL Plugin on Unix and macOS

You need the MySQL / MariaDB header files, as well as the shared library `libmysqlclient.so` / `libmariadb.so`. Depending on your Linux distribution, you may need to install a package which is usually called "mysql-devel" or "mariadb-devel".

Tell [qmake](https://doc.qt.io/qt-5/qmake-manual.html) where to find the MySQL / MariaDB header files and shared libraries (here it is assumed that MySQL / MariaDB is installed in `/usr/local`) and run `make`:

```
cd $QTDIR/qtbase/src/plugins/sqldrivers
qmake -- MYSQL_PREFIX=/usr/local
make sub-mysql
```







setSizePolicy 是设置控件在布局（layout）里面的大小变化的属性。如果控件没有在布局里，没什么用。

 

默认情况下，把 widget 放入 layout，widget 的大小一定程度上会随着 layout 变大而变大或者缩小而缩小；可以设置  widget 的 sizePolicy、minmunSize 和 maxmumSize，使其一定程度上不受 layout  的影响，但是不是说设置了 widget 的最小高度后，widget 就一定能显示这么大的高度，当 layout 减小到比 widget  最小高度更小的尺寸，widget 显示的不是按比例缩小，而是不完全显示。

 

把几个 widget 放入 layout 里面，可以通过设置 widget 的 sizePolicy、minmumSize 和  maxmumSize，layout 的 layoutStretch 和 layoutSpacing，从而控制 widget 的大小和相对位置。



**GUI界面假死的处理**
*在GUI程序中，主线程也叫GUI线程，因为它是唯一被允许执行GUI相关操作的线程。对于一些耗时的操作，如果放在主线程中，就是出现界面无法响应的问题。这种问题的解决一种方式是，把这些耗时操作放到次线程中，还有一种比较简单的方法：在处理耗时操作中频繁调用QApplication::processEvents()。这个函数告诉Qt去处理那些还没有被处理的各类事件，然后再把控制权返还给调用者。*

```
    QElapsedTimer et;  
    et.start();  
    while(et.elapsed()<300)  
        QCoreApplication::processEvents();  
```


### Qt程序打包时可能需要unixodbc

[Install the Microsoft ODBC driver for SQL Server (Linux) - ODBC Driver for SQL Server | Microsoft Docs](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)

[(7条消息) Ubuntu安装ODBC驱动——SQLServer_李的博客-CSDN博客](https://blog.csdn.net/u013894391/article/details/116708115)

[odbc - Installing unixodbc on 19.10 - Ask Ubuntu](https://askubuntu.com/questions/1183140/installing-unixodbc-on-19-10)

### Qt程序打包过程
[在 Ubuntu 下使用 linuxdeployqt 发布 Qt 程序 - 我的程序笔记](https://huayig.cn/index.php/archives/89/)

[(7条消息) 使用linuxdeployqt在linux下进行Qt打包发布(超详细)_百里杨的博客-CSDN博客](https://blog.csdn.net/zyhse/article/details/106381937)

[将Qt程序打包成appImage发布的方法 - 知乎](https://zhuanlan.zhihu.com/p/353959035)

[linux-ubuntu下使用linuxdeployqt+appimagetool将qt程序打包成xxx.AppImage文件 - 程序员大本营](https://www.pianshen.com/article/92981376422/)

[(7条消息) Linux Qt程序打包成一个可执行文件_hktkfly6的专栏-CSDN博客](https://blog.csdn.net/hktkfly6/article/details/80752213?utm_term=qt%E5%9C%A8linux%E7%B3%BB%E7%BB%9F%E4%B8%8B%E7%94%9F%E6%88%90%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-0-80752213&spm=3001.4430)

[Deploying a Qt5 Application Linux - Qt Wiki](https://wiki.qt.io/Deploying_a_Qt5_Application_Linux)

## 【Qt】错误GL/gl.h: No such file or directory的解决方法（以及cannot find -lGL解决方法）



[(8条消息) 【Qt】错误GL/gl.h: No such file or directory的解决方法（以及cannot find -lGL解决方法）_郭老二-CSDN博客](https://blog.csdn.net/u010168781/article/details/80896797)



> 【Qt】错误GL/gl.h: No such file or directory的解决方法（以及cannot find -lGL解决方法）