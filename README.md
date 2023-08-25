# Event-based-neuron

This is the readme for the event-based modeling framework described in the manuscript titled 
Reproducibility of biophysical in silico neuron states and spikes from event-based partial histories.

To recreate the figures from this paper, begin by running the `init.sh` script to build the data directories and compile 
the mod files.
This script works for linux and Mac systems, modify this to work in Windows.

The data of this project is generated with the various scripts and script wrappers in `./scripts`. The figures themselves 
are generated within jupyter notebooks within `./notebooks` and saved in the figures folder `./figures`. All of which 
utilize code from the `./utils` directory.

## Python Requirements
- jupyter
- NEURON 8.2
- numpy
- scipy
- matplotlib


## Paper Figures
All figures of Cudone et al. 2023 can be reconstructed from the contents of this repository. 

- **Figure 1**: Top and middle generated using `notebooks/model_specs.ipynb`; which lays out the parameterizations for the Hodgkin-Huxley (HH) and Wang-Buzsaki (WB) point cells for the event-based encodings manuscript. The Wang-Buzsaki is first described in https://doi.org/10.1523/jneurosci.16-20-06402.1996, and built using the implementation from the ModelDB entry 26997.

Bottom generated using `morpho/model_specs_morpho.ipynb`; with specifics of the the parameterization for the morphologically detailed CA1 pyramidal cell used in the event-based encodings manuscript. This models uses morphology originally from https://doi.org/10.1002/cne.903620103 and hosted on NeuroMorpho.org (https://doi.org/10.1523/jneurosci.2055-07.2007). The model is based off of Tom Morse's implementation: model 87284 on ModelDB. Our implementation recieves stimuli independently from 15 excitatory and 15 inhibitory synapses at random locations in the cell's dendrites. 

- **Figure 2**: Generated using `notebooks/spike_centered.ipynb`; Inspired by on conversations with Dr. Robert McDougal and Dr. Ted Carnevale.

- **Figure 3**: data generated with `partial_history.py` within the scripts folder for the 
Hodgkin Huxley models, and `partial_history_WB.py` within the scripts folder for the 
Wang Buzsaki models. Figures visualized within `notebooks/partial_history.ipynb`.

The partial histories scripts first generate stimuli patterns, then random cell histories (state variable frames) and then run experiments simulating the combination of each of the stimuli patterns with each of the histories with each value of n for n inputs. The results allow for the statistical analysis of response distributions given ambiguity in initial conditions and differing quanta of input stimuli. 

- **Figures 4**: data generated with `scripts/nst_distribution_evolution.py` and visualized within `nst_distribution_evolution_voltage_traces.ipynb`.

Displays an example of how the membranve voltage traces and the distribution of NSTs of a HH model change as more history (input stimuli) is provided, given ambiguity in the initial conditions.

- **Figures 5**: data generated with `scripts/nst_distribution_evolution.py` and visualized within `nst_distribution_categorical_evolution.ipynb`, and 
`nst_distribution_evolution_phase_diagram.ipynb` in the notebooks directory.

`nst_distribution_categorical_evolution.ipynb` looks at the evolution of the NST distributions as n, the number of stimuli events known by the model, increases. The NST distributions are categorized into one of four categories describing whether the distribution of responses is deterministic or not, and whether it is spiking or not.

`nst_distribution_evolution_phase_diagram.ipynb` categorizes the observed response (NST) distributions by whether they are deterministic or not and spiking or not. Then, builds phase diagrams describing how these transitions flow through these categories. Lastly, interogates the specific stimuli conditions (interval between stimuli and type of stimuli) that result in these conditions arising. 

- **Figures 6**: data generated with `scripts/nInputs.py` for the Hodgkin Huxley model and `scripts/nInputs_WB.py` for the Wang Buzsaki model, which utilize the wrappers `scripts/nInputs_wrapper.sh` and `scripts/nInputs_WB_wrapper.sh` respectively. These scripts run the n inputs experiments which simulates a neuron cell using the on-event framework introduced in Cudone et al. 2023. This requires the mod file `nInputs50.mod` in the `mod` folder to be compiled with NEURON.

Visualization is in `notebooks/nInputs_analysis.ipynb`, which shows the inter-spike-interval distributions the spike trains of the simulated event-based cells with varying values of n inputs, compared against the standard conductance-based model ISI distributions.

- **Figures 7**: data generated with `scripts/nInputs.py` for the Hodgkin Huxley model and `scripts/nInputs_WB.py` for the Wang Buzsaki model, which utilize the wrappers `scripts/nInputs_wrapper.sh` and `scripts/nInputs_WB_wrapper.sh` respectively. These scripts run the n inputs experiments which simulates a neuron cell using the on-event framework introduced in Cudone et al. 2023. This requires the mod file `nInputs50.mod` in the `mod` folder to be compiled with NEURON.

Visualization is in `notebooks/nInputs_analysis.ipynb`, which shows the victor purpura and van Rossum distances between the spike trains of the simulated event-based cells with varying values of n inputs, compared against the standard conductance-based model.

- **Figures 8**: nInputs data generated with `morpho/scripts/nInputs.py`, batch ran using dSQ and the joblist `morpho/scripts/nInputs_dSQ_joblist.txt`, ground truth simulations of the conductance-based model simulated with `morpho/scripts/nInputs_groundtruth_sims.py`. Requires stimuli locations files to be generated beforehand using the `morpho/scripts/initialize_stimuli_locs.py` script.

Visualized with `morpho/nInputs_analysis.ipynb` where raster plots of the ground truth conductance-based models are compared to the resulting spike trains of the n Inputs experiments, for the CA1 pyramidal cell. Additionally, van Rossum spike distances measured between the spike trains. 

- **Figure 9**: data for figure 9A, the point cell analysis, is generated from `scripts/generate_spiking_histories.py` which generates a large sum of spiking histories, and `scripts/state_reconstruct.py` which runs the pairs of simulations with identical input events but variable initial conditions, and saves thier membrane voltages. The analysis and visualization are within `notebooks/state_reconstruction.ipynb`, which finds the difference, or error, between the observed membrane voltages, which is the result of the differences in the spiking histories used as initial condtions for the simulation pairs.

  Data for 

## Repository contents

### utils 
`HH.py`
Contains the HH point cell model as a python class used throughout the codebase.

`Morpho.py`
Contains the morphologically detailed CA1 pyramidal cell as a python class used throughout the codebase. This class uses neuroMorpho's cell morphology file (Ascoli et al. 2007) originally from the work of (Ishizuka et al. 1995). This file is contained in the resources directory in this repository. 

`Stimuli.py`
Contains python classes and functions to assist in stimuli generation throughout the codebase; maintains consistency with synaptic parameterizations. 


### scripts
runs much of the experiments and outputs data to be analyzed in the jupyter notebooks in ./notebooks

`nInputs.py`
Performs the nInputs experiment on the HH model using the event-based-neuron framework within NEURON. 
This generates the data necessary for Figure 6 and Figure 7
    
`nInputs_wrapper.sh`
Bash script to run the nInputs.py script with each of the HH point cell synaptic parameterizations. 

`nInputs_morpho.py`
Performs the nInputs experiment on the morphologically detailed CA1 pyramidal cell. This script produces the 
data responsible for Figure 8 and Figure 9.
        
`nInputs_morpho_wrapper.sh`
Bash script for running the nInputs_morpho.py script. 

`partial_history_setup.py`
Generates the stimuli and histories necessary to do the partial histories experiment in partial_history.py

`partial_history.py`
Performs the partial histories experiment responsible for Figure 3 using the stimuli and histories generated in partial_history_setup.py.
    
`nst_distribution_evolution.py`
Runs the simulations responsible for Figure 4 and Figure 5. 
    
`state_reconstruct_part1.py`
Runs an extended simulation of a conductance-based HH point cell for which to compare reconstructed state variables of the event-based analog to. 

state_reconstruct_part2.py
Models a cell using the event-based-framework and then reconstructs the state variables of given windows. 

`state_reconstruct_part3.py`
Calculates the errors between the conductance-based model's state variables and the analogous event-based state variable reconstructions. 

`state_reconstruct_morpho_part1.py`
Runs an extended simulation of a conductance-based morphologically detailed CA1 pyramidal cell for which to compare reconstructed state variables of the event-based analog to. 
        
    
### data
directory to store intermediate and output data from the python scripts. Internal directory structure for all analysis 
should be as follows and is instantiated with `init.sh`.
    
    ./nInputs
    ./nInputs_morpho
    ./nst_distribution_evolution
        ./results
        ./stimuli
    ./partial_history
        ./results
    ./state_reconstruct
        ./original_simulation_data
        ./reconstruction_data
    ./state_reconstruct_morpho
        ./original_simulation_data
    
        

### notebooks
holds all of the jupyter notebooks used to generate the figures in the manuscript.
`model_specs.ipynb`
Describes the model specifications for the HH model and its synaptic parameterizations used in the manuscript. 
Generates table 1 and Figure 1.
    
`spike_centered.ipynb`
Includes the spike centered experiment. Generates table 2 and Figure 2.

`partial_history.ipynb`
Figure 3
NEEDS TO BE CLEANED UP

`nst_distribution_evolution_part1.ipynb`
Figure 4

`nst_distribution_evolution_part2.ipynb`
Figure 5 (part)

`nst_distribution_evolution_part3.ipynb`
Figure 5 (part)
NEEDS TO BE CLEANED UP

`nInputs_analysis.ipynb`
Figure 6, Figure 7

`nInputs_analysis_morpho.ipynb`
Figure 8, Figure 9

`state_reconstruction.ipynb`
Figure 10
NEEDS TO BE CLEANED UP

`state_reconstruction_morpho.ipynb`
Figure 11, Figure 12
        
        
### mod
`nInputs.mod`
Custom mod file to integrate event-based partial history input encodings in to NEURON, for the.

`morpho_nInputs.mod`
Custom mod file to integrate event-based partial history input encodings in to NEURON, for the morphologically detailed CA1 pyramidal cell.

`Nap.mod`
Passive Sodium channel used in the dendrites for the CA1 pyramidal cell. Derived from Magistretti & Alonso 1999.

`vecevent.mod`
NOT SURE IF WE USE THIS ANYMORE, CHECK!



### Morphology
`c91662.CNG.swc`
The CA1 pyramidal cell morphology file. Downloaded from https://neuromorpho.org/neuron_info.jsp?neuron_name=c91662 (Ascoli et al. 2007). Morphology originally from the work of (Ishizuka et al. 1995)
    
        
    
    
