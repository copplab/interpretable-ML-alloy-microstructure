# interpretable-ML-alloy-microstructure
# Magnesium-Based Machine Learning Models

This repository contains the code used in the study:

**"Machine Learning-Guided Discovery of Factors Governing Deformation Twinning in Mg–Y Alloys"**  
*Peter Mastracco, Kehang Yu, et al.*  
Published in *Advanced Engineering Materials*, 2025.  
[DOI: 10.1002/adem.202402485](https://doi.org/10.1002/adem.202402485)

The goal of this work is to use interpretable machine learning to uncover microstructural features that govern deformation twinning in magnesium–yttrium (Mg–Y) alloys. The included scripts support vector machine modeling, classification, feature selection, and hyperparameter optimization, all of which contributed to the findings of the publication.

---

## Installation

Install required Python packages using pip:

```bash
pip install numpy pandas scikit-learn xgboost BorutaShap matplotlib
```

## Usage
1. Training Regression Models
Run the following script to train and the accuracy of training dataset.

2. Decision Tree Regression
To generate decision trees used to further evaluate feature importance and interactions. 

3. Feature Selection with BorutaShap
Used to determine the most important features for classifying deformation twinning:

4. Hyperparameter Tuning
To optimize model hyperparameters using cross-validated grid search

## Citation
If you use this code or datasets in your work, please cite the following paper:

Mastracco, P., et al.
Machine Learning-Guided Discovery of Factors Governing Deformation Twinning in Mg–Y Alloys
Advanced Engineering Materials (2025).
DOI: 10.1002/adem.202402485



