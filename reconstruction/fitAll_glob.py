import os
import sys

def fit_waveform(input_files, waveform, already_fit_files, dryrun=0):
  for f in sorted(input_files):
      if waveform not in f:
        continue
      if not f.startswith('mysample'):
        continue
      multifit(f, already_fit_files, dryrun)

def multifit(f, already_fit_files, dryrun=0):
  i = 'input/%s' % f
  o = 'outputfit/%s' % f.replace('mysample', 'output')
  if os.path.exists(o):
    #print "skipping %s --> %s because %s already exists." %(i, o, o)
    already_fit_files += 1
    return  # not recreating+overwriting existing files
  print f
  params = f.split('_')
  NSAMPLES, NFREQ = params[3 : 5]
  waveform = params[-1].split('.')[0]
  toExec = 'bin/Example07.multifit %s %s %s %s %s' % (i, o, NSAMPLES, NFREQ, waveform)
  print toExec
  if (dryrun == 0) :
      os.system(toExec)


if __name__ == '__main__':

    print sys.argv

    dryrun = 0
    if len(sys.argv) > 1 :
      print " dry run option:",
      dryrun = sys.argv[1]
      print dryrun

    old_input_files = set()
    input_files = set()
    already_fit_files = 0
    wfs = ["CRRC10", "CRRC20", "CRRC30", "CRRC43", "CRRC60", "CRRC90",
           "QIE25", "QIE12", "QIE6"]
    while True:
      old_input_files = input_files
      input_files = set(os.listdir('input'))
      print len(old_input_files)
      print len(input_files)
      if input_files == old_input_files:
          print "no new input files"
          break
      for wf in wfs:
         fit_waveform(input_files, wf, already_fit_files)
    print already_fit_files, "already fit files"
