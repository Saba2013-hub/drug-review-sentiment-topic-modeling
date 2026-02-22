# src/preprocessing.py
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import pandas as pd


def load_and_merge(train_path: Path, test_path: Path) -> pd.DataFrame:
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    df = pd.concat([train_df, test_df], ignore_index=True)
    return df


def clean_review_text(text: str) -> str:
    """
    Minimal, safe cleaning:
    - decode HTML entities (&#039; -> ')
    - remove URLs
    - normalize whitespace
    - lowercase
    Note: we keep punctuation for now (better for TF-IDF + later steps).
    """
    if text is None or (isinstance(text, float) and pd.isna(text)):
        return ""

    text = html.unescape(str(text))  # converts &#039; etc.
    text = re.sub(r"http\S+|www\.\S+", " ", text)  # remove URLs
    text = re.sub(r"\s+", " ", text).strip()
    text = text.lower()
    return text


def make_binary_sentiment(rating: float) -> int | None:
    """
    Convert 1–10 rating to binary sentiment:
    - negative: 1–4 -> 0
    - positive: 7–10 -> 1
    - neutral: 5–6 -> None (we drop these)
    """
    try:
        r = float(rating)
    except Exception:
        return None

    if r <= 4:
        return 0
    if r >= 7:
        return 1
    return None


def preprocess(
    train_csv: Path,
    test_csv: Path,
    out_csv: Path,
    sample_n: int | None = None,
    random_state: int = 42,
) -> pd.DataFrame:
    df = load_and_merge(train_csv, test_csv)

    # Keep required columns only (safer + simpler)
    required_cols = ["uniqueID", "drugName", "condition", "review", "rating", "date", "usefulCount"]
    present_cols = [c for c in required_cols if c in df.columns]
    df = df[present_cols].copy()

    # Drop missing reviews
    df = df.dropna(subset=["review"]).copy()

    # Clean text
    df["clean_review"] = df["review"].apply(clean_review_text)

    # Create sentiment label
    df["sentiment"] = df["rating"].apply(make_binary_sentiment)

    # Drop neutral/unknown labels
    df = df.dropna(subset=["sentiment"]).copy()
    df["sentiment"] = df["sentiment"].astype(int)

    # Optional: sample (for solo speed)
    if sample_n is not None and sample_n > 0 and sample_n < len(df):
        df = df.sample(n=sample_n, random_state=random_state).copy()

    # Ensure output folder exists
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    # Save processed dataset
    df.to_csv(out_csv, index=False)

    return df


def main():
    parser = argparse.ArgumentParser(description="Phase 1: preprocess UCI Drug Review dataset")
    parser.add_argument("--train_csv", type=str, default="data/drugsComTrain_raw.csv")
    parser.add_argument("--test_csv", type=str, default="data/drugsComTest_raw.csv")
    parser.add_argument("--out_csv", type=str, default="data/processed/reviews_processed.csv")
    parser.add_argument("--sample_n", type=int, default=60000, help="Use None or 0 for full dataset")
    args = parser.parse_args()

    df = preprocess(
        train_csv=Path(args.train_csv),
        test_csv=Path(args.test_csv),
        out_csv=Path(args.out_csv),
        sample_n=None if args.sample_n == 0 else args.sample_n,
    )

    print("Saved:", args.out_csv)
    print("Rows:", len(df))
    print("Sentiment distribution:\n", df["sentiment"].value_counts())
    print("Example cleaned review:\n", df["clean_review"].iloc[0][:300])



if __name__ == "__main__":
    main()