# 尚易SY-3 UI Release Letter ---V1.0.0



**文件地址(File Location)：**  smb://172.16.20.8/share/技术部/王良/AppImage/SY-3-UI-v1.0.0.AppImage

**md5sum:**   a95a5184c3b64706fc7d4bbe9f357b3b

**sha256sum:**  f1b31bd30d0a1a449dd4c4fb83d2466fdc4c917ca5852422995de6d7a029acf9

**Run OS Env:** Ubuntu 18.04.6



**Code address:**  https://gitee.com/mathwater/zkys_treat.git

**Branch:**   v1.0.0

**Commit Tags:**  commit 1f70a86ebbcf0893f59edc79f1fe0d9e4240894e 



### **Release Features:**

- 键盘（硬件）中文输入法
- Formal Build and Packge Process first time（第一次固定平台Ubuntu18.04正常的打包）
- 添加振动频率控制

- 其它Detail 详见下表

| 序号                             | 问题描述                                                     | 简答                                                         | 备注                                                         |
| -------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <font color=green >3</font>      | 设备管理 界面![3](./pics/setManger.png)                      | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >4</font>      | 为什么 qt creator老报这个错，可运行，注释掉还不行![4](./pics/qml_module_not_found.png) | <font color=green > **-已解决--** </font>                    | -QML_IMPORT_PATH +=$$PWD/TaoQuick/imports/TaoQuick---        |
| <font color=green >5</font>      | 设备管理 界面![3](./pics/setManger.png)                      | **<font color=green > -已解决-- </font>**                    | ----                                                         |
| <font color=green >6</font>      | 登录界面未全屏 1080P ![4](./pics/1080.png)                   | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >7</font>      | CusButton是一种什么类型 ![5](./pics/CusButton.png)           | <font color=green > **-已解决--** </font>                    | 第三方控件，没有绑定Tab键功能                                |
| <font color=green >8</font>      | <font color=green >查找无法输入中文，其它一输入就成加密形式</font>![6](./pics/search.png) | ----<font color=green > **-已解决--** </font>                | 随着中文输入法的解决，已经解决                               |
| <font color=green >9</font>      | 切换有问题 ![8](./pics/switchissue.png)                      | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >10</font>     | -相机label有错位？-![9](./pics/camera.png)                   | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >12</font>     | -重复import, import 库后面加空格再带版本是qml特有语法吗？-![11](./pics/duplicateImport.png)-- | <font color=green > **-自行已解决--** </font>                | ----                                                         |
| <font color=green >13</font>     | 点退出系统，弹不出登录框![12](./pics/exit.png)----           | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >15</font>     | -外部杂音code还在？-![13](./pics/nosiecode.png)--            | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color="green">18</font>    | -医生图标与字体不在同一水平线，可微调-![16](./pics/doctor.png)-- | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color = green > 19</font>  | -<font color = green >输入框无法输入中文字符-</font>![17](./pics/input.png)-- | -<font color=green > **-已解决--** </font>---                | ----                                                         |
| <font color=green >20</font>     | -参数设置页面没有填满背景-![18](./pics/args.png)--           | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >22</font>     | -处方管理？背景无填满-![20](./pics/chufang.png)--            | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >23</font>     | -处方返回按钮无点无反应（其它条件不满足，应该不影响此按扭逻辑功能）-![21](./pics/chufangBack.png)-- | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color=green >24</font>     | -WebAssembly有什么作用？ 如何配置~-![21](./pics/WebAssembly.png)-- | <font color=green > **-none fix--** </font>                  | ----                                                         |
| <font color=green >25</font>     | -登录按钮悬停效果没改-                                       | ![1](./pics/login.png)----                                   | <font color=green > **-已解决--** </font>                    |
| <font color=green >26</font>     | -按回车键（登录图标区键盘）不自动登录--                      | --![1](./pics/login.png)---                                  | <font color=green > **-已解决--** </font>                    |
| <font color = green > 28</font>  | 开处方下所有的悬停按钮均未生效                               | <font color=green > **-已解决--** </font>                    | ----                                                         |
| <font color = green>29</font>    | 文字没对齐                                                   | -![1](./pics/buqi.png)----                                   | <font color=green > **-已解决--** </font>                    |
| <font color=green > 30 </font>   | --双击生效改为单击--                                         | ![2](./pics/doubleclick.png) ----                            | <font color=green > **-已解决--** </font>                    |
| <font color=green >32</font>     | 开处方界面背景（透明）处按钮还可又点击，应该禁止             | -![3](./pics/treat.png) -                                    | <font color=green > **-已解决--** </font>                    |
| <font color=green > 33 </font>   | <font color = green>肾经（脾经等，点击一下添加两条的），删除时点一个也应全部删除。</font> | ![2](./pics/doubleclick.png) --------                        | <font color=green > **-已解决--** </font>                    |
| <font color=green > 34 </font>   | 退出按钮未生效                                               | ![2](./pics/exitissue.png)                                   | <font color=green > **-已解决--** </font>                    |
| <font color=green > 35 </font>   | 1. 选中的背景都标红，<br />2. 经络计划列表前加数字顺序标记（按设计的来） | ![2](./pics/add_number.png)                                  | ----                                                         |
| <font color=green > 37 </font>   | 动画演示界面不能伸缩填满全屏（有黑边）                       | ![](./pics/display.png)                                      | <font color=green > **居中，改背景为白色 已解决**</font>     |
| <font color=green > 38 </font>   | CusButton 下延不明显，是否可以整体上移一定间距<font color=red> | ![](./pics/buttonTab.png)                                    | <font color=green > **-已解决--** </font>                    |
| <font color=green > 39 </font>   | github repo 其它人的本地commit无法push（协同开发受阻）       | <font color=green > gitee 方案解决，github still not work </font> | 建立公共三人都可以commit的repo,今天尝试了一下，任然未成功    |
| <font color=green >41 </font>    | 登录框输入用户名后，敲回车键进入白屏（不用鼠标点击）         | ![](./pics/whitescreen.png)<br>![](./pics/whiteScreen.png)   | <font color=green > **-已解决--** </font>                    |
| <font color=green >42 </font>    | <font color=green>TableView 字体显示不全（超出宽度时）</font> | ![](./pics/displayofshen.png)                                | <font color=green > **-已解决--** </font>                    |
| <font color = green>43</font>    | <font color = green>选择过的经络都应标为彩色</font>          | ![](./pics/selected.png)                                     | <font color=green > **-已解决--** </font>                    |
| <font color = green>45</font>    | <font color=green>声音、音量大小滑动控制</font>              | ![](./pics/voice.png)                                        | <font color=green > **-已解决--** </font>                    |
| <font color=green>50</font>      | <font color =green >开处方选择经络：肾经-体后的背景色与体前的一样</font> |                                                              | <font color=green > **-已解决--** </font>                    |
| <font color=green>51</font>      | <font color=green>键盘输入法切换问题</font>                  |                                                              |                                                              |
| <font color=green>54</font>      | 姿势模式排序不对                                             | ![](./pics/sortissue.png)                                    | <font color=green > **-已解决，不是问题--** </font>          |





Authors:  Wang Liang , Yun ze

Date:  2021年 12月 02日 星期四 10:34:00 CST
