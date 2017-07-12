ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
brew install python
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
pip install http://download.pytorch.org/whl/torch-0.1.12.post2-cp27-none-macosx_10_7_x86_64.whl 
pip install torchvision 
wget http://vis-www.cs.umass.edu/lfw/lfw.tgz
tar -zxvf ./lfw.tgz
python get_20_30_images.py
