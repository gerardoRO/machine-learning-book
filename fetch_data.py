import os
import tarfile
from urllib import request

DOWNLOAD_ROOT='https://raw.githubusercontent.com/ageron/handson-ml/master/'
HOUSING_URL= DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'
DATA_PATH='data_folder/housing'

def fetch_housing_data(housing_url = HOUSING_URL,data_path=DATA_PATH):
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    
    tgz_path = os.path.join(data_path, 'housing.tgz')
    request.urlretrieve(housing_url,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=data_path)
    housing_tgz.close()