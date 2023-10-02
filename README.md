# Code for the Non-Linearity Project

This repo includes the code to process and analyse the data for the Non-Linearity experiment. Here we are going to present:


* Simulation of a nanoparticle under the influence a non-linear force with and without a delay, and also the effects of adding a Butterworth filter to our setup.
* Methods to analyse the traces gathered during the execution of our experiment.
* Vivado project used to program the FPGA in the Red Pitaya board


## Installation

Well, now, how can you run this code? Follow the next steps.

1. First clone this repo in your computer. This can be done
    * Via SSH:

    ```bash
    git clone https://github.com/QuantumAdventures/non-linearity-experiment.git
    ```

    * Via HTTPS:

    ```bash
    git clone git@github.com:QuantumAdventures/optical-bottle-beam.git
    ```

    * Or, by downloading the .zip of the repo and unziping in your computer.

2. Install the requirements, this will set the libraries needed with the correct version in your computer. Inside the main folder of the project run the following command:

```bash
pip install -r requirements.txt
```

3. Download the data! A `data` folder is needed, to get all the data used and produced in the experiment you can

    * Follow the link [here](https://drive.google.com/drive/folders/1OXutfn_C_7TzHMjxG4hueFKlQWNWipJT), and download it.

    * The recommendation is to download only a fraction of the data


In the end you should have the following directory structure:


    ├── data
    │   ├── dataframes
    │   │   ├── filtered
    │   │   ├── outliers
    │   │   └── raw
    │   ├── images
    │   │   ├── circle
    │   │   ├── hour
    │   │   ├── long
    │   │   └── square
    │   ├── plots
    │   ├── quadrant
    │   ├── results
    │   ├── simulations
    │   │   ├── error_analysis
    │   │   ├── kl
    │   │   └── obb_nas
    │   └── videos
    ├── notebooks
    │   ├── 1. Create frames from video.ipynb
    │   ├── 2. Microparticle detection and tracking.ipynb
    │   ├── 2.1. Execute detection for multiple images.ipynb
    │   ├── 3. Potential Analysis with Multiple Parameters.ipynb
    │   ├── 4. Kullback-Leibler Analysis.ipynb
    │   ├── 5. Error Analysis for Intermediate Regime.ipynb
    │   └── 6. Gaussianity tests for optical tweezers.ipynb
    ├── scripts
    │   ├── calculate_psd_of_experiments.py
    │   ├── calculate_psd_of_simulations.py
    │   ├── DFT_simulation.m
    ├── LICENSE
    ├── README.md
    └── requirements.txt

## Usage

With the data downloaded, all the notebooks can be executed. To execute the scripts, run the following command inside the `optical-bottle-beam` folder:

```bash
python scripts/calculate_psd_of_experiments.py
```

Or 

```bash
python scripts/calculate_psd_of_simulations.py
```



## License

This code is licensed by:

General Public License version 3.0 [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)


Copyright (C) 2022  Quantum Adventures: Pontifical University of Rio de Janeiro
research group for optomechanics, quantum optics and quantum information.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Contact

#Name - [Linkedin](https://www.linkedin.com/in) [Email](email)
#Name - [Linkedin](https://www.linkedin.com/in) [Email](email)
#Name - [Linkedin](https://www.linkedin.com/in) [Email](email)
#Name - [Linkedin](https://www.linkedin.com/in) [Email](email)


Project Link: [Repository](https://github.com/QuantumAdventures/optical-bottle-beam)

## References

To be added in the future, but will look something like this

Authors *Title* **Journal of Randomic Random Things**. Year.
[doi:xx.XXXXX/](doi:xx.XXXX/)