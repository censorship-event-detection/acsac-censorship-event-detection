# censorship-event-detection

This repository contains the framework and data presented in I Can Show You the World (of Censorship): Extracting Insights from Censorship Measurement Data Using Statistical Techniques. Our framework consists of two statistical techniques, the Mann-Kendall trend detection test (MK) and control charts when applied to censorship measurement data, it identifies changes in the data corresponding to potential censorship events. In our paper, we implemented our framework on data from Censored Planet's Satellite, Hyperquack HTTP, and HTTPS as well as OONI, GFWatch, and Tor. We used data from six countries - Russia, Myanmmar, China, Iran, Türkiye, and Pakistan - from January 2021 through March 2023.

# Repository contents:
- An implementation of our framework as a Jupyter notebook ([Framework.ipynb](/framework)). The notebook can be edited to run on any censorship measurement or network measurement dataset. 
- An implementation of our framework applied to all of the datasets used in our paper ([framework.py](/framework)). The framework outputs the results in ([results](/results)). For further information see the README in `/results`.
- The source code for the Figures in Appendix B as a Jupyter notebook ([Signal_Figures.ipynb](/framework)). Figures 5-10 in the paper are zoomed in versions of these figures. Run `framework.py` before running `Signal_Figures.ipynb` as the notebook uses the output files from `framework.py` to generate the figures.
- The processed data used in our paper ([data](/data)) for more details see the README in `/data`.

# Environment
All experiments were executed on a machine running macOS Sonoma 14.6.1

# Requirement
Python3.9

# Setup
After cloning the repository, setup a python virtual environment within the project directory:
```
python3 -m venv my_env
source my_env/bin/activate
```
Install required python libraries:
```
pip install -r requirements.txt -I
```
# Running the framework
- `Framework.ipynb` can be executed as is within a Jupyter notebook environment (launch environment by running `jupyter notebook`). It will run on OONI China data. To run the notebook on a new dataset edit the variables `path_to_dataset`, `typ`, `version`, and `index` to fit the new dataset.

- To execute `framework.py`:
```
cd framework
python3 framework.py
```
- The results will be output to csv files and stored in `/results`.
- After running `framework.py` to generate the result files, run `Signal_Figures.ipynb` in a Jupyter notebook environment.
