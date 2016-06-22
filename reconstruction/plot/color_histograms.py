from ROOT import *
from glob import glob
import os
import sys


def chi2_under_cutoff(tree, chi2_cutoff=10):
  return tree.chiSquare < chi2_cutoff


def reco_largest_at_intime(tree, in_time_bx=4):
  return tree.samplesReco.at(in_time_bx) == max(tree.samplesReco)


def reco_large_enough(tree, reco_fraction_cutoff=0.1, in_time_bx=4):
  return tree.samplesReco.at(in_time_bx) > reco_fraction_cutoff * tree.amplitudeTruth


def classify_recos(filename, in_time_bx=4, test=lambda x: True, bins=100, xmin=0, xmax=20):

  good_list = []
  bad_list = []
  prefix = filename.replace('.root', '')
  prefix += '_reco_at_bx_%d' % in_time_bx
  all_hist = TH1F("%s_all" % prefix, "", bins, xmin, xmax)
  good_hist = TH1F("%s_good" % prefix, "", bins, xmin, xmax)
  bad_hist = TH1F("%s_bad" % prefix, "", bins, xmin, xmax)

  tfile = TFile(filename, "Read")
  tree = tfile.Get("RecoAndSim")
  entries = tree.GetEntries()
  for event in range(0, entries):
    tree.GetEntry(event)
    reco_amplitude = tree.samplesReco.at(in_time_bx)
    all_hist.Fill(reco_amplitude)
    if test(tree):
      good_list.append(reco_amplitude)
      good_hist.Fill(reco_amplitude)
    else:
      bad_list.append(reco_amplitude)
      bad_hist.Fill(reco_amplitude)
  tfile.Close()
  return all_hist, good_hist, bad_hist, good_list, bad_list


def draw_together(histograms, colors=[], save_canvas_as="",
                  x_axis_title="", hist_title="", out_root_file=None):
  c = TCanvas('_'.join([h.GetName() for h in histograms]), "title", 1)
  for hist, color in zip(histograms, colors):
    hist.SetLineColor(color)
  # Draw "tallest" histogram first so the axis will be long enough
  height = lambda hist: hist.GetBinContent(hist.GetMaximumBin())
  for i, h in enumerate(sorted(histograms, key=height, reverse=True)):
    if i == 0:
      h.GetXaxis().SetTitle(x_axis_title)
      h.SetTitle(hist_title)
      h.Draw()
    else:
      h.Draw("SAME")
  if save_canvas_as:
    c.SaveAs(save_canvas_as)
  if out_root_file:
    c.Write()


def main(filename, test=lambda x: True, in_time_bx=4,
         bins=100, xmin=-20, xmax=20, save_as_prefix='reco1D'):

  _, good_hist, bad_hist, _, _ = classify_recos(filename, in_time_bx, test, bins, xmin, xmax)

  suffix = filename.replace('outputfit/output_', '').replace('.root', '')
  _, shift, pu_shift, nsample, nfreq, amplitude, npu, noise, _, wf = suffix.split('_')


  outfilename = "%s_%s.root" % (save_as_prefix, suffix)
  outrootfile = TFile(outfilename, "RECREATE")

  hist_title = (('reconstructed %s pulse amplitude: ' +
                 '(true) AMPLITUDE=0.0, NSAMPLE=%s, NFREQ=%s, NPU=%s, NOISE=%s')
                % (wf, nsample, nfreq, npu, noise))
  png_name = "%s_%s.png" % (save_as_prefix, suffix)

  #draw_together([good_hist, bad_hist], [kRed],
                #x_axis_title="GeV", hist_title=hist_title, save_canvas_as=png_name)
  draw_together([good_hist, bad_hist], [kRed],
                x_axis_title="GeV", hist_title=hist_title, out_root_file=outrootfile)

  outrootfile.Close()


if __name__ == "__main__":
    
    args = []
    # for loop that converts arguments with a '*' to the corresponding files
    for arg in sys.argv[1:]:
        args += glob(arg)
    print args
    for f in args:
      #main(f, reco_largest_at_intime)
      main(f, xmin=9, xmax=11, save_as_prefix='two_color_reco1D_to1', test=reco_largest_at_intime)
      main(f, xmin=5, xmax=15, save_as_prefix='two_color_reco1D_to5', test=reco_largest_at_intime)
      main(f, xmin=0, xmax=20, save_as_prefix='two_color_reco1D_to10', test=reco_largest_at_intime)
      main(f, xmin=-10, xmax=30, save_as_prefix='two_color_reco1D_to20', test=reco_largest_at_intime)
