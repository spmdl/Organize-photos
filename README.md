# Organize-photos

* [詳細筆記](https://medium.com/@cbb104002/side-project-organize-photos-3491aef8e5ed?source=friends_link&sk=464906b2663c65a9d11f86ff77d1e259)

我整理照片步驟
1. 分類資料夾（Ex：場景、氛圍、主題...等），如果沒有拍很多就不用分
2. 過濾照片（用 jpg 預覽、把 raw 全部丟進 Lr）
3. 把不要的刪掉

上方步驟2, 3 往往都是手動的，因為懶所以有了這個 side project👍

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [執行環境](#執行環境)

## Background

classification.py：分類 JPG, RAW 

delimg.py：刪除多餘的檔案（比較 JPG, RAW 兩個資料夾，迭代比較多檔案的資料夾，若沒出現在比較少的資料夾裡就移到 Del 資料夾中）

default_path.txt：存放照片的目錄（Ex：/Users/angus/Desktop/攝影/圖債/未整理），這個目錄底下會有很多我拍攝完未整理的資料夾

file_extension.txt：紀錄上一次使用 classification.py 所分類的資料夾名稱（為了 delimg 比較 RAW, JPG哪個檔案比較多）

## Install

[python downloads](https://www.python.org/downloads/)

## Usage

### 第一步：手動 key 照片目錄的路徑到 default_path.txt 

開啟終端機 -> cd 到目錄底下 -> pwd -> 複製路徑 

```bash
$ cd Desktop/攝影/圖債/未整理
$ pwd
```

複製路徑 -> 開啟 default_path.txt -> 貼上剛剛複製的路徑

![alt tag](https://imgur.com/aaocYip.png)

### 第二步：classification.py

先 cd 到 Organize-photos 目錄底下 -> 執行 classification.py -> 選擇資料夾 -> 多個或單個 -> exit

```bash
$ python classification.py
>>> Input folder: 小王
多個輸入 2 單個輸入 1：1
>>> Input folder or exit: exit
```

![alt tag](https://imgur.com/TM9nra7.png)

多個的情況，假設今天拍小王拍很多套衣服或是場景：就適合輸入 2

![directory](https://imgur.com/vDVVaz1.png)

### 第三步：delimg.py

可以看一下 file_extension.txt 內容和要分類的資料夾是否相同（RAW 有沒有一樣），因為 delimg 是讀入 file_extension.txt 來比較兩個資料夾的檔案哪個多

執行 delimg.py -> 選擇資料夾 -> 多個或單個 -> exit

```bash
$ python delimg.py
>>> Input folder: 小王
多個輸入 2 單個輸入 1：1
>>> Input folder or exit: exit
```

![delimg.py](https://imgur.com/VbvVpmr.png)

## 執行環境

* Python 3.7.6
* macOS Mojave
