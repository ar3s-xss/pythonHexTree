import PyPDF2
import os
import tarfile


def extract_attachments_from_pdf(pdf_path, extract_to_folder):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, "rb"))
    catalog = pdf_reader.trailer["/Root"]

    if "/Names" in catalog and "/EmbeddedFiles" in catalog["/Names"]:
        embedded_files = catalog["/Names"]["/EmbeddedFiles"]["/Names"]
        for i in range(0, len(embedded_files), 2):
            file_spec = embedded_files[i + 1].get_object()
            file_name = file_spec["/F"]
            file_data = file_spec["/EF"]["/F"].get_data()

            # Ensure the directory exists
            file_path = os.path.join(extract_to_folder, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Write the file to disk
            with open(file_path, "wb") as f:
                f.write(file_data)
            print(f"Extracted {file_name} successfully.")
    else:
        print("No embedded files found.")


def extract_tar_gz(tar_gz_path, extract_to_folder):
    with tarfile.open(tar_gz_path, "r:gz") as tar:
        tar.extractall(path=extract_to_folder)
    print(f"Extracted contents of {tar_gz_path} successfully.")


# Specify paths
pdf_path = r'C:\Users\richs\PycharmProjects\HexTree\https___www_5ewjotfbm6qf6_hexbirch_com_ares_php_1.pdf'
extract_to_folder = "ExtractedFiles"  # This is the folder name you want to use

# Ensure the extraction folder exists
os.makedirs(extract_to_folder, exist_ok=True)

# Extract attachments from PDF
extract_attachments_from_pdf(pdf_path, extract_to_folder)

# Extract contents of the .tar.gz file
tar_gz_path = os.path.join(extract_to_folder, "folder.tar.gz")
if os.path.exists(tar_gz_path):
    extract_tar_gz(tar_gz_path, extract_to_folder)
else:
    print(f"{tar_gz_path} not found.")
