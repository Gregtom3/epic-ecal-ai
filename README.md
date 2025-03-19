:rocket: [![Make environment](https://github.com/Gregtom3/epic-ecal-ai/actions/workflows/base-ci.yml/badge.svg)](https://github.com/Gregtom3/epic-ecal-ai/actions/workflows/base-ci.yml)


# AI for the ePIC Barrel Calorimeter

A repository for testing/implementing AI methods with the ePIC barrel calorimeter. 


## Installation

1. Clone the repository locally.
   
```
git clone https://github.com/Gregtom3/epic-ecal-ai.git
```

2. Create a new python virtual enviornment (recommended: home directory). This project was developed using Python version 3.12.

```
python3 -m venv ~/.epic-ecal-ai
```

3. Source the new environment.

```
source ~/.epic-ecal-ai/bin/activate
```

4. Install python packages for this project.

```
make install
```

Package versioning errors may be due to your local Python version. You may have to switch to Python 3.12 to install properly.

5. Test the repository locally.

```
make test
```

This should create an `artifacts/` directory containing sample plots. 

## Latest Results

Results are taken from the functions in `src/tests/`.

<details>
<summary>test02_particle-kinematics</summary>
<br>


Electron kinematics

![Electron Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/particle-kinematics/electron_kinematics.png)

Pion kinematics

![Pion Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/particle-kinematics/pion_kinematics.png)

</details>

<details>
<summary>test03_ecal-barrel</summary>
<br>
  

Electron
- ECAL Barrel Plot 1

![Electron Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/ecal-barrel/electron_ecalBarrelPlot_v1.png)

- ECAL Barrel Plot 2

![Electron Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/ecal-barrel/electron_ecalBarrelPlot_v2.png)

Pion
- ECAL Barrel Plot 1

![Pion Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/ecal-barrel/pion_ecalBarrelPlot_v1.png)

- ECAL Barrel Plot 2

![Pion Plot](https://github.com/Gregtom3/epic-ecal-ai/blob/gh-pages/artifacts/ecal-barrel/pion_ecalBarrelPlot_v2.png)

</details>

## Contact

Gregory Matousek: gregory.matousek@duke.edu

