import os
import sys

if __name__ == '__main__':

    print sys.argv
    
    dryrun = 0
    if len(sys.argv) > 1 :
       print " dry run option:",
       dryrun = sys.argv[1]
       print dryrun
    for f in os.listdir('input'):
	i = 'input/%s' % f
	o = 'outputfit/%s' % f.replace('mysample', 'output')
	toExec = 'bin/Example07.multifit %s %s' % (i, o)
	print toExec
	if (dryrun == 0) :
	    os.system(toExec)
      
  




       

       
