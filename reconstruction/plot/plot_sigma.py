import collections
from copy import deepcopy
import csv
from ROOT import *


def get_data(csv_input, values, outer_keys):
  reader = csv.DictReader(csv_input)
  data = collections.defaultdict(list)
  for row in reader:
    key = tuple(row[k] for k in outer_keys)
    value = tuple(row[v] for v in values)
    data[key].append(value)
  return data


# data[(Nsample, Nfreq)] = [(shift, amplitude), (shift, amplitude), ...]


def make_one_graph(data, waveform="unknown", x_axis="Shift", title=""):


  lines = [(10.0, 25.0), (20.0, 12.5), (40., 6.25)]

  g_lines = []

  # First we iterate through all combos to make points/lines to fill
  for line_idx, line_val in enumerate(lines):
      # Initialize the line with error bars
      graph_line = TGraphErrors()
      graph_line.SetName("gr_%f_%f" % (line_val))
      graph_line.SetMarkerColor(100 - (line_idx*12)%50)
      graph_line.SetLineColor(100 - (line_idx*12)%50)
      graph_line.SetMarkerStyle(line_idx+20)
      graph_line.SetMarkerSize(2)

      for point_idx, (x_val, y_val) in enumerate(sorted(data[line_val])):
          if abs(x_val) < 5:
            graph_line.SetPoint(
                point_idx, x_val, y_val)

      graph_line.Draw("ALP")
      graph_line.Write()
      g_lines.append([deepcopy(graph_line), 
                      "NSAMPLE = " + str(line_val[0]) + 
                      " NFREQ = " + str(line_val[1])])


  # The canvas to be used 
  canvas = TCanvas("title", "name", 1200, 1000)
  # Initialize the graph and legend
  graph  = TMultiGraph()
  #legend = TLegend(0.4,0.8,0.8,0.95)
  legend = TLegend()

  graph.SetName("multigr")
  graph.SetTitle(title)
  legend.SetName(title + "_leg")
  legend.SetBorderSize(1)
  # Add the lines to the graph/legend
  for g in g_lines:
      graph.Add(g[0])
      legend.AddEntry(g[0], g[1], "p")
  graph.Draw("APL")
  graph.GetXaxis().SetTitle("shift (ns)")
  legend.Draw()
  graph.Write()
  if waveform.startswith("QIE"):
    waveform = "QIE"
  canvas.SaveAs(
      "amplitude_vs_%s_%s.png" % (x_axis.lower(), waveform))


wfs = ["QIE6", "QIE12", "QIE25", "CRRC10", "CRRC20", "CRRC30",
       "CRRC43", "CRRC60", "CRRC90"]
wfs = ["QIE*", "CRRC10", "CRRC20", "CRRC30",
       "CRRC43", "CRRC60", "CRRC90"]

all_datas = []


f = open("results.csv", "r")
d = get_data(f, ("sigmaNoise", "sigma_eff"), ("nSmpl", "nFreq"))
for k, v in d.iteritems():
  print k
  print v
