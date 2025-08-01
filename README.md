# XML Tag Cleaner

This Python script processes XML files in bulk, removing the outer tags `<retArquivoXML>` and `<proc>`, preserving only the inner `<nfeProc>` content. It moves invalid or unprocessable files to an error folder.

## Features

- Parses `.xml` files from a specified input folder.
- Extracts and cleans up the `<nfeProc>` content.
- Removes XML namespaces for cleaner output.
- Saves processed files to a separate output folder.
- Moves malformed or unexpected XML files to an error folder.
- Uses a `config.json` for directory paths.

## Requirements

- Python 3.6+

## Setup

1. Clone or copy the script.
2. Create a `config.json` file in the same directory as the script:

```json
{
  "input_folder": "C:/path/to/input",
  "output_folder": "C:/path/to/output",
  "error_folder": "C:/path/to/error"
}
```

3. Place your `.xml` files in the input folder.

## Usage

Run the script:

```bash
python app.py
```

## Output

- **Output folder:** Contains cleaned XMLs with only `<nfeProc>`.
- **Error folder:** Contains XMLs that were malformed or didn't match expected structure.

## Notes

- The script preserves filenames.
- The XML namespace is removed for simplicity.
- Files are overwritten if already present in the output or error folders.
