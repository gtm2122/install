import os
import shutil
list = []
for i in os.listdir('./lfw'):
	if len(os.listdir('./lfw/'+i))>10 :
		list.append(i)
try:
	shutil.rmtree('./celeb_imgs/')
	os.makedirs('./celeb_imgs/')
	
except:	
	os.makedirs('./celeb_imgs/')	

try:
	shutil.rmtree('./dataset_candidates/')
	os.makedirs('./dataset_candidates/')
	
except:	
	os.makedirs('./dataset_candidates/')	


for i in list:
	print(i)
	
	
	#shutil.rmtree('./celeb_imgs/')
	try:
		shutil.rmtree('./celeb_imgs/'+i)
		#os.makedirs('./celeb_imgs/'+i)
		shutil.copytree('./lfw/'+i,'./celeb_imgs/'+i)			

	except:
		#os.makedirs('./celeb_imgs/'+i)
		shutil.copytree('./lfw/'+i,'./celeb_imgs/'+i)			

		
		
		
