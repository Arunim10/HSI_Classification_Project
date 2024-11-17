import os
import requests
from tqdm import tqdm
import shutil

# Run Download First and comment the extraction code. Then comment download code and run the extraction code
# hdr_file_urls = []
# mhdr_file_urls = []

# hdr_id = "1476495"
# mhdr_id = "1476503"

# for id in range(130):
#     file = f'https://zenodo.org/records/{hdr_id}/files/{id:04d}.zip?download=1'
#     hdr_file_urls.append(file)
    
# for id in range(130):
#     file = f'https://zenodo.org/records/{mhdr_id}/files/{id:04d}.zip?download=1'
#     mhdr_file_urls.append(file)

# save_dirs = [
#     "D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//HDR_Data//",
#     "D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//Masked_HDR_Data//"
# ]

# def mkdir_overwrite(directory):
#     # If the directory exists, remove it
#     if os.path.exists(directory):
#         shutil.rmtree(directory)
#     # Create the new directory
#     os.mkdir(directory)
# # save_dir = "D:/HSI Project/Updated_Work/HSI_Classification/Minerals_Dataset/Masked_HDR_Data/"
# mkdir_overwrite(save_dirs[0])
# mkdir_overwrite(save_dirs[1])

# os.makedirs(save_dirs[0],exist_ok=True)
# os.makedirs(save_dirs[1],exist_ok=True)

# save_dir_hdr = save_dirs[0]
# for url in hdr_file_urls:
#     filename = url.split('/')[-1][:4] + ".zip"

#     if os.path.exists(os.path.join(save_dir_hdr, filename)):
#         print(f"{filename} already exists. Skipping download.")
#         continue

#     response = requests.head(url)
#     file_size = int(response.headers.get('content-length', 0))

#     # Initialize tqdm with the total file size
#     progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)

#     # Start downloading the file
#     response = requests.get(url, stream=True)
#     with open(os.path.join(save_dir_hdr, filename), 'wb') as f:
#         for data in response.iter_content(chunk_size=1024):
#             f.write(data)
#             progress_bar.update(len(data))

#     # Close the tqdm progress bar
#     progress_bar.close()

#     print(f"Downloaded {filename}")

# print("All HDR files downloaded successfully.")

# save_dir_mhdr = save_dirs[1]
# for url in mhdr_file_urls:
#     filename = url.split('/')[-1][:4] + ".zip"

#     if os.path.exists(os.path.join(save_dir_mhdr, filename)):
#         print(f"{filename} already exists. Skipping download.")
#         continue

#     response = requests.head(url)
#     file_size = int(response.headers.get('content-length', 0))

#     # Initialize tqdm with the total file size
#     progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)

#     # Start downloading the file
#     response = requests.get(url, stream=True)
#     with open(os.path.join(save_dir_mhdr, filename), 'wb') as f:
#         for data in response.iter_content(chunk_size=1024):
#             f.write(data)
#             progress_bar.update(len(data))

#     # Close the tqdm progress bar
#     progress_bar.close()

#     print(f"Downloaded {filename}")

# print("All MHDR files downloaded successfully.")

# from glob import glob
# import zipfile
# import os
# from tqdm import tqdm

# hdr_zip_paths = glob("D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//HDR_Data//*")
# hdr_extract_folder_path = f"D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//HDR_Data//Extracted_Folder//"

# mask_zip_paths = glob("D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//Masked_HDR_Data//*")
# mask_extract_folder_path = f"D://Machine Learning//Texmin_HSI//HSI_Classification_Updated//Minerals_Dataset//Masked_HDR_Data//Extracted_Folder//"

# # Create the extraction folder if it doesn't exist
# os.makedirs(hdr_extract_folder_path, exist_ok=True)
# os.makedirs(mask_extract_folder_path, exist_ok=True)

# # HDR Files
# for zip_file_path in tqdm(hdr_zip_paths,total=len(hdr_zip_paths)):
#     # Open the zip file
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         # Extract all the contents into the extraction folder
#         zip_ref.extractall(hdr_extract_folder_path)

# print("HDR Extraction complete.")

# # Masked HDR Files
# for zip_file_path in tqdm(mask_zip_paths,total=len(mask_zip_paths)):
#     # Open the zip file
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         # Extract all the contents into the extraction folder
#         zip_ref.extractall(mask_extract_folder_path)

# print("Extraction complete.")