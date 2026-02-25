---
title: "Drug Review Sentiment & Topic Modeling"
subtitle: "Course Project — Text Mining & Search (2025–2026)"
author: "Saba Haile Asfha"
output: html_document
---

## Project Overview

This project performs large-scale **sentiment classification** and **topic modeling** on the UCI Drug Review Dataset.  

The study aims to:

- Design a principled sentiment labeling strategy  
- Compare sparse and dense text representations  
- Evaluate multiple classification models  
- Analyze latent thematic structure using topic modeling  
- Critically assess performance using appropriate evaluation metrics  

---

## Dataset

**Source:** UCI Drug Review Dataset  
**Size:** Approximately 50,000 reviews after filtering  

Each record contains:

- Drug name  
- Medical condition  
- Review text  
- Rating (1–10 scale)  
- Useful count  

### Label Design

To reduce ambiguity and improve classification reliability:

- Ratings 1–4 → **Negative**
- Ratings 7–10 → **Positive**
- Ratings 5–6 removed (neutral/noisy region)

This filtering strategy reduces label noise and strengthens class separability.

---

## Methodological Pipeline

### Exploratory Data Analysis

- Rating distribution  
- Review length distribution  
- Condition frequency analysis  
- Sentiment balance assessment  

Notebook:  
`notebooks/exploratory_data_analysis.ipynb`

---

### Text Preprocessing

- Lowercasing  
- Punctuation removal  
- Stopword filtering  
- Token normalization  

Notebook:  
`notebooks/text_preprocessing.ipynb`

---

### Text Representation

Two complementary representations were compared.

#### TF-IDF (Sparse Representation)

- High-dimensional bag-of-words representation  
- Preserves lexical frequency information  
- Effective for linear classifiers  

Notebook:  
`notebooks/TF-IDF Representation.ipynb`

#### Transformer Embeddings (Dense Representation)

- Context-aware sentence embeddings  
- Captures semantic information  
- Used with logistic regression classifier  

---

### Classification Modeling

The following models were evaluated:

- Logistic Regression (TF-IDF)  
- Linear SVM (TF-IDF)  
- Logistic Regression (BERT embeddings)  

Evaluation metrics:

- Accuracy  
- Precision  
- Recall  
- Macro F1-score  
- Confusion Matrix  

Results stored in:  
`results/classification_metrics.csv`

Confusion matrices available in:  
`results/figures/confusion_matrix_*.png`

---

### Topic Modeling

Two topic modeling approaches were implemented:

- Latent Dirichlet Allocation (LDA)  
- BERTopic  

Evaluation procedures:

- Topic coherence using NPMI  
- Topic prevalence comparison across sentiment classes  

Example outputs:

- `results/figures/topic_lda_topic_words.png`  
- `results/figures/topic_bertopic_barchart.png`  
- `results/figures/fig_eval_coherence_npmi.png`  

---

## Key Findings

- Strong separation between positive and negative classes was achieved.  
- TF-IDF combined with Linear SVM produced competitive performance.  
- Transformer embeddings improved contextual robustness.  
- Topic modeling revealed distinct thematic differences across sentiment groups.  
- NPMI coherence scores indicate moderate semantic consistency of extracted topics.  

---

## Repository Structure
drug-review-sentiment-topic-modeling/
│
├── notebooks/
│ ├── dataset_and_label_design.ipynb
│ ├── exploratory_data_analysis.ipynb
│ ├── text_preprocessing.ipynb
│ ├── TF-IDF Representation.ipynb
│ ├── classification_models.ipynb
│ ├── topic_modeling.ipynb
│ ├── evaluation_and_comparison.ipynb
│ └── error_analysis.ipynb
│
├── results/
│ ├── classification_metrics.csv
│ ├── topic_words.txt
│ └── figures/
│
├── requirements.txt
└── README.md

### Execution Order

dataset_and_label_design

exploratory_data_analysis

text_preprocessing

TF-IDF Representation

classification_models

topic_modeling

evaluation_and_comparison

error_analysis

###Evaluation Rationale

Macro F1-score was selected to ensure balanced evaluation across classes.

Confusion matrices provide interpretability of classification errors.

NPMI coherence was used to assess semantic quality of extracted topics.

All conclusions are directly supported by empirical results.

### Author

Saba Haile Asfha
MSc Data Science
University of Milano–Bicocca
