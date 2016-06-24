from ROOT import TFile
import plot_sigma

def fit_lines(filename="plot_sigma.root"):
  tfile = TFile(filename, "Read")
  slopes = {}
  key_list = tfile.GetListOfKeys()
  for key_obj in key_list:
    key = key_obj.GetName()
    if key.startswith('multi'):
      continue
    tokens = key.split(':')
    print tokens
    params = dict(kv.split('-') for kv in tokens)
    tau = float(params['pulse_tau'])
    n_sample = float(params['nSmpl'])
    n_freq = float(params['nFreq'])
    gr = tfile.Get(key)
    result_ptr = gr.Fit("pol1", "S")
    slope = result_ptr.Parameters()[1]
    slope_err = result_ptr.ParError(1)
    slopes[(n_sample, n_freq)] = (tau, slope, slope_err)
  tfile.Close()
  return slopes

if __name__ == '__main__':
  slopes = fit_lines("plot_sigma_more_complicated.root")
  outfile = TFile("sigma_slopes_vs_tau.root")
  plot_sigma.make_multigraph(slopes, outfile)
  outfile.Close()
