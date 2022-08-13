# Software Production Environment Install

Document Number: O-0001
Document Type: Ops
Document Author: Yunze
Last Updated: 2022/07/14

|Version|Date|Author|Description of Changes|
|---|---|---|---|
|0.1|2022/07/14|Yuzne|Initial Documents|

## Introduction

### Purpose	

Introduce install Production Environment.

###Scope

Only for Production Environment. However, this document does not apply to development environment.


## Make startup disk

use rufus, ventoy or ubuntu startup disk creator make a startup disk.

## Install Ubuntu 18.04

check minimal install and third drivers when installing system.

## Config system

- change soft update source to China source.

- install cmake

	`sudo snap install cmake`

## Install NVIDIA driver 

### driver install
install nvidia driver 470, use GUI `Software & update` or `sudo ubuntu-drivers install`.

### cuda cudnn install

- cuda

	https://developer.nvidia.com/cuda-10.2-download-archive

- cudnn

	dpkg install file `cudnn-local-repo-ubuntu1804-8.4.1.50_1.0-1_amd64` download, or go to nvidia cudnn homepage download it(need account tolog in).

then,

```
sudo cp /var/cudnn-local-repo-ubuntu1804-8.4.1.50/cudnn-local-B2E73D77-keyring.gpg /usr/share/keyrings/

sudo apt update && sudo apt install libcudnn8-dev
```

set cuda path in .bashrc file.

`echo 'export PATH=/usr/local/cuda/bin:$PATH' >> .bashrc`

## Install camera driver(Realsense SDK)

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE

sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u

sudo apt-get install librealsense2-dkms librealsense2-utils
```

## Install identification module(Torch Torchvision)

use file or go to pytorch homepage download.

`/media/sy/new/data/libtorch-cxx11-abi-shared-with-deps-1.12.0+cu102.zip`
`/media/sy/new/data/vision-0.13.0.tar.gz`

`libtorch-cxx11-abi-shared-with-deps-1.12.0+cu102.zip` `vision-0.13.0.tar.gz`

pay attention to version **strictly correspondence**(list on vision github homepage readme).

`sudo apt install libjpeg-dev`

- For turing architecture GPU.
`cmake .. -DCMAKE_PREFIX_PATH=${your_libtorch_path} -DWITH_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=75`

ignore warning, then

`make && sudo make install`

## Install SY-3 GUI clinet

copy packaged appdir

Create a start.sh for start with system.

`echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH\n cd ${/path/to/Appdir/usr/bin};\n./qtDemo\n' > ~/start.sh`

`chmod 777 ~/start.sh`

then,

add this script in Ubuntu GUI software `Startup Applications Preferences`.

## Install other tools.

Install todesk, ssh.
