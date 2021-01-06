import os
import pandas as pd
import numpy as np
from emotiondetection.config import config
from emotiondetection.utils.text_processor import text_processor
from emotiondetection.utils.lemmatiser import wordnet_lemmatizer
from sklearn.model_selection import train_test_split


def process_data(
    dataset_path, dataset_name, vocab_size, split_ratio=0.8, processor_engine="SKLEARN"
):
    """Process data with respect to the processor engine

    This function will process the text data from the given processor and store them
    in the checkpoints directory

    Parameters:
    -----------
    dataset_path: reponame/data/raw/
    dataset_name: ISEAR.csv
    vocab_size:
    Split ratio: Train-Test Split Ratio


    Returns:
    --------
    train_data
    y_train
    test_data
    y_test
    processor
    label_encoder
    """

    df = pd.read_csv(
        os.path.join(dataset_path, dataset_name), names=["#", "emotions", "texts"]
    )

    df = df.loc[df["emotions"].apply(lambda x: x not in config.REMOVED_EMOTIONS)]

    df["emotions"] = df["emotions"].map(config.EMOTIONS)

    df = df.reset_index(drop=True)

    # Create a new column of the lemmatised columns
    df["lemmatised_tokens"] = generate_lemma(df, "texts")

    # Create Corpus and Target set
    corpus = df["lemmatised_tokens"].apply(" ".join).tolist()

    target = df["emotions"]

    x_train, y_train, x_test, y_test = train_test_split(
        corpus, target, train_size=split_ratio, random_state=53
    )

    print(df)


def generate_lemma(df, col):
    """Generate lemma for given words
    This function takes the df and column containing processed sentences and
    generates lemma for each instance of the df[col]

    parameters:
    ----------
    df: working DataFrame
    col: column containing processed texts
    """
    lemma = []
    for instance in df[col].tolist():
        tokens = text_processor(instance)
        lemma.append(wordnet_lemmatizer(tokens))
    return lemma


if __name__ == "__main__":

    process_data(
        dataset_path=config.DATA_PATH,
        dataset_name=config.DATASET_NAME,
        vocab_size=400,
        split_ratio=0.8,
        processor_engine="KERAS",
    )
