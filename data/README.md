## Selected Dataset

The project uses the **UCI Machine Learning Drug Review Dataset**  
(also distributed via Kaggle; originally compiled by Jessica Li et al.).

### Files Used

- `drugsComTrain_raw.csv`
- `drugsComTest_raw.csv`

The two files were merged to form a single dataset for analysis.

### Dataset Size

Approximately 200,000 patient drug reviews in total.

### Data Type

The dataset contains real-world, raw textual reviews collected by crawling online pharmaceutical review platforms.  

Each record consists of a free-text patient review accompanied by structured metadata.

### Main Fields

- `review` — Free-text patient review  
- `rating` — Satisfaction score (1–10 scale)  
- `drugName` — Name of the medication  
- `condition` — Medical condition treated  
- `date` — Review date  
- `usefulCount` — Number of users who found the review helpful  
- `uniqueID` — Record identifier  

---

## Suitability for the Course

This dataset is appropriate for a Text Mining and Search project because:

- It provides raw text requiring full preprocessing.
- It enables supervised text classification using the rating (or condition) as ground truth.
- It supports unsupervised topic modeling on large-scale natural language data.
- Its size allows comparative experiments across representations (e.g., TF-IDF vs contextual embeddings).
- It enables meaningful quantitative evaluation and critical discussion.

---

## Usage Constraints

According to the dataset source:

- Intended for research and learning purposes only.
- Non-commercial use.
- Redistribution of the raw data is not permitted.

For this reason, the raw dataset is not included in this repository.  
Users must download it directly from the official source.
