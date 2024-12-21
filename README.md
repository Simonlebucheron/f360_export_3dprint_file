# Fusion 360 Export Script

This script allows you to export the active Fusion 360 design in multiple formats (STEP, Fusion Archive, STL, and 3MF). It will automatically save the exported files in a user-selected directory with the same name as the design.

## Features

- **Export Formats**: STEP (.step), Fusion Archive (.f3d), STL (.stl), and 3MF (.3mf).
- **Custom Output Directory**: Prompts the user to select an output directory, with a default set to `3D Objects/F360` in the user's home folder.
- **Mesh Refinement**: Provides high mesh refinement for STL and 3MF exports.
- **File Overwrite Protection**: If a file with the same name already exists, a unique filename will be created by adding a numeric suffix.
- **User Feedback**: Displays a message indicating the success or failure of the export process.

## Requirements

- **Fusion 360**: This script is intended to be run within Autodesk Fusion 360's scripting environment.
- **Python**: This script is written in Python and uses the `adsk` (Autodesk) library, which is available in Fusion 360's API environment.

## Installation

### Manual Installation

1. **Download the Script**:
   - Download the Python script (`Fusion360ExportScript.py`).

2. **Copy the Script to the Fusion 360 Scripts Folder**:
   - Open the folder where you downloaded the script.
   - To find the default Fusion 360 scripts folder on your system, press `Win + R` to open the Run dialog.
   - Type the following path and press Enter:
     ```
     %APPDATA%\Autodesk\Autodesk Fusion 360\API\Scripts
     ```
   - This will open the **Scripts** folder used by Fusion 360.
   - Copy the downloaded Python script (`Fusion360ExportScript.py`) into this folder.

3. **Run the Script in Fusion 360**:
   - Open Fusion 360.
   - Go to the **"Tools"** menu and select **"Scripts and Add-Ins"**.
   - You should now see the script listed under the **Scripts** tab.
   - Select the script and click **"Run"** to execute it.

### Alternative Installation (Using a Batch Script)

Warning, not tested

1. **Run the Batch Script**:
   - Place the `install.bat` file in the same directory as the downloaded Python script.
   - Double-click on the `install.bat` file. It will automatically copy the script to the correct folder.

## Usage

- Once the script is copied and visible in **Scripts and Add-Ins**, simply run it from within Fusion 360.
- You will be prompted to select an output directory (or use the default one).
- The design will be exported in the selected formats: STEP, Fusion Archive, STL, and 3MF.

## License

This project is licensed under the MIT License.

## Author

- **slaig**
- **Creation Date**: 13/07/2024
- **Last update**: 21/12/2024
