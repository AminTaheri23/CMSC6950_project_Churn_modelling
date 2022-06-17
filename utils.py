import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class data_utils:
    def __init__(self):
        pass
    def get_data(self, file_name):
        """get the data from file

        Args:
            file_name (string): name of the file

        Returns:
            data: list of strings
        """        
        with open(file_name, 'r') as f:
            data = f.read()
        return data
    def get_data_csv(self, file_name):
        """read the csv file and put in a dataframe

        Args:
            file_name (string): The name of the file

        Returns:
            pd.DataFrame: data frame of the csv file
        """        
        df = pd.read_csv(file_name)
        return df
class visualizer:
    def __init__(self):
        pass

    def plot_data_bins(self, df):
        """plots the distribution of the data in bins

        Args:
            df (pd.DataFrame): The dataframe to be plotted
        """        
        df.hist(bins=50, figsize=(18, 15))
        plt.show()

    def plot_data_based_on_target(self, dataset, rows, cols, plot_type, column_names, target_name):
        """plot different types of plots for the data

        Args:
            dataset (pd.DataFrame): the desired dataframe
            rows (integer): number of rows for the plot
            cols (integer): number of columns for the plot
            plot_type (string): you should choose between 'box', 'violin'
            column_names (list of strings): list of columns to be plotted
            target_name (string): the name of the target column
        """        
        number_of_column = len(column_names)
        fig, axes = plt.subplots(rows, cols, figsize=(20, 16))

        counter = 0
        for i in range(rows):
            for j in range(cols):
                if 'violin' in plot_type:
                    sns.violinplot(
                        x=target_name, y=column_names[counter], data=dataset, ax=axes[i][j])
                elif 'box' in plot_type:
                    sns.boxplot(
                        x=target_name, y=column_names[counter], data=dataset, ax=axes[i][j])
               

                counter += 1
                if counter == (number_of_column-1,):
                    break


class ordinal_encoder:
    def __init__(self):
        pass
    def encode_ordinal(self, df, column_name):
        """encode the ordinal data

        Args:
            df (DataFrame): the dataframe to be encoded
            column_name (string): the name of the column to be encoded

        Returns:
            DataFrame: the encoded dataframe
        """        
        # unique values in the column
        unique_values = df[column_name].unique()
        # create a dictionary to map the unique values to integers
        mapping = {val: i for i, val in enumerate(unique_values)}
        # map the values in the column to the integers
        df[column_name] = df[column_name].map(mapping)
        return df

class outlier_handling():
    def __init__(self) -> None:
        pass
    def handle (self, df):
        """deletes the outliers from the dataframe in range of 1.5 times the IQR

        Args:
            df (DataFrame): the dataframe to remove the outliers from

        Returns:
            DataFrame: the dataframe without the outliers
        """        
        dim1, dim2 = df.shape
        print(dim1, dim2)
        # Delete outliers based on feature values for all rows and features with IQR if it's bigger than 2 times of the IQR.
        for i in range(len(df.columns) - 1):
            q1, q3 = np.percentile(df.iloc[:, i], [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5) # 1.5 times the IQR
            upper_bound = q3 + (iqr * 1.5) # 1.5 times the IQR
            df.drop(df[df.iloc[:, i] < lower_bound].index, inplace=True) 
            df.drop(df[df.iloc[:, i] > upper_bound].index, inplace=True)
        print("Number of deleted data for outliers", dim1 - df.shape[0]) # print the number of deleted data
        return df

if __name__ == "__main__":
    pass