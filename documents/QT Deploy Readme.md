# Qt UI 发布移植

Document Number: D-0001  
Document Type: Dev  
Document Author: Yunze  
Last Updated: 2022/08/13  

|Version|Date|Author|Description of Changes|
|---|---|---|---|
|0.2|2022/08/13|Yuzne|Update deprecated doc|
|0.1|2021/11/09|Yuzne|Initial Documents|


## 软件发布

### Auto Deploy

`sy-3-new/dev_utils/0711deploy.sh`

Pay attention to modify `QMAKE_PATH`, `QML_PATH` in script.


### QtCreator编译

Build a release version.

## QT项目发布环境搭建

### Qt依赖

官网Download或copy Qt环境

`libxcb-xinerama0`无法运行QtCreator, apt安装

`sudo apt install -y libxcb-xinerama0`

`g++`, `make`, `cmake`使Qt编译可用

### 发布过程依赖

#### 打包工具

linuxdeployqt patchelf appimagetool(additional option)

##### patchelf

sudo apt install patchelf

##### linuxdeployqt

build it from source code(use tag `continuous`).

modify main.cpp `host too new ,return 1`, remove it.

##### appimagetool(addtional option)

Download from github release page.

sudo cp dev_utils/resource/appimagetool-x86_64.AppImage /usr/local/bin/appimagetool

sudo chmod a+x /usr/local/bin/appimagetool

## Deprecated

### 移植后解决声音问题

`zkys_treat/dev_utils/pre_launch.sh`

发布后运行一次,替换gstreamer,以解决声音问题

解决：未安装patchelf工具，安装后未出现。

### 编译拼音输入法插件

QtInputMethod_GooglePinyin

打包时将生成的dict放到可执行文件同级目录,platforminputcontexts放入usr/lib中.

解决：
在main.cpp main函数中设置环境变量。

`qputenv("QT_IM_MODULE", QByteArray("qtvirtualkeyboard")); // QT 虚拟键盘组件`
`qputenv("QT_IM_MODULE", QByteArray("tgtsml")); // 自己编译的输入法插件`
`qputenv("QT_IM_MODULE", QByteArray("fcitx")); // 系统的fcitx输入法框架`

### 开机启动

terminal设置gnome-session-properties

add

name: App

Command: /home/deploy/Documents/appdir/SY-3-v-care-1.0.0.AppImage


### 打包过程依赖

> 仅Ubuntu18

sudo apt install libodbc; sudo apt install libpq5;

### 项目依赖

(QtQuick依赖)

`sudo apt install mesa-common-dev` (opengl环境,此包在ubuntu20上不同,为libgl-dev) (可能导致卡登录界面,重启解决)

修复找不到 -lGL

sudo ln -s /usr/lib/x86_64-linux-gnu/libGL.so.1 libGL.so

sudo apt install libzmq3-dev

### linuxdeployqt发布整理

TODO: add 输入法插件编译过程

echo "Categories=Development;" >> /home/deploy/Documents/build-qtDemo-Desktop_Qt_5_15_2_GCC_64bit-Debug/default.desktop 

