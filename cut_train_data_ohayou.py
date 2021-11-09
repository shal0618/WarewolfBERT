import os
import re

from config import Config

#変更元のファイルパス
trainFilePath = Config.train_data_path

#保存先のファイル名(拡張子無し)
saveFileName = os.path.splitext(os.path.basename(trainFilePath))[0]
# print(saveFileName)

#保存先のファイルパス
saveFilePath = Config.data_dir + os.sep + saveFileName + "2.txt"
print(saveFilePath)

#おはよ***が出た回数
ohayoCounter = 0
#おはよ***の最大数
ohayoMax = 5000

#0:質問
#1:解答
#2:改行
questionFlag = -1

# debugCounter = 0

array = []
with open(trainFilePath, "r", encoding="utf-8") as train_file:
    for line in train_file:
        questionFlag += 1
        if questionFlag == 0:
            item = []

        item.append(line)
        
        if questionFlag == 2:
            array.append(item)
            questionFlag = -1

        # debugCounter += 1
        # if debugCounter > 120:
        #     break

# print(array)


with open(saveFilePath, "w", encoding="utf-8") as save_file:
    for item in array:
        if "おはよ" in item[1]:
            if ohayoCounter > ohayoMax:
                continue
            ohayoCounter += 1
        save_file.writelines(item)