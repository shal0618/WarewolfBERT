import csv
import glob
import os

from config import Config


#ファイルのあるディレクトリパスを入力
dirPath = Config.save_file_path

#保存先のファイルパス
saveFilePath = Config.csv_file_path

#ファイル一覧を取得
files = glob.glob(dirPath + os.sep + "*.csv")
print(files)

with open(saveFilePath, "a", encoding="utf-8") as save_file:
    for file in files:
        #デバッグ用
        print(os.path.basename(file) + " is open.")

        #ファイルオープン
        with open(file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            first_read_flag = True
            for read in reader:
                if not first_read_flag:
                    if "\n" in read[6]:
                        read[6] = read[6].replace("\n","")
                    if "\n" in read[7]:
                        read[7] = read[7].replace("\n","")
                    if read[7] == "無し":
                        continue
                    text_complex = [read[6] + "\n", read[7] + "\n", "\n"]
                    save_file.writelines(text_complex)
                else:
                    first_read_flag = False

