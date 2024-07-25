import os


def categorize_files_by_type(folder_path):

    # Check if the provided path exists
    if not os.path.exists(folder_path):
        raise ValueError(f"The path '{folder_path}' does not exist.")

    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        raise ValueError(f"The path '{folder_path}' is not a directory.")

    # Initialize dictionary for storing result
    res = {}

    # Walk through the directory tree
    for root, dirnames, filenames in os.walk(folder_path):

        # Walk through files
        for filename in filenames:

            # Create full path for file
            full_file_path = os.path.join(root, filename)

            # Get the file extension
            file_extension = os.path.splitext(filename)[1]

            # Initialize the list for this extension if it doesn't exist
            if file_extension not in res:
                res[file_extension] = []

            # Append the full file path to the list for this extension
            res[file_extension].append(full_file_path)

    # Return result
    return res


result = categorize_files_by_type("/path/to/root/folder")
print(result)
