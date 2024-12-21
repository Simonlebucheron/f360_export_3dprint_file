# Fusion 360 Export Script

This script exports the active Fusion 360 design in multiple formats (STEP, Fusion Archive, STL, and 3MF). It saves the exported files to a user-selected directory with the same name as the design.

## Features

- **Export Formats**: STEP (.step), Fusion Archive (.f3d), STL (.stl), and 3MF (.3mf).
- **Custom Output Directory**: Prompts the user to select an output directory (default is `3D Objects/F360` in the user's home folder).
- **Mesh Refinement**: High mesh refinement for STL and 3MF exports.
- **File Overwrite Protection**: Automatically generates unique filenames if a file with the same name already exists.
- **User Feedback**: Displays success or failure messages.
- **Optional STL for Each Component**: Export a separate STL file for each component (set `export_individual_stl=True`).

## Requirements

- **Fusion 360**: This script must be run within Autodesk Fusion 360's scripting environment.
- **Python**: Written in Python using the `adsk` (Autodesk) library available in Fusion 360's API.

## Installation

### Manual Installation

1. **Download the Script**:
   - Download the Python script (`Fusion360ExportScript.py`).

2. **Copy the Script to the Fusion 360 Scripts Folder**:
   - Open the folder where you downloaded the script.
   - Find the default Fusion 360 scripts folder:
     ```
     %APPDATA%\Autodesk\Autodesk Fusion 360\API\Scripts
     ```
   - Copy the downloaded script into this folder.

3. **Run the Script in Fusion 360**:
   - Open Fusion 360.
   - Go to the **"Tools"** menu and select **"Scripts and Add-Ins"**.
   - The script will appear under the **Scripts** tab.
   - Select the script and click **"Run"**.

### Alternative Installation (Batch Script)

For quick installation (not tested):

1. Place the `install.bat` file in the same directory as the Python script.
2. Double-click the `install.bat` file to automatically copy the script to the correct folder.

## Usage

- Once installed, run the script from **Scripts and Add-Ins** in Fusion 360.
- Select an output directory or use the default one.
- The design will be exported in the following formats:
  - STEP (.step)
  - Fusion Archive (.f3d)
  - STL (.stl)
  - 3MF (.3mf)
- To export a separate STL for each component, pass `export_individual_stl=True` when running the script:
  
  ```python
  run(context, export_individual_stl=True)
  ```

## License

This project is licensed under the MIT License.

## Author

- **slaig**
- **Creation Date**: 13/07/2024
- **Last Update**: 21/12/2024
