# Title

Document Number: O-0001  
Document Type: Ops  
Document Author: Yunze  
Last Updated: 2022/07/14  

|Version|Date|Author|Description of Changes|
|---|---|---|---|
|0.1|2022/07/14|Yuzne|Initial Documents|


## Introduction

### Purpose

Intorduce install Production Environment.

### Scope

Only for Production Environment. However, this document does not apply to development environment.



## Do something

use rufus,ventoy or ubuntu startup disk creator make a startup disk.

- change soft update source to China source.

- install cmake

	`sudo snap install cmake`


```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE

sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u

sudo apt-get install librealsense2-dkms librealsense2-utils
```

pay attention to version **strictly correspondence**(list on vision github homepage readme).

