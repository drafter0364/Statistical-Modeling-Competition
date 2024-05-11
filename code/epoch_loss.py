import re
import matplotlib.pyplot as plt
import os

# 定义正则表达式模式
pattern = r'Epoch\s+(\d+)	Loss:(\d+\.\d+)'
path = "./主题分析结果"
files = os.listdir(path)
for xmlFile in files: 
    file_path = path + "/" + xmlFile
    with open(file_path, 'r', encoding='utf-8') as file:
        epochs = []
        losses = []
        for line in file:
            match = re.search(pattern, line)
            if match:
                epoch = int(match.group(1))
                loss = float(match.group(2))
                print(epoch)
                print(loss)
                epochs.append(epoch)
                losses.append(loss)

    # 绘制折线图
    plt.plot(epochs, losses, marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss vs Epoch')
    plt.grid(True)
    portion = os.path.splitext(xmlFile)
    plt.savefig("./训练损失图/" + portion[0] + ".png")
    plt.clf()
