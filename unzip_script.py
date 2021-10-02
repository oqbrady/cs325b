import os
import tarfile
from tqdm import tqdm
folder_with_tars = "unzip_test/"
dest = "unzip_dest/"
fls = os.listdir(folder_with_tars)
for fl in tqdm(fls):
    file = tarfile.open(folder_with_tars + fl)
    file.extractall(dest)
    file.close()