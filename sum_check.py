import os
import subprocess

def compute_sha256_with_native_command(file_path):
    """Compute the SHA-256 checksum using the native Linux sha256sum command."""
    result = subprocess.run(['sha256sum', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error calculating checksum for {file_path}: {result.stderr}")
        return None
    return result.stdout.split()[0]  # Extract the checksum from the output

def list_files_recursive(directory):
    """List all files recursively in a directory."""
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def compare_checksums(directory, given_checksum):
    """Compare file checksums with a given checksum."""
    file_checksums = {}
    files = list_files_recursive(directory)
    
    for file in files:
        checksum = compute_sha256_with_native_command(file)
        if checksum is not None:
            file_checksums[file] = checksum
            
            if checksum == given_checksum:
                print(f"Checksum matches for file: {file}")
            else:
                print(f"Checksum does NOT match for file: {file}")

    return file_checksums

# Example usage
directory = "."  # Set the directory you want to start the search from
given_checksum = "your_given_checksum_here"  # Replace with the actual checksum
file_checksums = compare_checksums(directory, given_checksum)

# Optionally, print all file checksums
for file, checksum in file_checksums.items():
    print(f"File: {file}, Checksum: {checksum}")
