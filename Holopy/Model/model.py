import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import numpy as np
import subprocess as sp
import time
import random
import matplotlib.pyplot as plt

# Dataset structure:
# testing_or_training/
# - 0/ <-type
# --- 1.png <-example 
# --- 2.png
# --- ...
# - 1/
# --- 1.png
# --- 2.png
# --- ...
# - ...

class Holonet(nn.Module):
	def __init__(self):
		super(Holonet, self).__init__()
		self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=7,padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
		self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=5),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2))
		self.layer3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=2),
            nn.BatchNorm2d(128),
            nn.Dropout(),
            nn.ReLU(),
            nn.MaxPool2d(4))
		self.fc = nn.Linear(7*7*128, 10)
		
	def forward(self, x):
		out = self.layer1(x)
		out = self.layer2(out)
		out = self.layer3(out)
		out = out.view(batch, -1)
		out = F.sigmoid(self.fc(out))
		return out

def convert_image(path, _type='L', size=(500,500)):
	image = Image.open(path)
	image.thumbnail(size)
	image = image.convert(_type)
	pixels = image.load()
	px_array = np.zeros([size[0],size[1]],dtype=np.float32)
	for i in range(28):
		for j in range(28):
			px_array[i][j] = float(pixels[i,j]) 
	_object = (px_array - np.min(px_array))/(np.max(px_array) - np.min(px_array))
	return _object
	
def loader(batch_size, size=(28,28), tfolder='training'):
	folders = [ sp.check_output('ls {}/{}_holo/'.format(tfolder,i),shell=True).split() for i in range(10) ]
	n = min([ len(i) for i in folders ])
	epoch = int(n/batch_size)
	contener = []
	outputs = []
	for typ, files in enumerate(folders):
		contener.append([])
		batch_out = np.zeros([batch_size,10],dtype=np.float32)
		for batch_nr, _file in enumerate(files[0:n-1:batch_size]):
			batch_con = np.zeros([batch_size,1,size[0], size[1]],dtype=np.float32)
			
			for batch in range(batch_size):
				batch_con[batch][0] = convert_image('{}/{}_holo/{}'.format(tfolder,typ,files[batch_nr+batch].decode()), 'L', size)
				batch_out[batch][typ] = 1
			contener[typ].append(batch_con)
		outputs.append(batch_out)
		print('Loaded folder {}'.format(typ))
	return contener, outputs
				       
def merger(inputs, outputs):
	data = []
	print('mearging...')
	for _class, sets in enumerate(inputs):
		for batchs in sets:
			_set = [batchs, outputs[_class]]
			data.append(_set)
	random.shuffle(data)
	print(data[0][0].shape)
	print(data[0][1].shape)
	return data

def test(data1):
	ok = 0
	al = 0
	for i, sets in enumerate(data1):
		y=Variable(torch.from_numpy(sets[0]))
		o=Variable(torch.from_numpy(sets[1]))
		res = net(y)
		al += o.size(0)
		_, pre = torch.max(res.data,1)
		_, ac = torch.max(o.data,1)
		ok += (pre == ac).sum()
	print("Accuracy of Test Data: {}".format(ok/al))
	return float(ok/al)
	
def multitest(path, batch):
	files = sp.check_output('ls {}'.format(path),shell=True).split()
	x, y = [], [] 
	for wave in files:
		files2, out2 = loader(batch,tfolder='{}/{}'.format(path, wave.decode('UTF-8')))
		data2 = merger(files2, out2)
		acc = test(data2)
		x.append(float(eval(wave)))
		y.append(acc)
	plt.plot(x,y,'ro')
	plt.xlabel('z [m]')
	plt.ylabel('Accuracy')
	plt.grid(True)
	plt.show()
	plt.clf()
	
if __name__ == "__main__":
	batch = 16
	files, out = loader(batch)
	files2, out2 = loader(batch,tfolder='testing')
	data = merger(files, out)
	data2 = merger(files2, out2)
	try:
		net = torch.load('holonet.pt')
	except:
		net = HoloNet()
	if torch.cuda.is_available():
		net = net.cuda()
	loss = nn.MSELoss()
	opti = torch.optim.SGD(net.parameters(), lr=0.001,momentum=0.1)
	x,y, l, xx, yy = [], [], [], [], []
	_file = open('data.data','w')
	q = 0
	for t in range(5):
		for tt, i in enumerate(data):
			net.zero_grad()			
			y_pred = net(Variable(torch.from_numpy(i[0]))).cuda()
			loss_f = loss(y_pred, Variable(torch.from_numpy(i[1])))
			loss_f.backward()
			opti.step()
			if tt%200 == 0:
				x.append(q)
				q += 1
				res = test(data2)
				y.append(res)
				l.append(loss_f.data[0])
				print('loss: {}'.format(loss_f.data[0]))
				_file.write('{} {} {}\n'.format(str(q), str(loss_f.data[0]), str(res)))
	torch.save(net,'holonet.pt')
	_file.close()
	plt.plot(x,y,'ro')
	plt.grid(True)
	plt.xlabel('epoch [k]')
	plt.ylabel('Accuracy')
	plt.show()
	plt.clf()
	plt.plot(x,l,'ro')
	plt.xlabel('epoch [k]')
	plt.ylabel('MeanSquareError')
	plt.grid(True)
	plt.show()
	plt.clf()
	multitest('new',16)

			

		
