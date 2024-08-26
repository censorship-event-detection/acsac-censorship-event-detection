# Results directory
Run [framework.py](/framework) to generate the result files which include a single summary file containing all the dates of the signals found (all_signal_dates.csv) as well as individual files for each country/dataset pair with details on the same signals (e.g., cn-ooni.csv). The signal dates in both the summary file and the individual country/pair files were used to create the figures in Appendix B of our paper.

# Contents of result files
- all_signal_dates.csv file
    - Signal Start: Date the signal started
    - Signal End: Date the signal ended
    - Type: The type of signal detected
        - Mann-Kendall increasing/decreasing or above/below the control chart limits
    - Country: Country code for the country where the data was collected
        - CN = China, IR = Iran, MM = Myanmar, PK = Pakistan, TR = Türkiye, RU = Russia
    - Dataset: Dataset that the signal was identified in
        - http (Hyperquack HTTP), https (Hyperquack HTTPS) satellite, ooni, gfwatch, or tor

- <country_code>-<dataset>.csv files
    - Same signals that are in the all_signal_dates.csv file but with additional information
    - Start Date: Date the signal started
    - End Date: Date the signal ended
    - MK Signal: Indicates if a Mann-Kendall signal is present `increasing`, `decreasing` or `no trend`
    - Control Limit Signal: Indicates if the control chart limits have been calculated and if a signal is present. `above limits` or `below limits` indicates a signal. `Within limits` indicates no signal, and `Waiting` means that the control chart limits have not been calculated because there have not yet been enough data points to create a baseline. 
    - Current Mean: Value of the current control chart mean
    - Current UCL: Value of the current control chart upper control limit
    - Current LCL: Value of the current control chart lower control limit
