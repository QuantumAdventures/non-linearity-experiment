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
    git clone git@github.com:QuantumAdventures/non-linearity-experiment.git
    ```

    * Or, by downloading the .zip of the repo and unziping in your computer.

2. Install the requirements, this will set the libraries needed with the correct version in your computer. Inside the main folder of the project run the following command:

```bash
pip install -r requirements.txt
```

3. Install the project. This step is mandatory, inside the root folder of the project run the following command on terminal



```bash
python setup.py install
```



3. Download the data! A `data` folder is needed, to get all the data used and produced in the experiment you can

    * Follow the link [here](https://drive.google.com/drive/folders/1OXutfn_C_7TzHMjxG4hueFKlQWNWipJT), and download it.

    * The recommendation is to download only a fraction of the data

## Usage

With the data downloaded and the project package installed, all the notebooks can be executed. One important observation is regarding the plots; all the plots use a LaTeX plugin. It is important to ensure that you are able to use this plugin on your machine. If not, we recommend installing it or commenting the code lines at the beginning of each notebook where the plot settings are made.

## FPGA

The complete FPGA project implemetend in the Red Pitaya can be found zipped [here](https://drive.google.com/file/d/13oADYg178D4p4PZ8vpfv2hjXdbjD0Tjp/view?usp=drive_link)

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


Project Link: [Repository](https://github.com/QuantumAdventures/non-linearity-experiment)

## References

To be added in the future, but will look something like this

Authors *Title* **Journal of Randomic Random Things**. Year.
[doi:xx.XXXXX/](doi:xx.XXXX/)