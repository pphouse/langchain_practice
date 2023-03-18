import re
import os


with open("./log.txt", "r") as f:
    lines = f.read()

print(lines)
#'''で囲まれた部分（コードブロック）を抽出する関数
# lines = re.search(r"```(.+)```", lines).group(1)
end = []
cnt = 0
for i, c in enumerate(lines):
    if c == "`":
        cnt += 1
        if cnt == 3:  # `が３回連続したら順番を記録する
            if lines[i + 1 : i + 7] == "python":  # 先頭のpythonは除外する
                end.append(i + 7)
            else:
                end.append(i)
    else:
        cnt = 0

code = lines[end[0] + 1 : end[1] - 2]

# pythonコードをテキストファイルに書き込む
with open("./modified.txt", "w") as f:
    f.write(code)
    # print(code)

# log.txtをsub_main.pyに変更
os.rename("./modified.txt", "./sub_main.py")
