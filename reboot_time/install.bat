echo off

echo ##Add Python27 to System Variable Path##
SETX PATH "%PATH%;C:\Python27;C:\Python27\Scripts;C:\Program Files\Mozilla Firefox;" /M

echo ##Add packages from requirements##
pip install -r requirements.txt

echo ##Finished! Press any key to exit...##
pause
shutdown -r -t 0