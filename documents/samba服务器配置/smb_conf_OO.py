import subprocess
import sqlite3


# create table
# cur.execute(
#     """CREATE TABLE stuff
# (NAME TEXT NOT NULL,
# ENNAME TEXT NOT NULL,
# GROUP_NAME TEXT NOT NULL,
# GROUP_PATH TEXT NOT NULL);"""
# )
# conn.commit()


# insert all
# for gname, gusers, gpath in d_bumens:
#     for enname, name in gusers:
#         tmp = Stuff(name, enname, gpath + "/" + name, gname, gpath)
#         s.insert_stuff(tmp)


samba_dirpath = "/opt/samba/share/研发中心"


class Stuff:
    empCount = 0

    def __init__(self, name, enname, path, group_name, group_path) -> None:
        self.name = name
        self.enname = enname
        self.path = path
        self.group_name = group_name
        self.group_path = group_path
        Stuff.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Stuff.empCount)

    def display_stuff(self):
        print(
            "Name:",
            self.name,
            "Enname:",
            self.enname,
            "Group:",
            self.group_path,
        )


class Sqlite:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("user.db")
        self.cur = self.conn.cursor()

    def insert(self, stuff):
        self.cur.execute(
            f"INSERT INTO stuff (NAME,ENNAME,GROUP_NAME,GROUP_PATH) VALUES ('{stuff.name}','{stuff.enname}','{stuff.group_name}','{stuff.group_path}')"
        )
        self.write_database()

    def find_by_name(self, name):
        self.cur.execute(f"SELECT * from stuff where name='{name}';")
        return self.cur.fetchall()

    def find_all(self):
        self.cur.execute(f"SELECT * from stuff;")
        return self.cur.fetchall()

    def write_database(self):
        self.conn.commit()


class StaffDAO:
    def __init__(self) -> None:
        self.db = Sqlite()

    def insert_stuff(self, stuff: Stuff):
        self.db.insert(stuff)

    def orm(self, db_data) -> Stuff:
        s = Stuff(
            db_data[0],
            db_data[1],
            db_data[3] + "/" + db_data[1],
            db_data[2],
            db_data[3],
        )
        return s

    def find_by_name(self, name):
        print("Try to find: ", name)
        rst_list = []
        for user in self.db.find_by_name(name):
            astuff = self.orm(user)
            rst_list.append(astuff)
            print("Found: ")
            astuff.display_stuff()

        return rst_list

    def find_all(self):
        rst_list = []
        for user in self.db.find_all():
            astuff = self.orm(user)
            rst_list.append(astuff)
            print("Found: ")
            astuff.display_stuff()

        return rst_list

    def get_groups_pathname(self):
        rst_list = []
        all_users = self.db.find_all()
        for _, _, _, gpath in all_users:
            rst_list.append(gpath)
        return list(set(rst_list))

    def get_groups_name(self):
        rst_list = []
        all_users = self.db.find_all()
        for _, _, gname, _ in all_users:
            rst_list.append(gname)
        return list(set(rst_list))

    def get_groups_couples(self):
        rst_list = []
        all_users = self.db.find_all()
        for _, _, gname, gpath in all_users:
            if [gname, gpath] not in rst_list:
                rst_list.append([gname, gpath])
        return rst_list


class Business:
    def __init__(self) -> None:
        """do some about shell"""
        self.dao = StaffDAO()

    def get_users(self):
        user_list = []
        p = subprocess.Popen("sudo pdbedit -L", stdout=subprocess.PIPE, shell=True)
        bytes_rst = p.stdout.readlines()
        for bytes_user in bytes_rst:
            user = bytes_user.decode()
            username = user.split(":")[0]
            user_list.append(username)
            print(username)

        return user_list

    def sync_sys_from_db(self):
        return True

    def change_group_permission(self):
        for gname, gpath in self.dao.get_groups_couples():
            groupdir = samba_dirpath + "/" + gpath
            subprocess.run(["sudo", "setfacl", "-R", "-b", groupdir])
            subprocess.run(["sudo", "chown", "-R", gname + "." + gname, groupdir])
            subprocess.run(
                ["sudo", "setfacl", "-R", "-m", "g:" + gname + ":rx", groupdir]
            )

    def change_user_permission(self):
        for name, enname, upath, gname, gpath in self.dao.find_all():
            user_path = samba_dirpath + "/" + upath
            subprocess.run(
                [
                    "sudo",
                    "chown",
                    "-R",
                    enname + "." + enname,
                    user_path,
                ]
            )
            subprocess.run(["sudo", "chmod", "-R", "700", user_path])
            subprocess.run(["sudo", "setfacl", "-R", "-b", user_path])
            subprocess.run(
                ["sudo", "setfacl", "-R", "-m", "u:" + enname + ":rwx", user_path]
            )
            subprocess.run(
                ["sudo", "setfacl", "-R", "-m", "g:" + gname + ":rx", user_path]
            )


# s = StaffDAO()
# # s.get_user_by_name("yunze")
# s.find_by_name("赵鹏")

b = Business()
b.change_group_permission()
