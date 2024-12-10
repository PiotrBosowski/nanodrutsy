import os
import pandas as pd

def extract_spectral_data(file_path):
    """
    Extracts spectral data from a file starting at '>>>>>Begin Spectral Data<<<<<'
    and returns it as a dictionary with key-value pairs.
    
    Parameters:
        file_path (str): Path to the input file.
        
    Returns:
        dict: A dictionary where keys are the first column (float) and values are the second column (float).
    """
    data_section_started = False
    spectral_data = {}
    
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line == ">>>>>Begin Spectral Data<<<<<":
                data_section_started = True
                continue
            
            if data_section_started:
                try:
                    key, value = map(lambda x: float(x.replace(',', '.')), line.split('\t'))
                    spectral_data[key] = value
                except ValueError:
                    print(f"Skipping malformed line: {line}")
    
    return spectral_data


def process_directory(directory_path, filename_map=None):
    """
    Processes all files in the given directory, extracts spectral data using `extract_spectral_data`,
    and merges the data into a single DataFrame. Allows renaming columns based on a filename_map.
    
    Parameters:
        directory_path (str): Path to the directory containing files.
        filename_map (dict): Optional dictionary mapping filenames to desired column names.
        
    Returns:
        pd.DataFrame: A DataFrame with keys as the index and file values as columns.
    """
    data_frames = []

    # Process each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):
            spectral_data = extract_spectral_data(file_path)
            
            if spectral_data:
                # Convert dictionary to DataFrame
                column_name = filename_map.get(filename, filename) if filename_map else filename
                df = pd.DataFrame.from_dict(spectral_data, orient='index', columns=[column_name])
                data_frames.append(df)
    
    # Merge all DataFrames on their index
    if data_frames:
        merged_df = pd.concat(data_frames, axis=1)
        return merged_df
    else:
        return pd.DataFrame()



if __name__=='__main__':

    data_path = "/mnt/c/Users/piotr/Desktop/pomiary-rafal"  # Replace with your data path

    filename_map = {
        'SbSeI_Reflection_002.txt': '0.0',
        'SbSeI_Reflection_003.txt': '0.5',
        'SbSeI_Reflection_004.txt': '1.0',
        'SbSeI_Reflection_005.txt': '1.5',
        'SbSeI_Reflection_006.txt': '2.0',
        'SbSeI_Reflection_007.txt': '2.5',
        'SbSeI_Reflection_008.txt': '3.0',
        'SbSeI_Reflection_009.txt': '3.5',
        'SbSeI_Reflection_010.txt': '4.0',
        'SbSeI_Reflection_011.txt': '4.5',
        'SbSeI_Reflection_012.txt': '5',
        'SbSeI_Reflection_013.txt': '6',
        'SbSeI_Reflection_014.txt': '7',
        'SbSeI_Reflection_015.txt': '8',
        'SbSeI_Reflection_016.txt': '9',
        'SbSeI_Reflection_017.txt': '10',
        'SbSeI_Reflection_018.txt': '11',
        'SbSeI_Reflection_019.txt': '12',
        'SbSeI_Reflection_020.txt': '13',
        'SbSeI_Reflection_021.txt': '14',
        'SbSeI_Reflection_022.txt': '15',
        'SbSeI_Reflection_023.txt': '17',
        'SbSeI_Reflection_024.txt': '19',
        'SbSeI_Reflection_025.txt': '21',
        'SbSeI_Reflection_026.txt': '23',
        'SbSeI_Reflection_027.txt': '25',
        'SbSeI_Reflection_028.txt': '27',
        'SbSeI_Reflection_029.txt': '29',
        'SbSeI_Reflection_030.txt': '31',
        'SbSeI_Reflection_031.txt': '33',
        'SbSeI_Reflection_032.txt': '35',
        'SbSeI_Reflection_033.txt': '37',
        'SbSeI_Reflection_034.txt': '39',
        'SbSeI_Reflection_035.txt': '41',
        'SbSeI_Reflection_036.txt': '43',
        'SbSeI_Reflection_037.txt': '45',
        'SbSeI_Reflection_038.txt': '50',
        'SbSeI_Reflection_039.txt': '55',
        'SbSeI_Reflection_040.txt': '60',
        'SbSeI_Reflection_041.txt': '65',
        'SbSeI_Reflection_042.txt': '70',
        'SbSeI_Reflection_043.txt': '75',
        'SbSeI_Reflection_044.txt': '80',
        'SbSeI_Reflection_045.txt': '85',
        'SbSeI_Reflection_047.txt': '90',
        'SbSeI_Reflection_048.txt': '95',
        'SbSeI_Reflection_049.txt': '100',
        'SbSeI_Reflection_050.txt': '105',
        'SbSeI_Reflection_051.txt': '110',
        'SbSeI_Reflection_052.txt': '115',
        'SbSeI_Reflection_053.txt': '120',
        'SbSeI_Reflection_054.txt': '125'
    }

    merged_dataframe = process_directory(data_path, filename_map=filename_map)
    merged_dataframe[merged_dataframe > 10000] = 0
    merged_dataframe[merged_dataframe < -10000] = 0
    merged_dataframe.to_csv(f"{data_path}/processed_data.csv")
    print(merged_dataframe)
