import os
import sys

if __name__ == '__main__':

    print sys.argv

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun

    old_input_files = set()
    input_files = set()
    while True:
      old_input_files = input_files
      input_files = set(os.listdir('input'))
      if input_files == old_input_files:
          break
      for f in sorted(input_files):
          if '43' in f:
            continue
          i = 'input/%s' % f
          o = 'outputfit/%s' % f.replace('mysample', 'output')
          if os.path.exists(o):
            #print "skipping %s --> %s because %s already exists." %(i, o, o)
            continue  # not recreating+overwriting existing files
          params = f.split('_')
          NSAMPLES, NFREQ = params[3 : 5]
          toExec = 'bin/Example07.multifit %s %s %s %s' % (i, o, NSAMPLES, NFREQ)
          print toExec
          if (dryrun == 0) :
              os.system(toExec)
