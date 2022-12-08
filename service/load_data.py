import gdown


url = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1W2ckIrN7KKiMZbF00hfH0rFSTKdmPZnr'
gdown.download(url, '../service/pretrained_models/tfidf_15.dill')

url = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1-5yCqSkSO-FECtoWlg2DdtsbUpRQy6qu'
gdown.download(url, '../service/data/genres_dict.dill')

url = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Kf4IDl2LNlc-9sR2kGj7AGbThba75Oww'
gdown.download(url, '../service/data/items_dict.dill')

print('Данные загружены')

