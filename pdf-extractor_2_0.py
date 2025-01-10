import os
import fitz  # PyMuPDF


def extract_file_from_pdf(pdf_path, target_filename, extract_to='.'):
    """
    Extracts a specific file from a PDF.

    Parameters:
    pdf_path (str): Path to the PDF file.
    target_filename (str): Name of the file to extract from the PDF.
    extract_to (str): Directory to extract the file to (default is current directory).
    """
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Loop through all pages in the PDF
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]

        # Get raw dictionary to find embedded files
        raw_dict = page.get_text("rawdict")

        if "embeddedFiles" in raw_dict:
            for embedded_file in raw_dict["embeddedFiles"]:
                file_info = pdf_document.extractFile(embedded_file["objno"])
                if file_info["name"] == target_filename:
                    # Construct the full path for the extracted file
                    extracted_file_path = os.path.join(extract_to, target_filename)

                    # Write the extracted file to disk
                    with open(extracted_file_path, "wb") as output_file:
                        output_file.write(file_info["file"])

                    print(f"File {target_filename} extracted successfully to {extracted_file_path}.")
                    return

    print(f"Error: The file {target_filename} was not found in the PDF.")


# Example usage
pdf_path = 'hextree_stirling_pdf_exploit\\https___www_3xt7swuvvthes_hexbirch_com_ares_php.pdf'  # Path to your PDF file
target_filename = 'stirling-pdf-DB.mv.db'  # Name of the file to extract
extract_to = '.'  # Directory to extract the file to (current directory by default)

extract_file_from_pdf(pdf_path, target_filename, extract_to)
