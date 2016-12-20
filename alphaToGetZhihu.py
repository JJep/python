#encoding:UTF-8

import gzip
def ungzip(data):
    try:
        print('zipping...')
        data = gzip.decompress(data)
        print('zipped!')
    except:
        print('no use to zip')
    return data
        
