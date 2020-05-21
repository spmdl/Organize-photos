import shutil
import os

from os.path import isdir, join, exists

# 分類JPG, NEF
def classification(path, pwd):

    os.chdir(path)
    files = os.listdir(path)
    ext_list = []

    for f in files:
        try:
            source = f.rsplit(".", 1)
            file_name = source[0]
            file_ext = source[1]

            folder_path = "{}/{}".format(path, file_ext)

            if file_ext  not in ext_list and f not in '.DS_Store': ext_list.append(file_ext)

            if not exists(folder_path):
                print("目錄：{}".format(file_ext))
                os.makedirs(folder_path)

            shutil.copy(f, folder_path)
            os.remove("{}/{}".format(path, f))
            # shutil.move("{}/{}".format(path,f), folder_path)

        except Exception as e:
            print(str(e))
            print("not ok={}".format(f))

    # 寫入副檔名
    os.chdir(pwd)
    with open('file_extension.txt', 'w') as file_ext:
        for ext in ext_list:
            file_ext.write(ext + '\n')

# 獲取默認路徑
with open('default_path.txt') as f:
    lines = f.readlines()
default_path = lines[0] + "/"

# 取得當前工作目錄
pwd_path = os.getcwd()

ch_path = input(">>> Input folder: ")
while ch_path != "exit":

    path = default_path + ch_path
    if exists(path):

        file = input("多個輸入 2 單個輸入 1：")
        if (file=="2"):

            files = os.listdir(path)
            for f in files:
              # 產生檔案的絕對路徑
                fullpath = join(path, f)

                if isdir(fullpath) and f not in '.DS_Store' and f != 'NEF' and f != 'JPG' and f!= 'Del':
                    print("目錄：", f)
                    classification(fullpath, pwd_path)

                    if isdir(fullpath + "/DS_Store"):
                        shutil.rmtree(fullpath + "/DS_Store")
                    elif isdir(path + "/.DS_Store"):
                        shutil.rmtree(path + "/DS_Store")

        elif(file=="1"):

            classification(path, pwd_path)

            if isdir(path + "/DS_Store"):
                shutil.rmtree(path + "/DS_Store")
            elif isdir(path + "/.DS_Store"):
                shutil.rmtree(path + "/DS_Store")

        ch_path = input(">>> Input folder or exit: ")

    else:
        if not exists(default_path):
            print("default_path is incorrect")
            ch_path = "exit"
        else:
            print("folder is incorrect")
            ch_path = input(">>> Input folder: ")