import argparse
import shutil
from pathlib import Path


def parse_arguments():
    """
    Parses command-line arguments.
    Expects a source directory and an optional destination directory.
    """
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")

    # Argument for the source directory
    parser.add_argument("source_folder", type=str, help="Path to the source directory")

    # Argument for the destination directory (optional)
    parser.add_argument("output_folder", nargs="?", default="dist", help="Path to the destination directory")

    return parser.parse_args()

def copy_file(file_path: Path, output_folder: Path) -> None:
    """
    Copies a file to the destination folder, sorted by extension.

    Args:
        file_path (Path): Path to the source file.
        output_folder (Path): Path to the root destination directory.
    """
    try:
        # Get the file extension (without the dot). If no extension, use 'no_extension'
        extension = file_path.suffix[1:] if file_path.suffix else "no_extension"

        # Create a target directory path based on the extension
        target_dir = output_folder / extension

        # Create the directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)

        # Define the full destination path including filename
        destination_file = target_dir / file_path.name

        # Copy the file with metadata
        shutil.copy2(file_path, destination_file)
        print(f"Copied: {file_path} -> {destination_file}")

    except PermissionError:
        print(f"Error: Permission denied for file {file_path}")
    except OSError as e:
        print(f"OS Error copying {file_path}: {e}")
    except Exception as e:
        print(f"Unexpected error copying {file_path}: {e}")

def read_folder(path: Path, output_folder: Path) -> None:
    """
    Recursively iterates through the directory.

    Args:
        path (Path): Current directory path to iterate.
        output_folder (Path): Destination root folder.
    """
    try:
        # Check if the path actually exists and is a directory
        if not path.exists():
            print(f"Error: The path {path} does not exist.")
            return

        # Iterate over all items in the directory
        for item in path.iterdir():
            if item.is_dir():
                # If item is a directory, call the function recursively
                # Skip the output folder if it is created inside the source folder
                if item.resolve() == output_folder.resolve():
                    continue
                read_folder(item, output_folder)
            elif item.is_file():
                # If item is a file, perform the copy operation
                copy_file(item, output_folder)

    except PermissionError:
        print(f"Error: Permission denied for directory {path}")
    except OSError as e:
        print(f"OS Error accessing {path}: {e}")
    except Exception as e:
        print(f"Unexpected error reading {path}: {e}")

def main() -> None:
    # Parse command-line arguments
    args = parse_arguments()

    source_path = Path(args.source_folder)
    output_path = Path(args.output_folder)

    print(f"Starting process...")
    print(f"Source: {source_path}")
    print(f"Destination: {output_path}")
    print("-" * 30)

    # Start the recursive reading and copying process
    read_folder(source_path, output_path)

    print("-" * 30)
    print("Process completed.")


if __name__ == "__main__":
    main()