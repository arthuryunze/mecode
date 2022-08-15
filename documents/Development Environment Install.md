# Development Environment Install

## 系统环境

Ubuntu 18.04 LTS

关闭BIOS的安全启动（否则无法加载显卡）

## Python环境

Python 3.7 并搭建Python虚拟环境 使用venv或anaconda

修改.bashrc文件默认启动Python虚拟环境

pyqt5==5.12

pyqtwebengine==5.12

opencv-python==4.1.2.30

>  pymysql安装(暂时不用)

## PyTorch

NVIDIA显卡驱动：Ubuntu打开 Software and Updates -> Additional Drivers

CUDA version: 10.2(取决于pytorch，可以先看一下pytorch官网安装界面)

​	到官网下载runfile安装

PyTorch 1.7.1	

## labelme 编译安装
## d2 编译安装

## Azure Kinect SDK安装

open3d编译安装前需要安装**Azure Kinect相机SDK**

download ippic ERROR!
ippicv_2020_lnx_intel64_general_20191018_general.tgz 

smb://192.168.1.8/share/技术部/李云泽/doc/ippicv_2020_lnx_intel64_general_20191018_general.tgz

edit open3d_2021_04/3rdparty/ippicv/ippicv.cmake

set_local_or_remote_url(
    IPPICV_URL
    LOCAL_URL "${OPEN3D_THIRD_PARTY_DOWNLOAD_DIR}/${OPENCV_ICV_NAME}"
    REMOTE_URLS "/home/sy/Downloads/ippicv_2020_lnx_intel64_general_20191018_general.tgz"
    )



> 原因：[Azure Kinect with Open3D — Open3D latest (664eff5) documentation](http://www.open3d.org/docs/latest/tutorial/Basic/azure_kinect.html)

ubuntu18安装SDK直接看官方文档

[microsoft/Azure-Kinect-Sensor-SDK: A cross platform (Linux and Windows) user mode SDK to read data from your Azure Kinect device.](https://github.com/microsoft/Azure-Kinect-Sensor-SDK)

>  ubuntu20安装SDK参考《常用官方文档.md》

注意解除sudo权限限制

 > Linux Device Setup

> On Linux, once attached, the device should automatically enumerate and load all drivers. However, in order to use the Azure Kinect SDK with the device and without being 'root', you will need to setup udev rules. We have these rules checked into this repo under 'scripts/99-k4a.rules'. To do so:

> - Copy 'scripts/99-k4a.rules' into '/etc/udev/rules.d/'.
> - Detach and reattach Azure Kinect devices if attached during this process.

> Once complete, the Azure Kinect camera is available without being 'root'.

## Open3D安装

之后GitLab 获取源码编译安装Open3D

打开梯子

export http_proxy="127.0.0.1:8889";export https_proxy="127.0.0.1:8889"（具体端口号查看梯子设置）

git clone --recursive git@192.168.1.8:vision/open3d_2021_04.git

Open3d编译安装 参考官方文档

需要 cmake 3.18  官网下载二进制包

[Build from source — Open3D 0.13.0 documentation](http://www.open3d.org/docs/release/compilation.html)

> 可能出现的错误  
> Could NOT find Vulkan (missing: VULKAN_LIBRARY VULKAN_INCLUDE_DIR) 
> -- Using X11 for window creation
> -- Found X11: /usr/include   
> CMake Error at 3rdparty/GLFW/CMakeLists.txt:236 (message):
> The RandR headers were not found

> 解决办法：
> sudo apt-get install xorg-dev  
> sudo apt-get install libc++-7-dev  
> sudo apt-get install libc++abi-7-dev  

最后一步选择make install-pip-package安装为python包形式

> ## Pypat音频播放(已弃用)

>[tnewman/pat: PAT Audio Technician](https://github.com/tnewman/pat#Prerequisites)

>sudo apt install build-essential cmake libavutil-dev libswresample-dev libavdevice-dev libavcodec-dev libavformat-dev libswscale-dev libsdl2-dev ninja-build



>pip install pypat

