# Solving the Travelling Salesman Problem (TSP) with Simulated Annealing

## Overview

This code carries out multiple experiments of solving TSP by Simulated Annealing.
We explore various cooling schemes (logarithmic, linear, and exponential) as well as two 
edit functions (2-opt and single city swap).

The main objective of this code is to gain insight into which cooling scheme and edit
function performs best with respect to finding a minimum circuit length. Our secondary
goal is comparing the outcomes with the provided global minimum.

The core component of the code is given in the Last Notebook.ipynb file which contains the
Simulated Annealing class and methods for various cooling schemes and edit functions. The
research questions are answered based on the t-test values at the end of the notebook in the 
"Statistics" portion of the code.

The experiments are carried out on three different problem instances of increasing number
of cities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

```bash
git clone https://github.com/koenweverink/stochastic_simulation_assignment_2.git
cd stochastic_simulation_assignment_1
pip install -r requirements.txt
```
