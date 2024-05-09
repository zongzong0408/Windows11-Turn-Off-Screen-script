@echo off
echo Tool: running command [rundll32.exe user32.dll, LockWorkStation]
echo Tool: To lock screen immediately.
echo Tool: running command after 5 seconds.
timeout /t 5 /nobreak >nul 
rundll32.exe user32.dll, LockWorkStation

echo Tool: running command [powercfg -change monitor-timeout-ac 1]
echo Tool: To set monitor [display off] option to [1 minute] (in situation that using AC power).
echo Tool: running command after 3 seconds.
timeout /t 3 /nobreak >nul 
powercfg -change monitor-timeout-ac 1

echo Tool: to lock the screen and turn off screen successfully.
echo Tool: auto close program in 3 seconds.
timeout /t 3 /nobreak >nul 
