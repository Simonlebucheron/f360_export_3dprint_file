# Fusion 360 Export Script
# This script exports the active design in various formats (STEP, Fusion Archive, STL, 3MF)
# and saves them in the specified directory with the same name as the design.
# Author: slaig
# Creation: 13/07/2024
# Licence: MIT

import os
import adsk.core, adsk.fusion, traceback, tempfile

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        
        # Get the name of the active design
        designName = design.rootComponent.name
        
        # Get the ExportManager from the active design
        exportMgr = design.exportManager
        
        # Define the default output directory
        defaultOutputDir = os.path.join(os.path.expanduser('~'), '3D Objects', 'F360')
        # defaultOutputDir = tmpDir = tempfile.gettempdir()  # uncomment to use default windows temp path
        
        # Prompt user to select output directory
        folderDlg = ui.createFolderDialog()
        folderDlg.title = 'Select Output Folder'
        if folderDlg.showDialog() == adsk.core.DialogResults.DialogOK:
            outputDir = folderDlg.folder
        else:
            outputDir = defaultOutputDir
        
        # Create and execute STEP export options
        stepOptions = exportMgr.createSTEPExportOptions(os.path.join(outputDir, f'{designName}.step'))
        exportMgr.execute(stepOptions)
        
        # Create and execute Fusion Archive export options
        fusionArchiveOptions = exportMgr.createFusionArchiveExportOptions(os.path.join(outputDir, f'{designName}.f3d'))
        exportMgr.execute(fusionArchiveOptions)
        
        # Create and execute STL export options
        stlOptions = exportMgr.createSTLExportOptions(design.rootComponent, os.path.join(outputDir, f'{designName}.stl'))
        stlOptions.sendToPrintUtility = False  # Disable sending to print utility
        stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh  # Options: MeshRefinementLow, MeshRefinementMedium, MeshRefinementHigh
        exportMgr.execute(stlOptions)
        
        # Create and execute 3MF export options
        threemfOptions = exportMgr.createC3MFExportOptions(design.rootComponent, os.path.join(outputDir, f'{designName}.3mf'))
        threemfOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        exportMgr.execute(threemfOptions)
        
        # Display a message indicating successful export
        ui.messageBox(f'Design exported to: {outputDir}')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

