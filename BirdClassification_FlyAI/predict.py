# -*- coding: utf-8 -*
'''
实现模型的调用
'''
from flyai.dataset import Dataset

from model import Model

data = Dataset()
model = Model(data)
p = model.predict(image_path='images/091.Mockingbird/Mockingbird_0087_79600.jpg')
print(p)
