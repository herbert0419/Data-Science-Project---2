import os
from pathlib import Path


package_name = 'ANPR'

list_of_files = [
    f"ANPR/src/{package_name}/__init__.py",
    f"ANPR/src/{package_name}/components/__init__.py",
    f"ANPR/src/{package_name}/components/data_ingestion.py",
    f"ANPR/src/{package_name}/components/data_transformation.py",
    f"ANPR/src/{package_name}/components/prepare_base_model.py",
    f"ANPR/src/{package_name}/components/model_trainer.py",
    f"ANPR/src/{package_name}/components/model_pusher.py",
    f"ANPR/src/{package_name}/config/__init__.py",
    f"ANPR/src/{package_name}/constants/__init__.py",
    f"ANPR/src/{package_name}/entity/__init__.py",
    f"ANPR/src/{package_name}/exception/__init__.py",
    f"ANPR/src/{package_name}/logger/__init__.py",
    f"ANPR/src/{package_name}/utils/__init__.py",
    f"ANPR/src/{package_name}/pipeline/__init__.py",
    "ANPR/notebooks/data_collection.py",
    "ANPR/notebooks/ocr.py",
    "ANPR/requirements.txt",
    "ANPR/app.py"

]

for file_path in list_of_files:
    file_path =  Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir!='':
        os.makedirs(file_dir,exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass # Create an empty array & do nothing