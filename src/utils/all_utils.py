import yaml
import os

def read_yaml(path_to_yaml : str) -> dict:
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
        
        return content
    except FileNotFoundError as fnf:
        print(fnf)


def create_dir(dirs : list):
    try:
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
            print(f"directory is created at {dir_path}")
    except Exception as e:
        print(e)


def save_local_df(data,data_path,index_status=False):
    data.to_csv(data_path, index = index_status)
    print(f"Data is saved at {data_path}")
    
