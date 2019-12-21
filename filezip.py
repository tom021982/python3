
import gzip
import shutil
with open('/root/pythonTraining/dishes', 'rb') as f_in:
    with gzip.open('/root/pythonTraining/dishes_zipped.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
