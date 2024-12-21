@echo off
set "SCRIPT_NAME=Export_3Dprint_for_publishing.py"
set "TARGET_DIR=%APPDATA%\Autodesk\Autodesk Fusion 360\API\Scripts"

echo Copying script to Fusion 360 scripts directory...

copy /Y "%SCRIPT_NAME%" "%TARGET_DIR%"

echo Script copied successfully!
pause
