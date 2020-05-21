import shutil
import os

from os.path import exists, isdir, join

#刪除多餘的 raw 檔
def delfile(path, file_extension):

    try:
        # 找出資料較多的資料夾
        if len(os.listdir(path + "/" + file_extension[0])) > len(os.listdir(path + "/" + file_extension[1])):
            path_m = path + "/" + file_extension[0]
            file_m = os.listdir(path_m)
            path_s = path + "/" + file_extension[1]
            file_s = os.listdir(path_s)
        else:
            path_m = path + "/" + file_extension[1]
            file_m = os.listdir(path_m)
            path_s = path + "/" + file_extension[0]
            file_s = os.listdir(path_s)

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
        print("not ok={}".format(f))

    # 新增 Del 資料夾
    if not os.path.isdir(path + "/Del"):
        os.mkdir(path + "/Del")

    for files in file_m:
        if files not in '.DS_Store':

            source = files.rsplit(".", 1)  # 分割字串
            file_name = source[0]

            if file_name+".JPG" not in file_s:

                try:
                    file_path = path + "/Del"
                    shutil.copy("{}/{}".format(path_m, files), file_path)
                    os.remove("{}/{}".format(path_m, files))
                    print("remove : {}".format(file_name))

                except Exception as e:
                    print(str(e))
                    print("not ok={}".format(f))

# 獲取默認路徑
with open('default_path.txt') as d_p:
    lines = d_p.readlines()
default_path = lines[0] + "/"

# 獲取副檔名
with open('file_extension.txt') as f_e:
    file_extension = f_e.read().splitlines()

ch_path = input(">>> Input folder: ")
while ch_path != "exit":

    path = default_path + ch_path

    if exists(path):
        file = input("多個輸入 2 單個輸入 1：")
        if (file == "1"):

            delfile(path, file_extension)

        elif (file == "2"):
            files = os.listdir(path)
            for f in files:

                fullpath = join(path, f)

                if isdir(fullpath) and f not in '.DS_Store' and f!= 'Del':
                    print("目錄：", f)
                    delfile(fullpath, file_extension)

        ch_path = input(">>> Input folder or exit: ")
    else:
        if not exists(default_path):
            print("default_path is incorrect")
            ch_path = "exit"
        else:
            print("folder is incorrect")
            ch_path = input(">>> Input folder: ")