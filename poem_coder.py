#!/usr/bin/env python
#coding: utf-8
import os

def run(filename):
    if os.path.exists(filename):
        return
    with open(filename, 'w') as f:
        text = """#!/usr/bin/env python
#coding: utf-8
import %s

def run():
    pass

if __name__ == "__main__":
    run()
        """ % filename.split('.')[0].split('_')[-1]
        f.write(text)
    print 'Generate %s Successful.' % filename

if __name__ == "__main__":
    prefix = "try_"
    filenames = ['requests', 'json', 'subprocess', 'pymysql', 'redis', 'pymongo']
    splitext = ".py"
    for filename in filenames:
        run(prefix + filename + splitext)