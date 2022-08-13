### linuxdeployqt编译安装过程记录

下载源码

修改源码 main.cpp

host too new部分 返回值修改为return 0;

cd linuxdeployqt

qmake

make

export LD_LIBRARY_PATH=~/Qt/5.15.2/gcc_64/lib

此时linuxdeployqt可用

网页下载patchelf

https://nixos.org/releases/patchelf/patchelf-0.9/patchelf-0.9.tar.bz2


```shell
wget https://nixos.org/releases/patchelf/patchelf-0.9/patchelf-0.9.tar.bz2
tar xf patchelf-0.9.tar.bz2
( cd patchelf-0.9/ && ./configure  && make && sudo make install )

```

/home/deploy/linuxdeployqt/bin/linuxdeployqt qtDemo -qmldir=/home/deploy/Qt/5.15.2/gcc_64/qml -qmake=/home/deploy/Qt/5.15.2/gcc_64/bin/qmake -appimage

注意qmldir,qmake参数使用绝对路径



error :

libodbc.so.2 => not found

sudo apt install libodbc1



"libpq.so.5 => not found"

sudo apt install libpq5



appimagetool: not found

sudo wget -c "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage" -O /usr/local/bin/appimagetool
sudo chmod a+x /usr/local/bin/appimagetool



fatal: Needed a single revision
Failed to run 'git rev-parse --short HEAD: Child process exited with code 128 (code 128)
Desktop file: /home/deploy/Documents/build-qtDemo-Desktop_Qt_5_15_2_GCC_64bit-Debug/default.desktop

vi /home/deploy/Documents/build-qtDemo-Desktop_Qt_5_15_2_GCC_64bit-Debug/default.desktop 

添加一行

```shell
Categories=Development;
```





---

总结写入zksy_treat/dev_utils/README.md