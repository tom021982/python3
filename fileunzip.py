
import gzip
import shutil

with gzip.open('/root/pythonTraining/dishes_zipped.gz', 'rb') as f_in, open('/root/pythonTraining/sourced_out.txt', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
