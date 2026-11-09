# Artificial Intelligence Applied to Industrial Control 

This repository is part of a course designed to provide students with the fundamental concepts and techniques of Artificial Intelligence (AI) currently used to solve real-world problems in Industrial Control which is lectured at the University of the Basque Country. 

Developed by [Artzai Picon](https://github.com/samtzai)

## What's Included

This course repository contains comprehensive materials organized into two different sections:

- **Notebooks**: They are meant to help the student to understand the concepts taught during the classes. They are based on python notebooks.
- **src**: As python notebooks are not suitable for professional coding, in this section, we include modular python code to help the students learn appropriate python coding.

### 📚 **Notebooks** (`notebooks/`)
- **Environment Setup** (`00_python_basics/`): Python basics and introduction
- **Introduction to AI** (`01_introduction/`): 
  - Linear model training 
  - Complex function fitting exercises
- **Predictive Maintenance** (`02_predictive_maintenance/`):
  - Supervised classification techniques
  - [AI4I 2020 machine failure classification](./notebooks/02_predictive_maintenance/01_supervised_classification/n03b_ai4i_failure_classification.ipynb): class imbalance, ROC/PR curves and cost-based thresholds ([quiz](./notebooks/02_predictive_maintenance/01_supervised_classification/n03b_ai4i_failure_classification_quiz.md))
  - Unsupervised anomaly detection
  - Overfitting prevention strategies
  - Feature selection methods
  - Complete supervised classification application
  - [NASA C-MAPSS remaining useful life prediction](./notebooks/02_predictive_maintenance/06_remaining_useful_life/n18_cmapss_rul_prediction.ipynb): feature-based MLP, 1D-CNN and LSTM models ([quiz](./notebooks/02_predictive_maintenance/06_remaining_useful_life/n18_cmapss_rul_prediction_quiz.md))
- **Steel Defects Classification** (`03_steel_defects_classification/`):
  - P6 (I): binary and multiclass classification and data augmentation with the NEU surface defect dataset ([quiz](./notebooks/03_steel_defects_classification/n14_steel_defect_data_augmentation_quiz.md))
  - P6 (II): [ResNet18 transfer learning and fine-tuning](./notebooks/03_steel_defects_classification/n17_steel_defect_neu_finetuning_resnet18.ipynb) ([quiz](./notebooks/03_steel_defects_classification/n17_steel_defect_neu_finetuning_quiz.md))
- **Reinforcement Learning** (`07_reinforcement_learning/`):
  - Q-learning tutorial with grid robot
  - Lunar lander reinforcement learning implementation
  - Pre-trained models and comprehensive quizzes

### 🛠️ **Source Code** (`src/`)
- Modular exercises (`exercise_01/` through `exercise_09/`)
- Reusable utility functions and classes
- Exercise outputs go in `outs/exercise_XX/` (not `out/`). Submit each exercise as a zip containing `src/` and `outs/`, with the report in Markdown (`.md`, not PDF).

### 💾 **Data** (`data/`)
- ECG datasets for biomedical signal processing
- Exercises 6 and 7 automatically join the two ECG zip fragments and extract `data/ecg/cut_pub_4sec.mat` on first use. Alternatively, run `python -m src.utils.prepare_ecg_data` from the repository root. In Colab, clone the repository first, change to its root with `%cd`, and run `!python -m src.utils.prepare_ecg_data`. Existing extracted data is reused; allow disk space for the archive and extracted file.

### 📋 **Configuration Files**
- `pyproject.toml`: Python project configuration
- `Makefile`: Build and automation scripts
- `general_installation.md`: Platform-specific installation guides

## Run in Google Colab

| Notebook | Colab |
|---|---|
| Python basics | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/00_python_basics/n00_python_basics_introduction.ipynb) |
| Linear model training | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/01_introduction/n01_linear_model_training.ipynb) |
| Complex function fitting | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/01_introduction/n02_complex_function_fitting.ipynb) |
| Classification tutorial | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/01_supervised_classification/n03_classification_tutorial.ipynb) |
| AI4I machine failure classification | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/01_supervised_classification/n03b_ai4i_failure_classification.ipynb) |
| K-means clustering | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/02_unsupervised_anomaly/n04_kmeans_clustering_tutorial.ipynb) |
| Simple 2D anomaly detection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/02_unsupervised_anomaly/n05_simple_2d_anomaly_detection.ipynb) |
| Anomaly detection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/02_unsupervised_anomaly/n06_anomaly_detection_tutorial.ipynb) |
| Overfitting and underfitting | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/03_overfitting/n08_overfitting_underfitting_demo_sin.ipynb) |
| PCA in 2D | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/04_feature_selection/n09_pca_2d_demonstration.ipynb) |
| PCA demonstration | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/04_feature_selection/n09_pca_demonstration.ipynb) |
| Synthetic wine quality classification | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/05_supervised_classification_app/n10_wine_quality_clf.ipynb) |
| Synthetic wine quality regression | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/05_supervised_classification_app/n11_wine_quality_reg.ipynb) |
| C-MAPSS remaining useful life prediction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/02_predictive_maintenance/06_remaining_useful_life/n18_cmapss_rul_prediction.ipynb) |
| NEU binary classification (P6 I) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/03_steel_defects_classification/n12_steel_defect_neu_binary.ipynb) |
| NEU multiclass classification (P6 I) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/03_steel_defects_classification/n13_steel_defect_neu_multiclass.ipynb) |
| NEU data augmentation (P6 I) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/03_steel_defects_classification/n14_steel_defect_neu_multiclass_augmentation.ipynb) |
| NEU ResNet18 fine-tuning (P6 II) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/03_steel_defects_classification/n17_steel_defect_neu_finetuning_resnet18.ipynb) |
| Grid robot Q-learning | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/07_reinforcement_learning/n15_grid_robot_qlearning_tutorial_training_process.ipynb) |
| Lunar Lander reinforcement learning | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samtzai/course_ai_for_industrial_control_students/blob/main/notebooks/07_reinforcement_learning/n16_lunar_lander_reinforcement_learning.ipynb) |

Complete and submit the quizzes (`.md`) as you would when working locally.

## Installation:
Follow this section if you are installing the development tools in your own computer. 
This process has been already done at the University lab. 
In that case, go to the "Open the repository in VS Code" section.

On Linux, you can use the [Makefile](./Makefile) to create the environment.

### INSTALL APPLICATIONS
<!-- 1) Install python3 from the Microsoft Store (python 3.13) -->
#### macOS
1) Install [Visual Studio Code for macOS](https://code.visualstudio.com/download).
2) Install Git by opening Terminal and running:
   ```bash
   xcode-select --install
   ```
   Follow the prompt to install the Xcode Command Line Tools; this provides Git.
3) Install the `uv` Python package manager in Terminal:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Close and reopen Terminal so `uv` is available on your `PATH`.
4) Install a compatible Python version:
   ```bash
   uv python install 3.11
   ```

#### Linux
Install `uv` from Terminal:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
1) Install Visual Studio Code and Git for Windows.
2) Install `uv` in PowerShell:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   Restart the terminal, or add `uv` to the current session's path:
   ```powershell
   $env:Path += ";$env:USERPROFILE\.local\bin"
   ```

### CONFIGURE WINDOWS POLICIES

In windows, if large directories are not allowed, change script policy in Powershell with admin rights:

1) Open PowerShell with Administrative privileges (**Run as administrator**)
2) Execute the following command to allow long paths:
```bash
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" ` -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```
3) Execute the following command in administrative rights powershell to allow script execution (**Run as administrator**)

Note: In windows, if script running rights are not allowed, change script policy in Powershell with admin rights for your user. 

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
## Configure your development stack:
1) Open VSCode
2) Install the following extensions on the extensions tab in VS Code    
    - Recommended extensions in VS Code:
        - Jupyter
        <!-- - WSL -->
        <!-- - Remote Explorer -->
        - Python
        <!-- - Excel Viewer -->
        - Git Graph
        - Rainbow CSV
        <!-- - Ruff -->
        <!-- - vscode-pydata-viewer -->
        - Markdown Preview Mermaid Support
        <!-- - Remote SSH -->
        <!-- - Material Icon Theme -->
<!-- 3) Configure git
    - In VSCode, open new terminal (menu, terminal, new)
    - Run the following commands: 
        Configure name and email in git
        ```bash
        git config --global user.name "Your Name"
        git config --global user.email "Your Email"
        ```
        set merge instead of rebase
        ```bash
        git config --global merge.rebase false
        ```
    - Close the terminal -->

## Open the repository in VS Code
1) Open VS Code
2) OPTION1: Clone the repository from github (if not downloaded from eGela)
    - Open the command palette (Ctrl+Shift+P)
    - Write "Git: Clone"
    - select "clone from github". This will help you clone the repository without the need of ssh keys
    - Write the url of the repository: https://github.com/your_group/your_project
    - Select the folder where you want to clone the repository
2) OPTION2: If downloaded  DownloadZip in github:
    - Go to code in github and select download zip
    - Unzip the folder
    - Move the unzipped folder to a short folder (e.g. C:\practicas_ia)
    -
3) Open the repository
    - Open the command palette (Ctrl+Shift+P)
    - Write "Open in Folder"
    - Select the folder where you cloned the repository

## Create environment
1) Open your project in VS Code
2) Open a new Terminal in vscode (tools->terminal-> new)
    - Execute uv to install environment
        ```bash
        uv sync
        ```
    - Assure that the environment is activated:
        - Linux/macOS:
        ```bash
        source .venv/bin/activate
        ```
        - Windows (PowerShell):
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```
  
  <!-- In windows, If you have permissions issues to run the command execute bypassing the execution permits:
      
  ```bash
    Powershell -ExecutionPolicy Bypass -File ".\scripts\create_env.ps1"
  ```
  Or allow script running the following command in a administrative rights powershell: 
  ```bash
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ``` -->

  
  When VSCODE detect that you are creating a new environment, say yes

## Run/Debug a Jupyter-Notebook in VSCODE
0) Open the notebook you want to run and make sure it is on the active tab.
1) Press Run-All option to run all the notebook 
![Selecting environment](./assets/select_env.png)
2) Select the generated environment (.venv)
 
If we want to debug step by step instead, we will go to the cell:
1) press "Run-By-Line":
2) press "run next line"
![Debugging Cell](./assets/cell_debug.png)
Remember that you can set breakpoints (red-dots). Code execution will stop there.

## Run/Debug a module in VSCODE
1) Open the repository in VS Code
2) Open the "run and debug" section
3) Select the configuration you want to run (e.g. "Python: Current Module" or "src.exercise_01.dataset")
4) Press Start debugging

<!-- ## Submitting the code
When you finish the exercise, you need to submit the code to the course coordinator.
1) Submit the code to the course coordinator by pushing the changes to your repository
```bash
git add .
git commit -m "commit message"
git push
``` -->
 
