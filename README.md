# El Paso Project

We first use a deep neural network-based seismic algorithm to identify seismic arrivals from natural and possibly mining events. We then will run an optimized STA/LTA detector to identify emergent, long duration signals, typical of trains, and then compare our results to the train schedule, where train traffic is very active. Trains can also be identified using spectral and beamforming analysis. We will use these techniques to compare our results with those from the STA/LTA and machine learning approaches. Finally, we will compare the differences in energy recorded by stations with variable site surface geology, incorporating signals recorded by a permanent broadband station as a reference.


# Phase Detection - PhaseNet
### Documentation: https://github.com/AI4EPS/PhaseNet
Make sure neccessary packages are installed

# Running PhaseNet

python phasenet/predict.py --model=model/190703-214543 --data_list=working_dataset/fnames.csv --data_dir=working_dataset/data --stations=working_dataset/mstations.json  --format=mseed_array --amplitude
