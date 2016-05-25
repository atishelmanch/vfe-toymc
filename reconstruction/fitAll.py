from glob import glob
import os
import sys

if __name__ == '__main__':

    print sys.argv

    dryrun = 0
    if len(sys.argv) > 1 :
       print " dry run option:",
       dryrun = sys.argv[1]
       print dryrun
    cmds = []
    #for f in os.listdir('input'):
    for f in glob('input/mysample_1_0_40_6.25_*_0.00_*_1.00_CRRC10.root'):
	#i = 'input/%s' % f
	i = f
	#o = 'outputfit/%s' % f.replace('mysample', 'output')
	o = 'outputfit/%s' % f.replace('input/mysample', 'output').replace('root',
            'chiSquare.root')
	toExec = 'bin/Example07.multifit.chiSq %s %s 40 6.25 CRRC10' % (i, o)
        cmds.append(toExec)
	print toExec
	if (dryrun == 0) :
	    os.system(toExec)

    for s in cmds:
      print s
