import pandas as pd


class DataReader:
    """Class for reading data from various sources."""

    def read_csv(self, file_path):
        """Read data from a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            pandas.DataFrame: DataFrame containing the data.
        """
        return pd.read_csv(file_path)

    def read_excel(self, file_path):
        """Read data from an Excel file.

        Args:
            file_path (str): Path to the Excel file.

        Returns:
            pandas.DataFrame: DataFrame containing the data.
        """
        return pd.read_excel(file_path)
