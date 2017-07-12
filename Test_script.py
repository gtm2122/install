from torchvision import datasets,models,transforms
import torch.nn as nn
from nndev import model_pip
import os

Model_name="ResNetModel_Pretrained.pth.tar"
datapath="./datasets/"
savepath="./ResNetModel.pth.tar"
res = models.resnet18(pretrained=True)
num_label = 0
for i in os.listdir("./datasets/test/"):
    if len(i) > 9 and ".DS_Store" not in i:
        num_label+=1
res.fc = nn.Linear(res.fc.in_features,num_label)
obj = model_pip(model_in=res,scale=True,batch_size=5,use_gpu=False,gpu=3,data_path=datapath,verbose=True)
model = obj.load_model(savepath)
#mdir="./"
#obj.test

obj.test(model_dir = './',model_name = Model_name,random_crop = False,test_on=True,save_miscl = True)

del (obj)
