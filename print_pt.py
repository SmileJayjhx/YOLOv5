import torch

    # Load category and color encodings
cat_dict = torch.load('/home/smile/YOLOv5/YOLOv5/yolov5s.pt')
for k, v in cat_dict.items():  # k 参数名 v 对应参数值
  print(k, v)

import torch

# 假设你的模型文件名为 'model.pt'
model = torch.load('yolov5s.pt')

# 获取类别名称
names = model.module.names if hasattr(model, 'module') else model.names

# 打印类别名称
print(names)
