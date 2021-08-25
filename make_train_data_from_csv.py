import csv
import glob
import os

from config import Config

#ファイルのあるディレクトリパスを入力
dirPath = Config.csv_file_path

#保存先のファイルパス
saveFilePath = Config.train_data_path

#ファイル一覧を取得
files = glob.glob(dirPath + os.sep + "*.csv")

with open(saveFilePath, "a", encoding="utf-8") as save_file:
    for file in files:
        #デバッグ用
        print(os.path.basename(file) + " is open.")

        #ファイルオープン
        with open(file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for read in reader:
                text_complex = [read[6] + "\n", read[7] + "\n", "\n"]
                save_file.writelines(text_complex)
