
import os
import shutil
list = []
for i in os.listdir('./dataset_candidates/'):
	list.append(i)

try:
	shutil.rmtree('./datasets')
	shutil.rmtree('./datasets/test')
	shutil.rmtree('./datasets/val')
	shutil.rmtree('./datasets/train')

	os.makedirs('./datasets')
	os.makedirs('./datasets/test')
	os.makedirs('./datasets/train')
	os.makedirs('./datasets/val')
except:
	os.makedirs('./datasets')
	os.makedirs('./datasets/test')
	os.makedirs('./datasets/train')
	os.makedirs('./datasets/val')
for i in list:


	for k in list:
		count = 0
		for final in ['train','test','val']:	
			try:
				shutil.rmtree('./datasets/'+final+'/'+k)				
				os.makedirs('./datasets/'+final+'/'+k)
			except:
				os.makedirs('./datasets/'+final+'/'+k)

		for l in os.listdir('./lfw/'+k):
			if (count>=10):break			
			count+=1
			if(count<=7):
				final = 'train'
			elif(count>7 and count<=9):
				final = 'val'
			elif(count==10):
				final = 'test'
			print(k+'/'+l)
			

			shutil.copy('./lfw/'+k+'/'+l , './datasets/'+final+'/'+k)


			

