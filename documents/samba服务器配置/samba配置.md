# 需求

管理员 全可读可写
用户 自己目录可读可写 其它目录可读

---



# samba配置备忘

## 创建用户名及密码

1.创建系统用户及密码

[root@localhost ~]# useradd test1
[root@localhost ~]# passwd test1
更改用户 test1 的密码 。
新的 密码：
无效的密码： WAY 过短
无效的密码： 是回文
重新输入新的 密码：

passwd： 所有的身份验证令牌已经成功更新。

  如果不创建系统用户会出现如下错误：

 [root@localhost ~]# smbpasswd -a test1
New SMB password:
Retype new SMB password:
Failed to add entry for user test1.

2.创建smb用户及密码

[root@localhost ~]# smbpasswd -a test1
New SMB password:
Retype new SMB password:

Added user test1.


## 重启samba服务
/etc/init.d/samba restart 





## 设置权限

普通权限

```
# 创建用户
sudo useradd yunze
sudo passwd sy123456
sudo smbpasswd -a yunze

# 创建共享文件夹
sudo mkdir /opt/samba/share/技术部/李云泽
# 设置权限
sudo chown -R yunze:yunze 李云泽
sudo chmod -R 755 李云泽

```

管理员权限



管理员创建普通用户文件夹脚本:

```
# 创建用户
sudo useradd -g smbuser yunze
sudo usermod -a -G groupA yunze
sudo smbpasswd -a yunze

# 创建共享文件夹
sudo mkdir /opt/samba/share/技术部/李云泽
# 设置权限
sudo chown -R yunze:smbadmin /opt/samba/share/技术部/李云泽
sudo chmod -R 775 /opt/samba/share/技术部/李云泽

```





修改smb密码

sudo smbpasswd yunze



组内删除成员

vim /etc/group





## 可用脚本

技术部/add_user.sh

增加用户或修改用户权限