import os, sys
import re
import importlib
import archive
import numpy as np
# first line: filn number
# second line attribute name
# file name, attr flag 1 and -1

if __name__ == '__main__':
    dataname = 'cityscape'
    dirname = './datasets/cityscape'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    datainfo = archive.datasets[dataname]
    domainname = ['cityscape', 'seg', 'synthia']
    phases = ['train', 'test']
    lines = []
    attrlen = len(datainfo['train'])
    for phase in phases:
        imgfolder = os.path.join(dirname, phase)
        if not os.path.exists(imgfolder):
            os.makedirs(imgfolder)

        for i, pattern in enumerate(datainfo[phase]): # for every domain
            labels = -np.ones((attrlen,), dtype=np.int)
            labels[i] = 1
            dirn, fpat = os.path.split(pattern)
            imgnames = os.listdir()
            for name in imgnames:
                if re.fullmatch(pattern, name) is not None:
                    s = name + ' ' + ' '.join(labels)
                    lines.append(s)
                    src = os.path.join(dirn, name)
                    dst = os.path.join(imgfolder, name)
                    os.symlink(src, dst) # make soft symbol
    
    attr_file = os.path.join(dirname, 'list_attr_celeba.txt'):
    with open(attr_file, 'w') as f:
        f.write(str(len(lines)) + '\n')
        f.write(' '.join(domainname) + '\n')
        f.write('\n'.join(lines))

            