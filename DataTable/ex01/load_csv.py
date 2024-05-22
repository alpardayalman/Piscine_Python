import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file and return it as a pandas DataFrame
    """
    try:
        if not path.endswith('.csv'):
            raise ValueError('Invalid file type')
        k = pd.read_csv(path)
        print(f"Loading dataset of dimensions {k.shape}")
        return k
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: File is badly formatted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

