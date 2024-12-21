# Fusion 360 Export Script
# This script exports the active design in various formats (STEP, Fusion Archive, STL, 3MF)
# and saves them in the specified directory with the same name as the design.
# Author: slaig
# Creation: 13/07/2024
# Last update : 21/12/2024
# Licence: MIT

import os
import adsk.core, adsk.fusion, traceback, tempfile

# Function to check and create a unique filename if the file already exists
def check_and_create_unique_filename(filepath):
    """
    Checks if the file already exists. If it does, adds a numeric suffix to make it unique.
    """
    base, ext = os.path.splitext(filepath)
    counter = 1
    while os.path.exists(filepath):
        filepath = f"{base}_{counter}{ext}"
        counter += 1
    return filepath

# Function to export to STEP format
def export_step(exportMgr, designName, outputDir):
    """
    Exports the design to STEP format, ensuring the file name is unique.
    """
    stepFilepath = os.path.join(outputDir, f'{designName}.step')
    stepFilepath = check_and_create_unique_filename(stepFilepath)
    stepOptions = exportMgr.createSTEPExportOptions(stepFilepath)
    exportMgr.execute(stepOptions)

# Function to export to Fusion Archive format
def export_fusion_archive(exportMgr, designName, outputDir):
    """
    Exports the design to Fusion Archive format (.f3d), ensuring the file name is unique.
    """
    fusionArchiveFilepath = os.path.join(outputDir, f'{designName}.f3d')
    fusionArchiveFilepath = check_and_create_unique_filename(fusionArchiveFilepath)
    fusionArchiveOptions = exportMgr.createFusionArchiveExportOptions(fusionArchiveFilepath)
    exportMgr.execute(fusionArchiveOptions)

# Function to export to STL format for a given component
def export_stl(exportMgr, design, designName, outputDir, component=None):
    """
    Exports the design or a given component to STL format, ensuring the file name is unique.
    Sets mesh refinement to high.
    """
    if component is None:
        # If no component is passed, export the root component (default behavior)
        component = design.rootComponent
    
    stlFilepath = os.path.join(outputDir, f'{component.name}.stl')
    stlFilepath = check_and_create_unique_filename(stlFilepath)
    stlOptions = exportMgr.createSTLExportOptions(component, stlFilepath)
    stlOptions.sendToPrintUtility = False  # Disable sending to print utility
    stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    exportMgr.execute(stlOptions)

# Function to export to 3MF format
def export_3mf(exportMgr, design, designName, outputDir):
    """
    Exports the design to 3MF format, ensuring the file name is unique.
    Sets mesh refinement to high.
    """
    threemfFilepath = os.path.join(outputDir, f'{designName}.3mf')
    threemfFilepath = check_and_create_unique_filename(threemfFilepath)
    threemfOptions = exportMgr.createC3MFExportOptions(design.rootComponent, threemfFilepath)
    threemfOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    exportMgr.execute(threemfOptions)

# Main function that orchestrates the exports
def run(context, export_individual_stl=True):
    """
    Main function to export the design in multiple formats (STEP, Fusion Archive, STL, and 3MF).
    
    Parameters:
    - export_individual_stl (bool): If True, exports each component as a separate STL file.
    """
    ui = None
    try:
        app = adsk.core.Application.get()  # Get the active Fusion 360 application instance
        ui = app.userInterface  # Get the user interface for message display
        design = app.activeProduct  # Get the active design
        
        # Get the name of the design
        designName = design.rootComponent.name
        
        # Get the ExportManager from the active design
        exportMgr = design.exportManager
        
        # Define the default output directory
        defaultOutputDir = os.path.join(os.path.expanduser('~'), '3D Objects', 'F360')
        
        # Prompt the user to select an output directory
        folderDlg = ui.createFolderDialog()
        folderDlg.title = 'Select Output Folder'
        if folderDlg.showDialog() == adsk.core.DialogResults.DialogOK:
            outputDir = folderDlg.folder  # Get the selected folder
        else:
            outputDir = defaultOutputDir  # Use the default directory if canceled
        
        # Export the design in all formats
        export_step(exportMgr, designName, outputDir)
        export_fusion_archive(exportMgr, designName, outputDir)
        export_3mf(exportMgr, design, designName, outputDir)

        # Export individual STLs if the flag is set to True
        if export_individual_stl:
            # Iterate over all components in the design and export STL for each
            for occurrence in design.rootComponent.occurrences:
                export_stl(exportMgr, design, designName, outputDir, occurrence.component)

        else:
            # Export STL for the root component if not exporting individual STLs
            export_stl(exportMgr, design, designName, outputDir)

        # Display success message
        ui.messageBox(f'Design exported to: {outputDir}')
        
    except Exception as e:
        if ui:
            # If an error occurs, display an error message
            ui.messageBox('Failed:\n{}'.format(str(e)))
