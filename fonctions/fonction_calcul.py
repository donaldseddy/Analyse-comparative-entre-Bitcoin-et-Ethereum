import pandas as pd



def calcul_z_scrore(df, value: str, period: int) -> pd.DataFrame:
    """
    This function calculates the Z-score for a given column in a DataFrame over a specified period.
    The Z-score is a statistical measure that indicates how many standard deviations a data point is from the mean.
    It helps in identifying outliers and understanding the data distribution.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    value (str): The name of the column in the DataFrame for which the Z-score needs to be calculated.
    period (int): The period over which to calculate the rolling mean and standard deviation.

    Returns:
    pd.DataFrame: The input DataFrame with an additional column 'Z_SCRORE' containing the calculated Z-scores.
    """
    rolling_mean = df[value].rolling(window=period).mean()
    rolling_std = df[value].rolling(window=period).std()
    z_score = (df[value] - rolling_mean) / rolling_std
    df['Z_SCRORE'] = z_score
    return df

