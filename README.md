# AIMD using VASP: Thermal Stability Analysis

This repository contains the workflow, input files, post-processing scripts, and plotting tools used for performing **Ab-Initio Molecular Dynamics (AIMD)** simulations using VASP and analyzing the thermal stability of materials.

The workflow covers the complete process from preparing AIMD calculations to visualization, thermal stability analysis, trajectory inspection, and publication-quality plotting.

---

# Workflow

## Step 1: Prepare AIMD Calculations

Prepare the required VASP input files:

* POSCAR
* INCAR
* KPOINTS
* POTCAR

Set up the molecular dynamics calculation with the desired:

* Temperature
* Time step
* Number of ionic steps
* Thermostat settings

---

## Step 2: Run AIMD Simulation

Run the molecular dynamics calculation using VASP.

After completion, important output files include:

* OUTCAR
* OSZICAR
* XDATCAR
* CONTCAR
* vasprun.xml

These files contain the information required for thermal stability analysis and visualization.

---

## Step 3: Visualize AIMD Output

Visualize the atomic motion and structural evolution during the simulation using:

* VESTA
* OVITO
* p4vasp
* ASE

This helps identify:

* Atomic diffusion
* Structural distortions
* Phase transformations
* Stability of the material

---

## Step 4: Analyze Temperature Evolution

Extract temperature data from:

* OUTCAR
* OSZICAR

Analyze:

* Temperature fluctuations
* Thermal equilibration
* Stability during simulation

---

## Step 5: Analyze Total Energy Evolution

Extract total energy information from:

* OUTCAR
* OSZICAR

Study:

* Energy fluctuations
* Convergence behavior
* Dynamic stability

---

## Step 6: Examine Atomic Trajectories

Use XDATCAR and trajectory visualization tools to investigate:

* Atomic motion
* Bond rearrangements
* Structural changes
* Diffusion processes

---

## Step 7: Generate Data using p4vasp

Use p4vasp to extract:

* Temperature data
* Total energy data
* Structural information

Export data for further analysis.

---

## Step 8: Generate Publication-Quality Plots using Python

Use the provided Python scripts to generate:

* Temperature vs Time
* Energy vs Time
* Structural evolution plots
* Thermal stability figures

Plots are suitable for:

* Journal publications
* Reports
* Presentations

---

## Step 9: Analyze AIMD Results using VASPKIT

Use VASPKIT for additional post-processing and analysis.

Generate:

* Temperature evolution plots
* Energy evolution plots
* Structural analysis data
* Additional AIMD statistics

---

## Step 10: Interpret AIMD Results

Evaluate:

* Thermal stability
* Structural stability
* Atomic diffusion behavior
* Material robustness at finite temperature

Interpret results for applications in:

* Semiconductors
* Photovoltaics
* Optoelectronics
* Energy storage
* 2D materials
* Nanomaterials

---

# Software Used

* VASP
* VASPKIT
* p4vasp
* VESTA
* OVITO
* Python
* NumPy
* Matplotlib

---

# Repository Contents

```text
├── Input_Files/
├── AIMD_Output_Data/
├── Python_Scripts/
├── Figures/
├── Example_Results/
└── README.md
```

---

# Tutorial Video

**YouTube Tutorial:**
AIMD using VASP: Thermal Stability Analysis

The video demonstrates the complete workflow from AIMD setup to post-processing and publication-quality visualization.

---

# Contact

**Deobrat QMatX**

Email: [deobratqmatx@gmail.com](mailto:deobratqmatx@gmail.com)

YouTube: Deobrat QMatX (www.youtube.com/@DeobratQMatX)

GitHub: [https://github.com/deobratsingh9](https://github.com/deobratsingh9)

---

If you find this repository useful, consider starring ⭐ the repository and subscribing to the YouTube channel for more tutorials on:

* VASP
* DFT
* AIMD
* Phonons
* Optical Properties
* GW
* BSE
* Effective Mass
* Mechanical Properties
* Solar Cell Efficiency
* Computational Materials Science
