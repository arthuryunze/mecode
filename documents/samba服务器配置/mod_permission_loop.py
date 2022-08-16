import subprocess
import time

ruanjianzu = [
    ("hanyong", "韩勇"),
    ("huangjianxiong", "黄建雄"),
    ("yunze", "李云泽"),
    ("zhuyun", "朱雲"),
    ("daiyongzhu", "戴永柱"),
    ("tangpeng", "汤鹏"),
    ("caofengcai", "曹凤彩"),
    ("zhaopeng", "赵鹏"),
]
zhiliangzu = [
    ("pengyingbo", "彭映波"),
    ("limanfei", "李曼飞"),
    ("tangman", "汤曼"),
]

yingjianzu = [
    ("liyongliang", "李永亮"),
    ("wangning", "王宁"),
    ("douweifei", "豆为飞"),
    ("hanzhencai", "韩振才"),
]

shengchanzu = [
    ("liuzhongyuan", "刘忠元"),
    ("wangjinchun", "王金春"),
    ("shenjianzheng", "申建征"),
]

gongyingzu = [
    ("tianjiatian", "田家甜"),
]

d_bumens = [
    ["ruanjianzu", ruanjianzu, "软件组"],
    ["zhiliangzu", zhiliangzu, "质量组"],
    ["yingjianzu", yingjianzu, "硬件组"],
    ["shengchanzu", shengchanzu, "生产组"],
    ["gongyingzu", gongyingzu, "供应组"],
]
# 修改目录权限
def change_permission(group_users, group_name, group_path):
    groupdir = "./" + group_path
    subprocess.run(["sudo", "chown", "-R", group_name + "." + group_name, groupdir])
    subprocess.run(["sudo", "setfacl", "-R", "-b", groupdir])
    subprocess.run(["sudo", "setfacl", "-R", "-m", "g:" + group_name + ":rx", groupdir])
    # print("sudo", "chown", "-R", bumen_name + "." + bumen_name, groupdir)

    for user in group_users:
        user_path = "./" + group_path + "/" + user[1]
        subprocess.run(
            [
                "sudo",
                "chown",
                "-R",
                user[0] + "." + user[0],
                user_path,
            ]
        )
        # print("sudo", "chmod", "-R", "700", user_path)
        # print("sudo", "setfacl", "-R", "-b", user_path)
        # print("sudo", "setfacl", "-R", "-m", "u:" + user[0] + ":rwx", user_path)
        # print("sudo", "setfacl", "-R", "-m", "g:" + bumen_name + ":rx", user_path)
        subprocess.run(["sudo", "chmod", "-R", "700", user_path])
        subprocess.run(["sudo", "setfacl", "-R", "-b", user_path])
        subprocess.run(
            ["sudo", "setfacl", "-R", "-m", "u:" + user[0] + ":rwx", user_path]
        )
        subprocess.run(
            ["sudo", "setfacl", "-R", "-m", "g:" + group_name + ":rx", user_path]
        )


# set super admin
def set_super_user(username):
    # print("sudo", "setfacl", "-R", "-m", "u:" + username + ":rwx", "./*")
    subprocess.Popen(f"sudo setfacl -R -m u:{username}:rwx ./*", shell=True)


while True:

    # change user permission
    for bumen_name, bumen_user, bumen_path in d_bumens:
        # print("changing ", bumen_user, bumen_name, bumen_path)
        change_permission(bumen_user, bumen_name, bumen_path)

    set_super_user("zhaopeng")

    time.sleep(10)
