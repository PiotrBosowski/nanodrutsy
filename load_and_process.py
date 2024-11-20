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

    data_path = "/mnt/c/Users/piotr/Desktop/Lab_pec_nanoprety"  # Replace with your data path

    filename_map = {
        'SbSI_Reflection_002.txt': '0.0',
        'SbSI_Reflection_003.txt': '0.5',
        'SbSI_Reflection_004.txt': '1.0',
        'SbSI_Reflection_005.txt': '1.5',
        'SbSI_Reflection_006.txt': '2.0',
        'SbSI_Reflection_007.txt': '2.5',
        'SbSI_Reflection_008.txt': '3.0',
        'SbSI_Reflection_009.txt': '3.5',
        'SbSI_Reflection_010.txt': '4.0',
        'SbSI_Reflection_011.txt': '4.5',
        'SbSI_Reflection_012.txt': '5',
        'SbSI_Reflection_013.txt': '6',
        'SbSI_Reflection_014.txt': '7',
        'SbSI_Reflection_015.txt': '8',
        'SbSI_Reflection_016.txt': '9',
        'SbSI_Reflection_017.txt': '10',
        'SbSI_Reflection_018.txt': '11',
        'SbSI_Reflection_019.txt': '12',
        'SbSI_Reflection_022.txt': '15',
        'SbSI_Reflection_023.txt': '17',
        'SbSI_Reflection_024.txt': '19',
        'SbSI_Reflection_025.txt': '21',
        'SbSI_Reflection_026.txt': '23',
        'SbSI_Reflection_027.txt': '25',
        'SbSI_Reflection_028.txt': '27',
        'SbSI_Reflection_029.txt': '29',
        'SbSI_Reflection_030.txt': '31',
        'SbSI_Reflection_031.txt': '33',
        'SbSI_Reflection_032.txt': '35',
        'SbSI_Reflection_033.txt': '37',
        'SbSI_Reflection_034.txt': '39',
        'SbSI_Reflection_035.txt': '41',
        'SbSI_Reflection_036.txt': '43',
        'SbSI_Reflection_037.txt': '45',
        'SbSI_Reflection_038.txt': '50',
        'SbSI_Reflection_039.txt': '55',
        'SbSI_Reflection_040.txt': '60',
        'SbSI_Reflection_041.txt': '65',
        'SbSI_Reflection_042.txt': '70',
        'SbSI_Reflection_043.txt': '75',
        'SbSI_Reflection_044.txt': '80',
        'SbSI_Reflection_045.txt': '85',
        'SbSI_Reflection_047.txt': '90',
        'SbSI_Reflection_048.txt': '95',
        'SbSI_Reflection_049.txt': '100',
        'SbSI_Reflection_050.txt': '105',
        'SbSI_Reflection_051.txt': '110',
        'SbSI_Reflection_052.txt': '115',
        'SbSI_Reflection_053.txt': '120',
        'SbSI_Reflection_054.txt': '125'
    }

    merged_dataframe = process_directory(data_path, filename_map=filename_map)
    merged_dataframe.to_csv(f"{data_path}/processed_data.csv")
    print(merged_dataframe)
