# censorship-event-detection

This repository contains the framework and data presented in I Can Show You the World (of Censorship): Extracting Insights from Censorship Measurement Data Using Statistical Techniques.

# Repository contents:
- The data used in our paper ([data](/data))
  - We implemented our framework on data from Censored Planet's Satellite, Hyperquack HTTP, and HTTPS as well as OONI, GFWatch, and Tor. We used data from six countries - Russia, Myanmmar, China, Iran, Türkiye, and Pakistan - from January 2021 through March 2023.
- An implementation of our framework as a Jupyter notebook ([framework.ipynb](/framework)). The notebook can be edited to run on any censorship measurement or network measurement dataset.
  - Our framework consists of two statistical techniques, the Mann-Kendall trend detection test (MK) and control charts. After performing the MK and control chart calculations, the Jupyter notebook outputs the dates of the signals found by the framework. 
- An implementation of our framework applied to all of the datasets used in our paper ([framework.py](/framework)). The framework outputs the results in ([results](/results)) as a single summary file containing all the dates of the signals found (all_signal_dates.csv) as well as individual files for each country/dataset pair with details on the same signals (e.g., cn-ooni.csv).
  - The signal dates in both the summary file and the individual country/pair files were used to create the figures in Appendix B of our paper. 

# Setup
After cloning the repository setup a python virtual environment within the project directory:
```
python3 -m venv my_env
source my_env/bin/activate
```
Install required python libraries:
```
pip install -r requirements.txt
```
# Running the framework
- `framework.ipynb` can be executed as is within a Jupyter notebook environment (launch environment by running `jupyter notebook`). It will run on OONI China data. To run the notebook on a new dataset edit the variables `path_to_dataset`, `typ`, `version`, and `index` to fit the new dataset.

- To execute `framework.py`:
```
cd framework
python3 framework.py
```
- The results will be output to csv files and stored in `/results`

