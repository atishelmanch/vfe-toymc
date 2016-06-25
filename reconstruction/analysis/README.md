Analysis tools
====


Scan all results:

    python analysis/scan.py outputfit/output_*.root
    
the output is a file "results.csv".
    
Then plot:

    python analysis/plot_sigma.py

Then make second-order plots:

    python analysis/sigma_slope.py
