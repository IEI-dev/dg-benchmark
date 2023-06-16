import sys
import re

loglines=[]
modelpaths=[]
with open( sys.argv[1]) as f:
    modelpaths = list(f)

with open( sys.argv[2]) as f:
    loglines = list(f)

#print( len(loglines))
modelprofs=[]
for line in loglines:
    if 'Throughput:' in line:
        xre=re.search(r'Throughput: +(\d*.*\d+)', line)
        fps = float(xre[1])
        idx=len(modelprofs)
        prof={ 'path': modelpaths[idx].strip('\n'), 'fps': fps}
        modelprofs.append(prof)

def rearrange(models):
    for m in models:
        #public/mobilenet-ssd/FP32/mobilenet-ssd.xml
        [cls, nm, prec, fn] = m['path'].split('/')
        m['name'] = nm
        m['prec'] = prec

def dumpmodel( m):
    print( m['name'], m['prec'], m['fps'])


#| Tables   |      Are      |  Cool |
#|----------|:-------------:|------:|
#| col 1 is |  left-aligned | $1600 |
#| col 2 is |    centered   |   $12 |
#| col 3 is | right-aligned |    $1 |

def models_markdown_table(models):
    print('| Name  | Precision  |  FPS |')
    print('|-------|------------|------|')
    for m in models:
        print('| {}   |  {}  | {} |'.format( m['name'], m['prec'], m['fps']))


rearrange(modelprofs)
models_markdown_table( modelprofs)
 



