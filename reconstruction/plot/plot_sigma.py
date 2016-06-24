import collections
from copy import deepcopy
import csv
from ROOT import *


def get_data(csv_input, value_names, inner_keys, ignore_keys):
  reader = csv.DictReader(csv_input)
  data = collections.defaultdict(lambda: collections.defaultdict(list))
  for row in reader:
    key = tuple(float(row[k]) for k in inner_keys)
    value = tuple(float(row[v]) for v in value_names)
    outer_key = ':'.join(
        '%s-%s' % kv for kv in sorted(row.items()) if kv[0] not in (
            inner_keys + value_names + ignore_keys))
    data[outer_key][key].append(value)
  return data


# data = [(x, y, y_err), (x, y, y_err), ...]
def make_graph_line(data):
  graph_line = TGraphErrors()
  for i, (x, y, y_err) in enumerate(sorted(data)):
    graph_line.SetPoint(i, x, y)
    graph_line.SetPointError(i, 0, y_err)
  return graph_line


# data[(Nsample, Nfreq)] = [(x, y, y_err), (x, y, y_err), ...]
def make_multigraph(data, out_root_file=None, graph_name="gr",
                    title="", x_axis_title="",
                    save_canvas_as=""):

  lines = [(10.0, 25.0), (20.0, 12.5), (40., 6.25)]

  g_lines = []

  for line_idx, line_val in enumerate(lines):
      graph_line = make_graph_line(data[line_val])
      graph_line.SetName("%s:nSmpl-%.2f:nFreq-%.2f" % ((graph_name,) + line_val))

      graph_line.SetMarkerColor(100 - (line_idx*12)%50)
      graph_line.SetLineColor(100 - (line_idx*12)%50)
      graph_line.SetMarkerStyle(line_idx+20)
      graph_line.SetMarkerSize(2)
      graph_line.Draw("ALP")

      if out_root_file:
        graph_line.Write()

      g_lines.append([graph_line, "NSAMPLE=%d NFREQ=%.2f" % line_val])


  # The canvas to be used 
  canvas = TCanvas("title", "name", 1200, 1000)
  # Initialize the graph and legend
  graph  = TMultiGraph()
  #legend = TLegend(0.4,0.8,0.8,0.95)
  legend = TLegend()

  graph.SetName("multi_%s" % graph_name)
  graph.SetTitle(title)
  legend.SetName(title + "_leg")
  legend.SetBorderSize(1)
  # Add the lines to the graph/legend
  for g in g_lines:
      graph.Add(g[0])
      legend.AddEntry(g[0], g[1], "p")
  graph.Draw("APL")
  graph.GetXaxis().SetTitle(x_axis_title)
  legend.Draw()
  if out_root_file:
    graph.Write()
  if save_canvas_as:
    canvas.SaveAs(save_canvas_as)


def main(infile_name="results.csv", outfile_name="plot_sigma.root", save_canvas_as=""):
  f = open(infile_name, "r")
  d = get_data(f, ("sigmaNoise", "sigma_eff", "sigma_eff_err"), ("nSmpl", "nFreq"), ("avg_reco_amplitude",))
  f.close()

  outrootfile = TFile(outfile_name, "RECREATE")
  for outer_key, inner_data in d.iteritems():
    print outer_key
    make_multigraph(inner_data, outrootfile, outer_key)
  outrootfile.Close()


if __name__ == '__main__':
  main("results.csv", "plot_sigma_more_complicated.root")
