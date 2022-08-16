import subprocess
import sqlite3

ruanjianzu = [
    ("hanyong", "韩勇"),
    ("huangjianxiong", "黄建雄"),
    ("yunze", "李云泽"),
    ("zhuyun", "朱雲"),
    ("daiyongzhu", "戴永柱"),
    ("tangpeng", "汤鹏"),
    ("caofengcai", "曹凤彩"),
]
zhiliangbu = [
    ("pengyingbo", "彭映波"),
    ("limanfei", "李曼飞"),
    ("tangman", "汤曼"),
]

yingjianbu = [
    ("liyongliang", "李永亮"),
    ("wangning", "王宁"),
    ("douweifei", "豆为飞"),
    ("hanzhencai", "韩振才"),
]

shengchanbu = [
    ("liuzhongyuan", "刘忠元"),
    ("wangjinchun", "王金春"),
    ("shenjianzheng", "申建征"),
]

gongyingbu = [
    ("tianjiatian", "田家甜"),
]


def del_user(bumen):
    """del user"""
    for user in bumen:
        subprocess.run(["sudo", "userdel", user[0]])
        subprocess.run(["sudo", "pdbedit", "-x", "-u", user[0]])


def add_group(group_name):
    subprocess.run(
        [
            "sudo",
            "useradd",
            "-d",
            "/opt/samba/share",
            "-s",
            "/sbin/nologin",
            group_name,
        ]
    )


def add_user(bumen, bumen_name):
    """add user"""
    for user in bumen:
        subprocess.run(
            [
                "sudo",
                "useradd",
                "-d",
                "/opt/samba/share",
                "-s",
                "/sbin/nologin",
                user[0],
            ]
        )
        subprocess.run(["sudo", "pdbedit", "-a", "-u", user[0], "-P"])
        subprocess.run(["sudo", "gpasswd", "-a", user[0], bumen_name])


def change_permission(bumen, bumen_name, path_name):
    for user in bumen:
        user_path = "./" + path_name + "/" + user[1]
        subprocess.run(
            [
                "sudo",
                "chown",
                "-R",
                user[0] + "." + user[0],
                user_path,
            ]
        )
        subprocess.run(["sudo", "chmod", "-R", "700", user_path])
        subprocess.run(
            ["sudo", "setfacl", "-R", "-m", "u:" + user[0] + ":rwx", user_path]
        )
        subprocess.run(
            ["sudo", "setfacl", "-R", "-m", "g:" + bumen_name + ":rx", user_path]
        )


d_bumens = [
    ["ruanjianzu", ruanjianzu, "软件组"],
    ["zhiliangbu", zhiliangbu, "质量部"],
    ["yingjianbu", yingjianbu, "硬件组"],
    ["shengchanbu", shengchanbu, "生产部"],
    ["gongyingbu", gongyingbu, "供应部"],
]

# for g in bumens:
#     add_group(g)


# change dir permission
# for bumen_name, bumen_user, bumen_path in d_bumens:
#     subprocess.run(["sudo", "chown", "-R", "zhaopeng.zhaopeng", "./" + bumen_path])
#     subprocess.run(["sudo", "chmod", "-R", "700", "./" + bumen_path])
#     subprocess.run(
#         ["sudo", "setfacl", "-R", "-m", "g:" + bumen_name + ":rx", "./" + bumen_path]
#     )

# change user
# for bumen_name, bumen_user, bumen_path in d_bumens:
#     #     # print(name, path)
#     # add_user(bumen, name)
#     change_permission(bumen_user, bumen_name, bumen_path)

# change all user password
# for bumen_name, bumen_user, bumen_path in d_bumens:
#     for user_name, user_path in bumen_user:
#         ps = subprocess.Popen(
#             ("printf", "sy123456\nsy123456\n"), stdout=subprocess.PIPE
#         )
#         output = subprocess.check_output(
#             ("sudo", "smbpasswd", "-s", user_name), stdin=ps.stdout
#         )
#         ps.wait()

# super user ! testing
def set_super_user(username):
    print("sudo", "setfacl", "-R", "-m", "u:" + username + ":rwx", "./*")
    subprocess.run(["sudo", "setfacl", "-R", "-m", "u:" + username + ":rwx", "./*"])


# add_group("ruanjianzu")
# for name, path in ruanjianzu:
#     subprocess.run(["sudo", "gpasswd", "-a", name, "ruanjianzu"])

# set_super_user("zhaopeng")

conn = sqlite3.connect("user.db")
cur = conn.cursor()
for zu, zuname, zupath in d_bumens:
    cur.execute(f"CREATE TABLE IF NOT EXISTS {zu} (Name TEXT, Enname TEXT)")
    for enname, name in zuname:
        cur.execute(f"INSERT INTO {zu} (Name,Enname) VALUES ('{name}','{enname}')")


# cur.execute("CREATE TABLE IF NOT EXISTS ruanjianzu (Name TEXT, Enname TEXT)")
# cur.execute("INSERT INTO ruanjianzu (Name,Enname) VALUES ('李云泽','yunze')")

conn.commit()
print("insert success.")
conn.close()
